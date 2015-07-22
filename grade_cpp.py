import config, json, cgi, sys, Websheet, re, os

void_functions = []

def pre(s, specialBlank = False):
  if len(s) > 10000:
    s = s[:10000] + "\n... " + str(len(s)-10000) + " characters truncated"
  if (specialBlank and s==""):
    return "<pre><i>(no output)</i></pre>"
  return "<pre>\n" + cgi.escape(s) + "</pre>"

def tt(s):
  return "<code>" + cgi.escape(s) + "</code>"

def execute(command, stdin):
  return config.execute(command, stdin, output_encoding='Latin-1')

def grade(reference_solution, student_solution, translate_line, websheet):
    cpp_compiler = config.config_jo["cpp_compiler"]

    unusable_cppflags = []

    # following http://bits.usc.edu/cs103/compile/
    default_cppflags = ["-g",
                        "-Wall", "-Wshadow", "-Wunreachable-code",
                        "-Wconversion",
                        "-Wno-sign-compare", "-Wno-write-strings"]
    if "clang" in cpp_compiler: # good options, but not in g++
        default_cppflags += ["-Wvla", "-Wno-shorten-64-to-32", "-Wno-sign-conversion", "-fsanitize=undefined"]
    else:
      unusable_cppflags = ["-Wno-array-bounds","-Wno-return-stack-address","-Wunreachable-code"]

    websheet.unusable_cppflags = unusable_cppflags

    # create a temp directory
    refdir = config.create_tempdir()
    studir = config.create_tempdir()

    # put slug.cpp
    jail = config.config_jo["java_jail-abspath"]
    refcpp = open(jail + refdir + websheet.slug + ".cpp", "w")
    refcpp.write(reference_solution)
    refcpp.close()
    
    stucpp = open(jail + studir + websheet.slug + ".cpp", "w")
    stucpp.write(student_solution)
    stucpp.close()
    
    suffix = ""
    if websheet.lang == "C++func": suffix = ".o"

    compile_list = [cpp_compiler] + websheet.cppflags(default_cppflags)
    
    compile_args = []
    if websheet.lang == "C++func":
      compile_args += ["-c"]      
    compile_args += [websheet.slug + ".cpp", "-o", websheet.slug + suffix]

    # build reference
    os.chdir(jail + refdir)
    refcompile = execute(compile_list + compile_args, "")
    if (refcompile.stderr != "" or refcompile.returncode != 0
        or not os.path.isfile(jail + refdir + websheet.slug + suffix)):
        return ("Internal Error (Compiling Reference)",
                "cmd:"+pre(" ".join(compile_list))+
                "<br>stdout:"+pre(refcompile.stdout)+
                "<br>stderr:"+pre(refcompile.stderr)+
                "<br>retval:"+pre(str(refcompile.returncode)))

    # build student
    os.chdir(jail + studir)
    stucompile = execute(compile_list + compile_args, "")
      
    result = "<div>Compiling: saving your code as "+tt(websheet.slug+".cpp")
    result += " and calling "+tt(" ".join(["compile"] + compile_args))
    if stucompile.stdout!="":
      result += pre(stucompile.stdout)
    result += "</div>"
    if (stucompile.stderr != "" or stucompile.returncode != 0
        or not os.path.isfile(jail + studir + websheet.slug + suffix)):
      msg = re.sub('(\.cpp:)(\d+)(?!\d)', 
                   lambda m : m.group(1)+translate_line(m.group(2)),
                   stucompile.stderr)
      result += "<div>Did not compile. Error message:"+pre(msg)+"</div>"
      return ("Syntax Error", result)

    if len(websheet.tests)==0:
      return ("Internal Error", "No tests defined!")

    def example_literal(cpptype):
      known = {"int":"0", "double":"0.0", "bool":"false", "char":"'x'", "string":'""', "char*": '(char*)NULL', "char[]": '""'}
      if cpptype in known: return known[cpptype]
      return None

    for test in websheet.tests:
      if websheet.lang =='C++func' and test[0]=="check-function":
        funcname = test[1]
        returntype = test[2]
        if (returntype == "void"):
          global void_functions
          void_functions += [funcname]
        argtypes = test[3]
        literals = [None] * len(argtypes)
        for i in range(len(literals)):
          literals[i] = example_literal(argtypes[i])
          if literals[i] == None:
            return ("Internal Error", tt("need example_literal for " + argtypes[i]))
        tester = student_solution 
        tester += "\n#include <iostream>\n" + returntype + "(*some_unique_identifier)(" + ', '.join(argtypes) + ") = &" + funcname + ";"
        tester += "\n" + " void even_uniquer() { " + funcname + "(" + ', '.join(literals) + ");}"
        tester += "\n" + "int main() {}\n"

        newslug = websheet.slug + "test"
        cpp = open(jail + refdir + newslug + ".cpp", "w")
        cpp.write(tester)
        cpp.close()

        compile_list = [cpp_compiler] + websheet.cppflags(default_cppflags)

        compile_list += [newslug + ".cpp", "-o", newslug + suffix]

        os.chdir(jail + refdir)
        refcompile = execute(compile_list, "")

        if (refcompile.stderr != "" or refcompile.returncode != 0
            or not os.path.isfile(jail + refdir + websheet.slug + suffix)):
          text = ("<div><!--"+refcompile.stderr+"-->"+
                  "You must define a function " 
                  + tt(funcname) + 
                  ( " taking no arguments" if len(argtypes)==0 else 
                    (" taking arguments of types " + tt(", ".join(argtypes))))
                  + " and with return type " + tt(returntype) + "</div>")

          return ("Failed Tests",
                  text + "<!--" +
                  "stdout:"+pre(refcompile.stdout)+
                  "<br>stderr:"+pre(refcompile.stderr)+
                  "<br>retval:"+pre(str(refcompile.returncode))
          +"-->"   )
              
        continue # check-function
      
      if websheet.lang=='C++func' and test[0]=="call-function":
        funcname = test[1]
        args = test[2]        
        testline = funcname + "(" + ', '.join(args) + ")"
        testmain = "\n#include <iostream>\nint main(){std::cout << std::showpoint << std::boolalpha;"
        if funcname not in void_functions: testmain += "std::cout << "
        testmain += testline + ";}\n"
        stutester = student_solution + testmain
        reftester = reference_solution + testmain
        newslug = websheet.slug + "test"

        compile_list = [cpp_compiler] + websheet.cppflags(default_cppflags)

        compile_list += [newslug + ".cpp", "-o", newslug]

        cpp = open(jail + refdir + newslug + ".cpp", "w")
