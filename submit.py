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
import config, json, cgi, sys, Websheet, re, os

def submit_and_log(websheet_name, student, client_request, meta):

  config.meta = meta

  websheet = Websheet.Websheet.from_filesystem(websheet_name)

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

    #print(cgi.escape(student_solution[1]))
    #print(cgi.escape(reference_solution))

    if websheet.lang == "C++":
      student_solution = student_solution[1]
      if websheet.mode == "func":
        student_solution = re.sub(r"\bmain\b", "__student_main__", student_solution)

    if websheet.lang == "C++":
      import grade_cpp
      return grade_cpp.grade(reference_solution, student_solution, translate_line, websheet)
    elif websheet.lang == "Java":
      import grade_java
      return grade_java.grade(reference_solution, student_solution, translate_line, websheet)

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

