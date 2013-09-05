#!/usr/bin/python3

if __name__ == "__main__":

    import sys, Websheet, json, re, cgi
    
    student = sys.argv[2]
    websheet = Websheet.Websheet.from_filesystem(sys.argv[1])

    if not re.match(re.compile("^[a-z0-9]+$"), student):
        print("Error: invalid student name")
        exit(1)

    stdin = input() # assume json all on one line
    user_poschunks = json.loads(stdin)

    # this is the pre-syntax check
    student_solution = websheet.make_student_solution(user_poschunks, "student."+student)
    if student_solution[0] == False:
        print("<div class='pre-syntax-error'>Syntax error:")
        print("<pre>"+cgi.escape(student_solution[1])+"</pre></div>") # error text
        exit(0)
    ss_to_ui_linemap = student_solution[2]
    def translate_line(ss_lineno):
        ss_lineno = int(ss_lineno)
        if ss_lineno in ss_to_ui_linemap:
            return str(ss_to_ui_linemap[ss_lineno])
        else:
            return "???("+str(ss_lineno)+")"
        
    reference_solution = websheet.get_reference_solution("reference")

    classname = websheet.classname

    with open("GenericTester.java") as file:
        GTjava = "\n".join(file)

    from submit_config import run_java, run_javac, scratch_dir
              
    dump = {
        "reference/" + classname + ".java" : reference_solution,
        "student/" + student + "/" + classname + ".java" : student_solution[1],
        "tester/" + classname + ".java" : websheet.make_tester(),
        "framework/GenericTester.java" : GTjava,
        }

    for filename in dump:
        file = open(scratch_dir + filename, "w")
        file.write(dump[filename])
        file.close()

    compileTester = run_javac("framework/GenericTester.java "
                              + "reference/" + classname + ".java "
                              + "tester/" + classname + ".java")
    
    if compileTester.returncode != 0:
        print("<pre>")
        print(cgi.escape(compileTester.stdout))
        print(cgi.escape(compileTester.stderr))
        print("</pre>")
        exit(1)

    compileUser = run_javac("student/" + student + "/" + classname + ".java")
        
    if compileUser.returncode != 0:
        print("Syntax error (could not compile):")
        print("<pre>")
        #remove the safeexec bits
        compilerOutput = cgi.escape(compileUser.stderr).split("\n")[:-5]
        for i in range(0, len(compilerOutput)):
            # transform error messages
            if compilerOutput[i].startswith("student/"+student+"/"+classname+".java:"):
                linesep = compilerOutput[i].split(':')
                linesep[1] = "Line " + translate_line(linesep[1])
                compilerOutput[i] = ":".join(linesep[1:])
            print(compilerOutput[i])
        print("</pre>")
        exit(0)

    runUser = run_java("tester." + classname + " " + student)

    if runUser.returncode != 0:
        print(runUser.stdout)
        print("<div class='safeexec'>Crashed! The grader reported ")
        print("<code>")
        print(cgi.escape(runUser.stderr.split('\n')[0]))
        print("</code>")
        print("</div>")
        exit(0)

    runtimeOutput = re.sub(
        re.compile("at line (\d+) "),
        lambda match: "at line " + translate_line(match.group(1)) + " ",
        runUser.stdout)

    if "<div class='all-passed'>" in runtimeOutput and websheet.epilogue is not None:
        runtimeOutput += "<div class='epilogue'>" + websheet.epilogue + "</div>"
        
    print(runtimeOutput)