#        print(reftester)
        cpp.write(reftester)
        cpp.close()
        os.chdir(jail + refdir)
        refcompile = execute(compile_list, "")

        if (refcompile.stderr != "" or refcompile.returncode != 0
            or not os.path.isfile(jail + refdir + newslug)):
          return ("Internal Error: Reference Type Check Failed",
                  "<!--" +
                  "stdout:"+pre(refcompile.stdout)+
                  "<br>stderr:"+pre(refcompile.stderr)+
                  "<br>retval:"+pre(str(refcompile.returncode))
                  +"-->"   )

        cpp = open(jail + studir + newslug + ".cpp", "w")
        cpp.write(stutester)
        cpp.close()
        os.chdir(jail + studir)
        stucompile = execute(compile_list, "")

        if (stucompile.stderr != "" or stucompile.returncode != 0
            or not os.path.isfile(jail + refdir + newslug)):
          return ("Internal Error: Type Check Failed",
                  "<!--" +
                  "stdout:"+pre(stucompile.stdout)+
                  "<br>stderr:"+pre(stucompile.stderr)+
                  "<br>retval:"+pre(str(stucompile.returncode))
          +"-->"   )
         # call-function
        if funcname in void_functions:
          result += "<div>Calling " + tt(testline) + "&hellip;</div>"
        else:
          result += "<div>Printing the result of calling " + tt(testline) + "&hellip;</div>"

        exename = newslug
        stdin = ""
        args = []
      if websheet.lang=='C++': # normal test, calling main
        stdin = ""
        args = []
        if 'stdin' in test:
          stdin = test['stdin']
        if 'args' in test:
          args = test['args']

        cmd = websheet.slug
        if len(args) > 0: cmd += " " + " ".join(args)
        result += "<div>Running " + tt("./" + cmd)

        if len(stdin) > 0: 
          result += " on input " + pre(stdin)
        else:
          result += "&hellip;"
        result += "</div>"

        exename = websheet.slug
      
      cfg = config.config_jo

      cmd = [cfg["safeexec-executable-abspath"]]
      cmd += ["--chroot_dir", cfg["java_jail-abspath"]]
      cmd += ["--exec_dir", "/" + refdir]
      cmd += ["--clock", "1"]
      cmd += ["--mem", "40000"]
      cmd += ["--exec", exename]
      cmd += args

      runref = execute(cmd, stdin)

      if runref.returncode != 0 or not runref.stderr.startswith("OK"):
        result += "<div>Reference solution crashed!"
        result += "<br>stdout:"+pre(runref.stdout)
        result += "stderr:"+pre(runref.stderr)
        result += "val:"+pre(str(runref.returncode))
        result += "</div>"
        return ("Internal Error", result)

      cmd = [cfg["safeexec-executable-abspath"]]
      cmd += ["--chroot_dir", cfg["java_jail-abspath"]]
      cmd += ["--exec_dir", "/" + studir]
      cmd += ["--clock", "1"]
      cmd += ["--mem", "40000"]
      cmd += ["--exec", exename]
      cmd += args

      runstu = execute(cmd, stdin)
      if runstu.returncode != 0 or not runstu.stderr.startswith("OK"):
        result += "<div>Crashed! "
        errmsg = runstu.stderr
        if "elapsed time:" in errmsg:
          errmsg = errmsg[:errmsg.index("elapsed time:")]
        errmsg = errmsg.replace("Command terminated by signal (8: SIGFPE)",
                                "Floating point exception")
        errmsg = errmsg.replace("Command terminated by signal (11: SIGSEGV)",
                                "Segmentation fault (core dumped)")
        if errmsg != "":
          result += "Error messages:" + pre(errmsg)
        if runstu.stdout != "":
          result += "Produced this output:"+pre(runstu.stdout)
