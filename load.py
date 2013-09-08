#!/usr/bin/python3

if __name__ == "__main__":
  import sys, Websheet
  student = sys.argv[2]
  classname = Websheet.Websheet.from_filesystem(sys.argv[1]).classname

  import config
  print(config.load_submission(student, classname))
