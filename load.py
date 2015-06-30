#!/usr/bin/python3

if __name__ == "__main__":
  import sys
  from Websheet import Websheet
  student = sys.argv[2]
  try:
    websheet = Websheet.from_name(sys.argv[1], sys.argv[3]=='True', student) # preview?
    dbslug = websheet.dbslug
    
    import config, json
    
    if not config.db_enabled: student="anonymous"
    #  websheet = Websheet.from_filesystem(classname)
    data = {"template_code":websheet.get_json_template(),
            "description":websheet.description,
            "user_code": config.load_submission(student, dbslug),
            "ever_passed": config.ever_passed(student, dbslug),
            "num_submissions": config.num_submissions(student, dbslug),
            "initial_snippets": websheet.get_initial_snippets(),
            "lang": websheet.lang
          }
    if websheet.nocode:
      data["nocode"] = websheet.get_nocode_question()
    else:
      data["nocode"] = False
    if data["ever_passed"] or websheet.attempts_until_ref == 0:
      data["reference_sol"] = websheet.get_reference_snippets()
    print(json.dumps(data, indent=4, separators=(',', ': '))) # pretty!
  except FileNotFoundError:
    print("No exercise named " + sys.argv[1])
