#!/usr/bin/python3

"""
Note: this is a relatively cheap and dirty solution that assumes
that the delimeters never occur in comments or quotes
in the source code. While this approach should be practical,
a more full solution could be done by extending java_parse.
"""

import re
import sys
sys.path.append('../../java-syntax')
import java_syntax

def record(**dict):
    """ e.g. foo = record(bar='baz', jim=5) creates an object foo
    such that foo.bar == 'baz', foo.jim == 5 """
    return type('', (), dict)

open_delim = {r'\[', r'\hide[', r'\fake['}
close_delim = {']\\'} # not rawstring to make emacs happy
    
def parse_websheet_source(source):
    # allowing source to start with a newline makes the source files prettier
    if (source[:1]=="\n"):
        source = source[1:]

    result = []
    pos = 0
    n = len(source)

    regex = '|'.join(re.escape(delim) for delim in 
                     (open_delim | close_delim)) # set union

    depth = 0
    
    for token in re.split('('+regex+')', source):
        if token in open_delim:
            depth += 1
            type = "open"
        elif token in close_delim:
            depth -= 1
            type = "close"
        else:
            type = ""
            
        result.append(record(depth=depth, token=token, type=type))
        
        if depth < 0:
            return [False, 'Error in websheet source code: too many closing delimiters']
        if depth > 1:
            return [False, 'Error in websheet source code: nesting not currently allowed']
    if depth != 0:
        return [False, 'Error in websheet source code: not enough closing delimiters']

    return [True, result]

def prepare_websheet(ws):
    parsed = parse_websheet_source(ws.code)
    if not parsed[0]:
        return parsed
    input_count = 0
    for token in parsed[1]:
        if token.type == "open" and token.token == r"\[":
            input_count += 1
    return [True, record(source_code = ws.code,
                         token_list = parsed[1],
                         input_count = input_count,
                         classname = ws.classname,
                         description = ws.description,
                         tests = ws.tests)]

def make_html_exercise(pws):
    result = ""
    result += '<h3>' + pws.classname + '</h3>\n'
    result += '<div class="exercise">\n'
    result += '<div class="section preamble">\n' + pws.description + "\n</div>\n"
    result += '<div class="section code">'
    stack = []
    r = []
    input_count = 0
    for item in pws.token_list:
        if item.type=="open":
            stack.append(item.token)
        elif item.type=="close":
            stack.pop()
        else:
            assert item.type==""
            if len(stack)==0:
                r.append(item.token)
            else:
                assert len(stack)==1
                if stack[0]=="\\[":
                    if "\n" in item.token:
                        rows = 1 + item.token.count('\n')
                        r.append("<textarea cols=60 rows={} name='wsi{}'></textarea>".
                                 format(rows, input_count))
                        input_count += 1
                    else:
                        cols = 3 + len(item.token)
                        r.append('<input class="oneliner" type="text" size="{}" name="wsi{}"/>'.
                                 format(cols, input_count))
                        input_count += 1
                elif stack[0]=="\\fake[":
                    r.append(item.token)
                elif stack[0]=="\\hide[":
                    pass

    result += ''.join(r)

    result += '</div> <!--code-->\n'
    result += '<div class="section">'
    result += '<table class="actions"><tr><td><input type="button" value="Submit" class="exercise-submit"></td></tr></table>\n'
    result += '<div class="results"></div>\n'
    result += '</div> <!--tail section-->\n'
    result += '</div> <!--exercise-->\n'
    return result

def is_valid_substitute(reference_code, student_code):
    is_inline = not ("\n" in reference_code)

    stuparse = java_syntax.java_parse(student_code)
    if not stuparse.valid:
        return [False, stuparse.errmsg]
    if stuparse.ends_with_scomment and is_inline:
        return [False, "// is not allowed"]
    refparse = java_syntax.java_parse(reference_code)
    if refparse.oneline or refparse.oneline_with_semicolon:
        if "\n" in student_code:
            return [False, "newlines are not allowed"]
    if refparse.oneline and stuparse.semicolons > 0:
        return [False, "; is not allowed"]
    if refparse.oneline_with_semicolon and not stuparse.oneline_with_semicolon:
            return [False, "must have exactly one semicolon, at the end"]
    if stuparse.empty and not refparse.empty:
        return [False, "must not be empty"]
    if stuparse.terminated_badly and not refparse.terminated_badly:
        return [False, "must end with a semicolon (;) or a {block}"]
    return [True]

