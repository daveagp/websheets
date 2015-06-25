#!/usr/bin/python3

"""
always produces:
 - results, an html fragment to display to the user
 - category: "Internal Error"/"Pre-syntax Error"/"Syntax Error"/"Sandbox Limit"/"Runtime Error"/"Failed Tests"/"Passed"
   ... it should correspond to the exit point from the logic in this script
sometimes produces:
 - errmsg, the high-level description of the error (without line numbers)
 - epilogue, commentary after a submission
"""
import config, json, cgi

cpp_compiler = "clang++-3.5"
default_cppflags = [
  "-Wall", "-Wvla", "-Wshadow", "-Wunreachable-code",
  "-Wconversion",
  "-Wno-shorten-64-to-32", "-Wno-sign-conversion",
  "-Wno-sign-compare", "-Wno-write-strings",
  "-g"]

void_functions = []

def pre(s, specialBlank = False):
  if len(s) > 10000:
    s = s[:10000] + "\n... " + str(len(s)-10000) + " characters truncated"
  if (specialBlank and s==""):
    return "<pre><i>(no output)</i></pre>"
  return "<pre>\n" + cgi.escape(s) + "</pre>"

def tt(s):
  return "<code>" + cgi.escape(s) + "</code>"

def submit_and_log(websheet_name, student, client_request, meta):
  import sys, Websheet, re, os
  from config import run_java

  config.meta = meta

  websheet = Websheet.Websheet.from_filesystem(websheet_name)
  classname = websheet.classname

  errmsg = None
  epilogue = None
  
  def compile_and_run():
    nonlocal errmsg, epilogue

    if websheet.nocode:
      if websheet.evaluate_nocode_submission(client_request["nocode_state"]):
        return ("Passed", "<div>Correct!</div>")
      else:
        return ("Failed", "<div>Not correct, please try again.</div>")

    user_poschunks = client_request["snippets"]

    # this is the pre-syntax check
    student_solution = websheet.combine_with_template(user_poschunks, "student")
    if student_solution[0] == False:
        if student_solution[1] == "Internal error! Wrong number of inputs":
          return("Internal Error (Wrong number of snippets)", "Error: wrong number of snippets")

        errmsg = student_solution[1].split('\n')
        if len(errmsg) > 1:
          errmsg = errmsg[1]
        else:
          errmsg = errmsg[0]
        
        return("Pre-syntax Error",
               "<div class='pre-syntax-error'>Syntax error:" + 
               "<pre>\n"+cgi.escape(student_solution[1])+"</pre></div>") # error text
    ss_to_ui_linemap = student_solution[2]

    def translate_line(ss_lineno):
        ss_lineno = int(ss_lineno)
        if ss_lineno in ss_to_ui_linemap:
          return str(ss_to_ui_linemap[ss_lineno])
        else:
          return "???("+str(ss_lineno)+")" + "<!--" + json.dumps(ss_to_ui_linemap) + "-->"
        
    reference_solution = websheet.get_reference_solution("reference")

    ss = student_solution[1]
    for i in range(len(ss)):
      if ord(ss[i]) >= 128:
        return("Pre-syntax Error",
               "<div class='pre-syntax-error'>Syntax error:" + 
               " Your code contains a non-ASCII character:<br>" + 
               "<pre>"
               +("&hellip;" if i>5 else "")
               +cgi.escape(ss[max(0,i-5):i])
               +"<b style='background:orange'>"
               +cgi.escape(ss[i])+"</b>"
               +cgi.escape(ss[i+1:i+6])
               +("&hellip;" if i+5<len(ss) else "")
               +"</pre></div>")

    for verboten in websheet.verboten:
        for chunk in user_poschunks:
          if verboten in chunk['code']:
            return("Pre-syntax Error",
                   "<div class='pre-syntax-error'>" + 
                   "You can't use " + tt(verboten) + 
                   " in this exercise.</div>")

    dump = {
        "reference." + classname : reference_solution,
        "student." + classname : student_solution[1],
#        "tester." + classname : websheet.make_tester()
        }

