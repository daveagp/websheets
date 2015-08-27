import config, json, cgi, sys, Websheet, re, os

def grade(reference_solution, student_solution, translate_line, websheet, student):

    if not re.match(r"^\w+$", websheet.classname):
      return ("Internal Error (Compiling)", "Invalid overridden classname <tt>" + websheet.classname + " </tt>")
    
    dump = {
        "reference." + websheet.classname : reference_solution,
        "student." + websheet.classname : student_solution[1],
        "tester." + websheet.classname : websheet.make_tester()    
        }

#    print(student_solution[1])
#    print(reference_solution)
#    print(websheet.make_tester())
    
    for clazz in ["Grader", "Options", "Utils"]:
      dump["websheets."+clazz] = "".join(open("grade_java_files/"+clazz+".java"))

    for dep in websheet.dependencies:
      depws = Websheet.Websheet.from_name(dep)
      if depws == None:
          return ("Internal Error", "Dependent websheet " + dep + " does not exist");
      submission = config.load_submission(student, dep, True)
      if submission == False:
        return("Dependency Error",
               "<div class='dependency-error'><i>Dependency error</i>: " + 
               "You need to successfully complete the <a href='javascript:websheets.load(\""+dep+"\")'><tt>"+dep+"</tt></a> websheet first (while logged in).</div>") # error text
      submission = [{'code': x, 'from': {'line': 0, 'ch':0}, 'to': {'line': 0, 'ch': 0}} for x in submission]
      dump["student."+dep] = depws.combine_with_template(submission, "student")[1]
      
      dump["reference."+dep] = depws.get_reference_solution("reference")


    compileRun = config.run_java(["traceprinter/ramtools/CompileToBytes"], json.dumps(dump))
    compileResult = compileRun.stdout
    if (compileResult==""):
      return ("Internal Error (Compiling)", "<pre>\n" + 
              cgi.escape(compileRun.stderr) +
              "</pre>"+"<!--"+compileRun._toString()+"-->")
    
    compileObj = json.loads(compileResult)

#    print(compileObj['status'])

    if compileObj['status'] == 'Internal Error':
      return ("Internal Error (Compiling)", "<pre>\n" + 
              cgi.escape(compileObj["errmsg"]) +
              "</pre>")
    elif compileObj['status'] == 'Compile-time Error':
        errorObj = compileObj['error']
        if errorObj['filename'] == ("student." + websheet.classname + ".java"):
            result = "Syntax error (could not compile):"
            result += "<br>"
            result += '<tt>'+errorObj['filename'].split('.')[-2]+'.java</tt>, line '
            result += str(translate_line(errorObj['row'])) + ':'
            #result += str(errorObj['row']) + ':'
            result += "<pre>\n"
            #remove the safeexec bits
            result += cgi.escape(errorObj["errmsg"]
                                 .replace("stdlibpack.", "")
                                 .replace("student.", "")
                                 )
            result += "</pre>"
            return ("Syntax Error", result)
        else:
            return("Internal Error (Compiling reference solution and testing suite)",
                   '<b>File: </b><tt>'+errorObj['filename']+'</tt><br><b>Line number: '
                   +str(errorObj['row'])+"</b><pre>"
                   +errorObj['errmsg']+":\n"+dump[errorObj['filename'][:-5]].split("\n")[errorObj['row']-1]+"</pre>")
                    

    #print(compileResult)

    # prefetch all urls, pass them to the grader on stdin
    compileObj["stdin"] = json.dumps({
      "fetched_urls":websheet.prefetch_urls(True)
      })

    compileResult = json.dumps(compileObj)
    
    runUser = config.run_java(["traceprinter/ramtools/RAMRun", "tester." + websheet.classname], compileResult)
    #runUser = config.run_java("tester." + websheet.classname + " " + student)

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
        re.compile("(at|from) line (\d+) "),
        lambda match: match.group(1)+" line " + translate_line(match.group(2)) + " ",
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
