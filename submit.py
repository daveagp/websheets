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
errmsg = None
epilogue = None

if __name__ == "__main__":
  import sys, Websheet, json, re, cgi, os
  from config import run_java, run_javac, scratch_dir

  student = sys.argv[2]
  websheet = Websheet.Websheet.from_filesystem(sys.argv[1])
  classname = websheet.classname
  stdin = input() # assume json all on one line
  user_state = json.loads(stdin)

  def main():
    global errmsg, epilogue
    if not re.match(re.compile("^[a-z0-9]+$"), student):
        return("Internal Error (Student)", "Error: invalid student name")

    user_poschunks = user_state["snippets"]

    # this is the pre-syntax check
    student_solution = websheet.make_student_solution(user_poschunks, "student."+student)
    if student_solution[0] == False:
        errmsg = student_solution[1].split('\n')[1]
        return("Pre-syntax Error",
               "<div class='pre-syntax-error'>Syntax error:" + 
               "<pre>\n"+cgi.escape(student_solution[1])+"</pre></div>") # error text
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
        return ("Internal Error (Compiling)", "<pre>\n" + 
                cgi.escape(compileTester.stdout) + "\n" +
                cgi.escape(compileTester.stderr) +
                "</pre>")

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
                if errmsg is None: errmsg = ":".join(linesep[2:])
                linesep[1] = "Line " + translate_line(linesep[1])
                compilerOutput[i] = ":".join(linesep[1:])
            result += compilerOutput[i] + "\n"
        result += "</pre>"
        return ("Syntax Error", result)

    runUser = run_java("tester." + classname + " " + student)

    if runUser.returncode != 0:
        errmsg = runUser.stderr.split('\n')[0]
        result = runUser.stdout
        result += "<div class='safeexec'>Crashed! The grader reported "
        result += "<code>"
        result += cgi.escape(errmsg)
        result += "</code>"
        result += "</div>"
        return ("Sandbox Limit", result)

    runtimeOutput = re.sub(
        re.compile("at line (\d+) "),
        lambda match: "at line " + translate_line(match.group(1)) + " ",
        runUser.stdout)

    def ssf(s, t, u): # substring from of s from after t to before u
      s = s[s.index(t)+len(t) : ]
      return s[ : s.index(u)]
    
    if "<div class='error'>Runtime error:" in runtimeOutput:
      category = "Runtime Error"
      errmsg = ssf(runtimeOutput, "<pre >\n", "\n")
    elif "<div class='all-passed'>" in runtimeOutput:
      category = "Passed"
      epilogue = websheet.epilogue
    else:
      category = "Failed Tests"
      errmsg = ssf(runtimeOutput, "<div class='error'>", '</div>')
      
    return (category, runtimeOutput)

  try:
    category, results = main()
  except Exception:
    category = "Internal Error (Script)"
    import traceback
    results = '<pre>' + cgi.escape(traceback.format_exc()) + '</pre>'

  if category.startswith("Internal Error"):
    results = "<b><p>Internal Error; please report to course staff!</p></b>" + results

  import copy
    
  print_output = {'category': category, 'results' : results}
  save_this = {'category': category}
  if errmsg is not None:
    print_output['errmsg'] = errmsg
    save_this['errmsg'] = errmsg
  if epilogue is not None: # no need to log this
    print_output['epilogue'] = epilogue

  passed = (category == "Passed")
  import config

  if (not user_state["viewing_ref"]):
    # remove positional information
    user_snippets = [blank["code"] for blank in user_state["snippets"]]
    config.save_submission(student, classname, user_snippets, save_this, passed)

  print(json.dumps(print_output))
  sys.exit(0)
