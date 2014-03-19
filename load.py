#!/usr/bin/python3

if __name__ == "__main__":
  import sys
  from Websheet import Websheet
  student = sys.argv[2]
  websheet = Websheet.from_filesystem(sys.argv[1])
  classname = websheet.classname

  import config, json
#  websheet = Websheet.from_filesystem(classname)
  print(json.dumps({"template_code":websheet.get_json_template(),
                    "description":websheet.description,
                    "user_code": config.load_submission(student, classname),
                    "ever_passed": config.ever_passed(student, classname),
                    "num_submissions": config.num_submissions(student, classname),
                    "reference_sol": websheet.get_reference_snippets(),
                    "initial_snippets": websheet.get_initial_snippets()
                    }))