#        result += "Return code:"+pre(str(runstu.returncode))
        result += "</div>"
        return ("Sandbox Limit", result)
      
      if websheet.example:
        result += "<div>Printed this output:"
        result += pre(runstu.stdout) + "</div>"
        continue

      stucanon = re.sub(' +$', '', runstu.stdout, flags=re.MULTILINE)
      refcanon = re.sub(' +$', '', runref.stdout, flags=re.MULTILINE)

      if (stucanon == refcanon 
          or stucanon == refcanon + "\n" and not refcanon.endswith("\n")):
        result += "<div>Passed! Printed this correct output:"
        result += pre(runstu.stdout, True) + "</div>"
      elif stucanon == refcanon + "\n":
        result += "<div>Failed! Printed this output:"
        result += pre(runstu.stdout, True)
        result += "which is almost correct but <i>you printed an extra newline at the end</i>.</div>"
        return ("Failed Tests", result)
      elif refcanon == stucanon + "\n":
        result += "<div>Failed! Printed this output:"
        result += pre(runstu.stdout, True)
        result += "which is almost correct but <i>you are missing a newline at the end</i>.</div>"
        return ("Failed Tests", result)
      else:
        result += "<div>Failed! Printed this incorrect output:"
        result += pre(runstu.stdout, True)
        result += "Expected this correct output instead:"
        result += pre(runref.stdout, True) + "</div>"
        return ("Failed Tests", result)

    if websheet.example:
      return ("Example", result)
    else:
      result += "<div>Passed all tests!</div>"
      return ("Passed", result)
      