#    for clazz in ["Grader", "Options", "Utils"]:
#      dump["websheets."+clazz] = "".join(open(clazz+".java"))

    #print(cgi.escape(student_solution[1]))
    #print(cgi.escape(reference_solution))

    student_solution = student_solution[1]
    if websheet.mode == "func":
      student_solution = re.sub(r"\bmain\b", "__student_main__", student_solution)

    for dep in websheet.dependencies:
      depws = Websheet.Websheet.from_filesystem(dep)
      submission = config.load_submission(student, dep, True)
      if submission == False:
        return("Dependency Error",
               "<div class='dependency-error'><i>Dependency error</i>: " + 
               "You need to successfully complete the <a href='javascript:loadProblem(\""+dep+"\")'><tt>"+dep+"</tt></a> websheet first (while logged in).</div>") # error text
      submission = [{'code': x, 'from': {'line': 0, 'ch':0}, 'to': {'line': 0, 'ch': 0}} for x in submission]
      dump["student."+dep] = depws.combine_with_template(submission, "student")[1]
      
      dump["reference."+dep] = depws.get_reference_solution("reference")

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
    if websheet.mode == "func": suffix = ".o"

    compile_list = [cpp_compiler] + websheet.cppflags(default_cppflags)
    
    compile_args = []
    if websheet.mode == "func":
      compile_args += ["-c"]      
    compile_args += [websheet.slug + ".cpp", "-o", websheet.slug + suffix]

    # build reference
    os.chdir(jail + refdir)
#    refcompile = config.execute("make " + websheet.slug, "")
    refcompile = config.execute(compile_list + compile_args, "")
    if (refcompile.stderr != "" or refcompile.returncode != 0
        or not os.path.isfile(jail + refdir + websheet.slug + suffix)):
        return ("Internal Error (Compiling Reference)",
                "cmd:"+pre(" ".join(compile_list))+
                "<br>stdout:"+pre(refcompile.stdout)+
                "<br>stderr:"+pre(refcompile.stderr)+
                "<br>retval:"+pre(str(refcompile.returncode)))

    # build student
    os.chdir(jail + studir)
    stucompile = config.execute(compile_list + compile_args, "")
      
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
      if test[0]=="check-function":
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
        tester += "\n" + "int main() {}"

        newslug = websheet.slug + "test"
        cpp = open(jail + refdir + newslug + ".cpp", "w")
        cpp.write(tester)
        cpp.close()

        compile_list = [cpp_compiler] + websheet.cppflags(default_cppflags)

        compile_list += [newslug + ".cpp", "-o", newslug + suffix]

        os.chdir(jail + refdir)
        refcompile = config.execute(compile_list, "")

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
      
      if test[0]=="call-function":
        funcname = test[1]
        args = test[2]        
        testline = funcname + "(" + ', '.join(args) + ")"
        testmain = "\n#include <iostream>\nint main(){std::cout << std::showpoint << std::boolalpha;"
        if funcname not in void_functions: testmain += "std::cout << "
        testmain += testline + ";}"
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
        refcompile = config.execute(compile_list, "")

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
        stucompile = config.execute(compile_list, "")

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
      else: # normal test, calling main
        stdin = test[0]
        args = test[1]

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
      cmd += ["--exec", exename]
      cmd += args

      runref = config.execute(cmd, stdin)

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
      cmd += ["--exec", exename]
      cmd += args

      runstu = config.execute(cmd, stdin)
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
      
  try:
    category, results = compile_and_run()
    config.uncreate_tempdirs()
  except Exception:
    category = "Internal Error (Script)"
    import traceback
    results = '<pre>' + cgi.escape(traceback.format_exc()) + '</pre>'

  if category.startswith("Internal Error"):
    results = "<b><p>"+category+"; please report to course staff!</p></b>" + results

  import copy
    
  print_output = {'category': category, 'results' : results}
  save_this = {'category': category}
  if errmsg is not None:
    print_output['errmsg'] = errmsg
    save_this['errmsg'] = errmsg
  if epilogue is not None: # no need to log this
    print_output['epilogue'] = epilogue

  passed = (category == "Passed")

  global authinfo
  #print(authinfo)
  if authinfo["error_div"] != "":
    print_output["results"] = authinfo["error_div"]
    print_output["category"] = "Auth Error" 
    meta["logout_bug"] = True

  if (not client_request["viewing_ref"]):
    if websheet.nocode:
      user_state = client_request["nocode_state"]
    else:
      # remove positional information
      user_state = [blank["code"] for blank in client_request["snippets"]]
    config.save_submission(student, websheet.dbslug, user_state, save_this, passed)

  if passed or websheet.attempts_until_ref == 0: 
    print_output["reference_sol"] = websheet.get_reference_snippets()
    
  return print_output

if __name__ == "__main__":
  import sys

  global authinfo

  stdin = json.loads(input()) # assume json all on one line
  authinfo = stdin["authinfo"]
  student = stdin["php_data"]["user"]
  websheet_name = stdin["php_data"]["problem"]
 
  meta = stdin["php_data"]["meta"]
  
  if "frontend_user" in stdin["client_request"]:
    meta["frontend_user"] = stdin["client_request"]["frontend_user"]
 
  data = submit_and_log(websheet_name, student, stdin["client_request"], meta) 

  print(json.dumps(data, 
                   indent=4, separators=(',', ': '))) # pretty!
  sys.exit(0)

