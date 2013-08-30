#!/usr/bin/python3

def make_tester(ws):
    
    return (
"package tester;\n" +
"import java.util.Random;\n" +
"import static framework.GenericTester.*;\n" +
"public class " + ws.classname + " extends framework.GenericTester {\n" +
"{className=\"" + ws.classname + "\";}" +
"protected void runTests() {" +
ws.tests +
"\n}" +
("" if ws.tester_preamble is None else ws.tester_preamble) +
" public static void main(String[] args) {" +
ws.classname + " to = new " + ws.classname + "();\n" + 
"to.genericMain(args);\n" + 
"}\n}"
)

if __name__ == "__main__":

    import sys, Websheet, json
    
    module = __import__(sys.argv[1])
    student = sys.argv[2]
    websheet = Websheet.Websheet.from_module(module)
    import re
    if not re.match(re.compile("^[a-z0-9]+$"), student):
        print("Error: invalid student name")
        exit(1)

    stdin = input() # assume json all on one line
    user_poschunks = json.loads(stdin)

    student_solution = websheet.make_student_solution(user_poschunks, "student."+student)
    if student_solution[0] == False:
        print("<p>Syntax error:</p>")
        print(student_solution[1]) # Error
        exit(0)

    reference_solution = websheet.get_reference_solution("reference")

    classname = websheet.classname

    ss_to_ui_linemap = student_solution[2]

    with open("GenericTester.java") as file:
        GTjava = "\n".join(file)
              
    dump = {
        "/home/cscircles/dev_java_jail/scratch/reference/" + classname + ".java" : reference_solution,
        "/home/cscircles/dev_java_jail/scratch/student/" + student + "/" + classname + ".java" : student_solution[1],
        "/home/cscircles/dev_java_jail/scratch/tester/" + classname + ".java" : make_tester(websheet),
        "/home/cscircles/dev_java_jail/scratch/framework/GenericTester.java" : GTjava,
        }

    for filename in dump:
        file = open(filename, "w")
        file.write(dump[filename])
        file.close()

    javac = "/java/bin/javac -J-Xmx128M "

    java = "/java/bin/java -Xmx128M "

    safeexec = "/home/cscircles/dev/safeexec/safeexec"

    jail = "/home/cscircles/dev_java_jail/"

    safeexec_args = " --chroot_dir "+ jail +" --exec_dir /scratch --env_vars '' --nproc 50 --mem 500000 --nfile 30 --clock 2 --exec "

    call0 = (safeexec + " --fsize 1000" + safeexec_args + javac + "-cp . framework/GenericTester.java"
    + " reference/" + classname + ".java"
    + " tester/" + classname + ".java")
    call3 = safeexec + " --fsize 1000" + safeexec_args + javac + "student/" + student + "/" + classname + ".java"
    call4 = safeexec + safeexec_args + java + "tester." + classname + " " + student

    from subprocess import Popen, PIPE

    proc = Popen(call0.split(" "), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    result = proc.communicate(input = "")

    import cgi
    
    if proc.returncode != 0:
        print("<pre>")
        print(cgi.escape(result[0].decode("UTF-8")))
        print(cgi.escape(result[1].decode("UTF-8")))
        print("</pre>")
        exit(1)
    
    proc = Popen(call3.split(" "), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    result = proc.communicate(input = "")

    def translate_line(ss_lineno):
        ss_lineno = int(ss_lineno)
        if ss_lineno in ss_to_ui_linemap:
            return str(ss_to_ui_linemap[ss_lineno])
        else:
            return "???("+str(ss_lineno)+")"
        
    if proc.returncode != 0:
        print("Syntax error (could not compile):")
        print("<pre>")
        #remove the safeexec bits
        compilerOutput = cgi.escape(result[1].decode("UTF-8")).split("\n")[:-5]
        for i in range(0, len(compilerOutput)):
            # transform error messages
            if compilerOutput[i].startswith("student/"+student+"/"+classname+".java:"):
                linesep = compilerOutput[i].split(':')
                linesep[1] = "Line " + translate_line(linesep[1])
                compilerOutput[i] = ":".join(linesep[1:])
            print(compilerOutput[i])
        print("</pre>")
        exit(0)

    proc = Popen(call4.split(" "), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    result = proc.communicate(input = "")

    if proc.returncode != 0:
        print(result[0].decode("UTF-8"))
        print("<div class='safeexec'>Crashed! The grader reported ")
        print("<code>")
        print(cgi.escape(result[1].decode("UTF-8").split('\n')[0]))
        print("</code>")
        print("</div>")
        exit(0)

    runtimeOutput = result[0].decode("UTF-8")
    runtimeOutput = re.sub(
        re.compile("at line (\d+) "),
        lambda match: "at line " + translate_line(match.group(1)) + " ",
        runtimeOutput)
    print(runtimeOutput)
