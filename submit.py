#!/usr/bin/python3

if __name__ == "__main__":
  import sys, Websheet, json, re, cgi, os
  from config import run_java, run_javac, scratch_dir

  student = sys.argv[2]
  websheet = Websheet.Websheet.from_filesystem(sys.argv[1])
  classname = websheet.classname
  stdin = input() # assume json all on one line

  def main():
    if not re.match(re.compile("^[a-z0-9]+$"), student):
        return("Error: invalid student name", 1, False)

    user_poschunks = json.loads(stdin)

    # this is the pre-syntax check
    student_solution = websheet.make_student_solution(user_poschunks, "student."+student)
    if student_solution[0] == False:
        return("<div class='pre-syntax-error'>Syntax error:" + 
               "<pre>\n"+cgi.escape(student_solution[1])+"</pre></div>", # error text
               0, False)
    ss_to_ui_linemap = student_solution[2]
    def translate_line(ss_lineno):
        ss_lineno = int(ss_lineno)
        if ss_lineno in ss_to_ui_linemap:
            return str(ss_to_ui_linemap[ss_lineno])
        else:
            return "???("+str(ss_lineno)+")"
        
    reference_solution = websheet.get_reference_solution("reference")

    with open("GenericTester.java") as file:
        GTjava = "\n".join(file)

    dump = {
        "reference/" + classname + ".java" : reference_solution,
        "student/" + student + "/" + classname + ".java" : student_solution[1],
        "tester/" + classname + ".java" : websheet.make_tester(),
        "framework/GenericTester.java" : GTjava,
        }

    studir = scratch_dir + "student/" + student + "/"
    if not os.path.exists(studir):
      os.makedirs(studir)

    for filename in dump:
        file = open(scratch_dir + filename, "w")
        file.write(dump[filename])
        file.close()

    compileTester = run_javac("framework/GenericTester.java "
                              + "reference/" + classname + ".java "
                              + "tester/" + classname + ".java")
    
    if compileTester.returncode != 0:
        return ("<pre>\n" + 
                cgi.escape(compileTester.stdout) + "\n" +
                cgi.escape(compileTester.stderr) +
                "</pre>", 1, False)

    compileUser = run_javac("student/" + student + "/" + classname + ".java")
        
    if compileUser.returncode != 0:
        result = "Syntax error (could not compile):"
        result += "<pre>\n"
        #remove the safeexec bits
        compilerOutput = cgi.escape(compileUser.stderr).split("\n")
        for i in range(0, len(compilerOutput)):
            # transform error messages
            if compilerOutput[i].startswith("student/"+student+"/"+classname+".java:"):
                linesep = compilerOutput[i].split(':')
                linesep[1] = "Line " + translate_line(linesep[1])
                compilerOutput[i] = ":".join(linesep[1:])
            result += compilerOutput[i] + "\n"
        result += "</pre>"
        return (result, 0, False)

    runUser = run_java("tester." + classname + " " + student)

    if runUser.returncode != 0:
        result = runUser.stdout
        result += "<div class='safeexec'>Crashed! The grader reported "
        result += "<code>"
        result += cgi.escape(runUser.stderr.split('\n')[0])
        result += "</code>"
        result += "</div>"
        return (result, 0, False)

    runtimeOutput = re.sub(
        re.compile("at line (\d+) "),
        lambda match: "at line " + translate_line(match.group(1)) + " ",
        runUser.stdout)

    passed = "<div class='all-passed'>" in runtimeOutput 
    if passed and websheet.epilogue is not None:
        runtimeOutput += "<div class='epilogue'>" + websheet.epilogue + "</div>"
        
    return (runtimeOutput, 0, passed)

  output, returncode, passed = main()
  import config
  config.save_submission(student, classname, stdin, output)
  print(json.dumps({'results': output, 'passed': passed, 'internal_err': returncode != 0}))
  sys.exit(returncode)
