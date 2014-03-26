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
import config, json

def submit_and_log(websheet_name, student, client_request, meta):
  import sys, Websheet, re, cgi, os
  from config import run_java

  config.meta = meta

  websheet = Websheet.Websheet.from_filesystem(websheet_name)
  classname = websheet.classname

  errmsg = None
  epilogue = None
  
  def compile_and_run():
    nonlocal errmsg, epilogue

    user_poschunks = client_request["snippets"]

    # this is the pre-syntax check
    student_solution = websheet.make_student_solution(user_poschunks, "student")
    if student_solution[0] == False:
        if student_solution[1] == "Internal error! Wrong number of inputs":
          return("Internal Error (Wrong number of snippets)", "Error: wrong number of snippets")
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
        GTjava = "".join(file)

    dump = {
        "reference." + classname : reference_solution,
        "student." + classname : student_solution[1],
        "tester." + classname : websheet.make_tester(),
        "framework.GenericTester" : GTjava,
        }

    #print(student_solution[1])

    for dep in websheet.dependencies:
      depws = Websheet.Websheet.from_filesystem(dep)
      submission = config.load_submission(student, dep, True)
      if submission == False:
        return("Dependency Error",
               "<div class='dependency-error'><i>Dependency error</i>: " + 
               "You need to successfully complete the <a href='javascript:loadProblem(\""+dep+"\")'><tt>"+dep+"</tt></a> websheet first (while logged in).</div>") # error text
      submission = [{'code': x, 'from': {'line': 0, 'ch':0}, 'to': {'line': 0, 'ch': 0}} for x in submission]
      dump["student."+dep] = depws.make_student_solution(submission, "student")[1]
      
      dump["reference."+dep] = depws.get_reference_solution("reference")
      
    compileRun = run_java("traceprinter/ramtools/CompileToBytes", json.dumps(dump))
    compileResult = compileRun.stdout
    if (compileResult==""):
      return ("Internal Error (Compiling)", "<pre>\n" + 
              cgi.escape(compileRun.stderr) +
              "</pre>")
    
    compileObj = json.loads(compileResult)

#    print(compileObj['status'])

    if compileObj['status'] == 'Internal Error':
      return ("Internal Error (Compiling)", "<pre>\n" + 
              cgi.escape(compileObj["errmsg"]) +
              "</pre>")
    elif compileObj['status'] == 'Compile-time Error':
        result = "Syntax error (could not compile):"
        result += "<br>"
        errorObj = compileObj['error']
        result += '<tt>'+errorObj['filename'].split('.')[-2]+'.java</tt>, line '
        result += str(translate_line(errorObj['row'])) + ':'
        #result += str(errorObj['row']) + ':'
        result += "<pre>\n"
        #remove the safeexec bits
        result += cgi.escape(errorObj["errmsg"])
        result += "</pre>"
        return ("Syntax Error", result)

#    print(compileResult)
    
    runUser = run_java("traceprinter/ramtools/RAMRun tester." + classname + " " +student, compileResult)
    #runUser = run_java("tester." + classname + " " + student)

    #print(runUser.stdout)
    RAMRunError = runUser.stdout.startswith("Error")
    RAMRunErrmsg = runUser.stdout[:runUser.stdout.index('\n')]

    runUser.stdout = runUser.stdout[runUser.stdout.index('\n')+1:]

    #print(runUser.stdout)
    #print(runUser.stderr)

    if runUser.returncode != 0 or runUser.stdout.startswith("Time Limit Exceeded"):
        errmsg = runUser.stderr.split('\n')[0]
        result = runUser.stdout
        result += "<div class='safeexec'>Crashed! The grader reported "
        result += "<code>"
        result += cgi.escape(errmsg)
        result += "</code>"
        result += "</div>"
        result += "<!--" + runUser.stderr + "-->"
        return ("Sandbox Limit", result)

    if RAMRunError:
        result += "<div class='safeexec'>Could not execute! "
        result += "<code>"
        result += cgi.escape(RAMRunErrmsg)
        result += "</code>"
        result += "</div>"
        return ("Internal Error (RAMRun)", result)
      
    runtimeOutput = re.sub(
        re.compile("at line (\d+) "),
        lambda match: "at line " + translate_line(match.group(1)) + " ",
        runUser.stdout)

    #print(runtimeOutput)

    def ssf(s, t, u): # substring from of s from after t to before u
      if t not in s: raise ValueError("Can't ssf("+s+","+t+","+u+")") 
      s = s[s.index(t)+len(t) : ]
      return s[ : s.index(u)]
    
    if "<div class='error'>Runtime error:" in runtimeOutput:
      category = "Runtime Error"
      errmsg = ssf(runtimeOutput[runtimeOutput.index("<div class='error'>Runtime error:"):], "<pre >", "\n")
    elif "<div class='all-passed'>" in runtimeOutput:
      category = "Passed"
      epilogue = websheet.epilogue
    else:
      category = "Failed Tests"
      if "<div class='error'>" in runtimeOutput:
        errmsg = ssf(runtimeOutput, "<div class='error'>", '</div>')
      else:
        return ("Internal Error", "<b>stderr</b><pre>" + runUser.stderr + "</pre><b>stdout</b><br>" + runUser.stdout)
        
    return (category, runtimeOutput)

  try:
    category, results = compile_and_run()
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

  if (not client_request["viewing_ref"]):
    # remove positional information
    user_snippets = [blank["code"] for blank in client_request["snippets"]]
    config.save_submission(student, classname, user_snippets, save_this, passed)

  return json.dumps(print_output)

if __name__ == "__main__":
  import sys

  stdin = json.loads(input()) # assume json all on one line
  student = stdin["php_data"]["user"]
  websheet_name = stdin["php_data"]["problem"]
  print(submit_and_log(websheet_name, student, stdin["client_request"], stdin["php_data"]["meta"]))
  sys.exit(0)

