import cgi

def pre(s, specialBlank = False):
  if len(s) > 10000:
    s = s[:10000] + "\n... " + str(len(s)-10000) + " characters truncated"
  if (specialBlank and s==""):
    return "<pre><i>(no output)</i></pre>"
  return "<pre>\n" + cgi.escape(s) + "</pre>"

def tt(s):
  return "<code>" + cgi.escape(s) + "</code>"