def make_student_solution(pws, student_code):
    stack = []
    r = []
    input_count = 0
    if pws.input_count != len(student_code):
        return [False, "Wrong number of inputs"]
    for item in pws.token_list:
        if item.type=="open":
            stack.append(item.token)
        elif item.type=="close":
            stack.pop()
        else:
            assert item.type==""
            if len(stack)==0:
                r.append(item.token)
            else:
                assert len(stack)==1
                if stack[0]=="\\[":
                    valid = is_valid_substitute(item.token, student_code[input_count])
                    if not valid[0]:
                        return [False, 
                                "Error in input area "+str(input_count)+": "+
                                valid[1]]
                    r.append(student_code[input_count])
                    input_count += 1
                elif stack[0]=="\\hide[":
                    r.append(item.token)
                elif stack[0]=="\\fake[":
                    pass
    return [True, ''.join(r)]

def make_reference_solution(pws, before_ref="", after_ref=""):
    stack = []
    r = []
    for item in pws.token_list:
        if item.type=="open":
            stack.append(item.token)
        elif item.type=="close":
            stack.pop()
        else:
            assert item.type==""
            if len(stack)==0:
                r.append(item.token)
            else:
                assert len(stack)==1
                if stack[0] in {"\\[", "\\hide["}:
                    r.extend([before_ref, item.token, after_ref])
                else:
                    assert stack[0]=="\\fake["
    return ''.join(r)

def make_page(pwses):
    result = r"""
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Testing Multiple Text Areas</title>
        <link rel="stylesheet" href="codemirror/lib/codemirror.css">
        <link rel="stylesheet" href="codemirror/theme/neat.css">
        <link rel="stylesheet" href="style.css">
        <script type="text/javascript" 
         src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
        <!-- next one for one-line text inputs -->
        <script type="text/javascript" src="autoGrowInput.js"></script>
        <script type="text/javascript" 
         src="codemirror/lib/codemirror.js"></script>
        <script type="text/javascript" 
         src="codemirror/mode/clike/clike.js"></script>
        <script type="text/javascript" src="interface.js"></script>
   </head>
   <body>
"""
    for pws in pwses:
       result += make_html_exercise(pws)
    result += "</body></html>"
    return result

if __name__ == "__main__":
    # testing
    import ws_MaxThree, ws_FourSwap, ws_NextYear
    all_ws = (ws_MaxThree, ws_FourSwap, ws_NextYear)
    all_pws = []
    for ws in all_ws:
        pws = prepare_websheet(ws)
        if not pws[0]:
            print("Error in preparing websheet!")
            print(pws[1])
            print("Websheet input:")
            print(ws)
            sys.exit(0)
        all_pws.append(pws[1])

    if len(sys.argv) > 1:
        for pws in all_pws:
          while True:  
            print("#reference for "+pws.classname+"#")
            print(make_reference_solution(pws, "<r>", "</r>"))
            stulist = []
            for i in range(pws.input_count):
                r = ""
                while True:
                    inp = input("Enter more for input #"+str(i)+" (blank to stop): ")
                    if inp != "":
                        if r != "": r += "\n"
                        r += inp
                    else:
                        break
                if i==0 and r =="": break
                stulist.append(r)
            if stulist==[]: break
            print("#student sample for "+pws.classname+"#")
            ss = make_student_solution(pws, stulist)
            if ss[0]:
                print("Accepted:\n"+ss[1])
            else:
                print("Error:", ss[1])
    else:
        print(make_page(all_pws))

    
