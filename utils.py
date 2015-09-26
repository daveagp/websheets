import cgi

def pre(s, specialBlank = False):
  if len(s) > 10000:
    s = s[:10000] + "\n... " + str(len(s)-10000) + " characters truncated"
  if (specialBlank and s==""):
    return "<pre><i>(no output)</i></pre>"
  return "<pre>\n" + cgi.escape(s) + "</pre>"

def tt(s):
  return "<code>" + cgi.escape(s) + "</code>"

def badchar(ch):
  x = ord(ch)
  return x<32 and x not in [10, 13] or x == 127 or x >= 0x2018 and x < 0x2020

def expose_badchars(str):
  for i in reversed(range(len(str))):
    if badchar(str[i]):
      # write all as 4 digits, since none of the typical issues are >16 bits in unicode
      tmp = hex(65536 + ord(str[i]))
      str = str[:i] + "\\u"+tmp[3:] + str[i+1:] # 3: is 0x1
  return str
