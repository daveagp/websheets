#!/usr/bin/python3

"""
Note: this is a cheap and dirty solution that assumes
that the delimeters never occur in comments or quotes
in the source code. While this approach should not be practical,
a more full solution could be done by extending java_parse.
"""

import re

def record(**dict):
    """ e.g. foo = record(bar='baz', jim=5) creates an object foo
    such that foo.bar == 'baz', foo.jim == 5 """
    return type('', (), dict)

open_delim = {r'\[', r'\hide[', r'\fake['}
close_delim = {']\\'} # not rawstring to make emacs happy
    
def parse(source):
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
            return 'Error: too many closing delimiters'
        if depth > 1:
            return 'Error: nesting not currently allowed'
    if depth != 0:
        return 'Error: not enough closing delimiters'

    return result

def make_html_exercise(ws):
    result = ""
    result += '<h3>' + ws.classname + '</h3>\n'
    result += '<div class="exercise">\n'
    result += '<div class="section preamble">\n' + ws.description + "\n</div>\n"
    result += '<div class="section code">'
    stack = []
    r = []
    input_count = 0
    for item in parse(ws.code):
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


def make_student_solution(ws, student_code):
    stack = []
    r = []
    input_count = 0
    for item in parse(ws.code):
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
                    r.append(student_code[input_count])
                    input_count += 1
                elif stack[0]=="\\hide[":
                    r.append(item.token)
                elif stack[0]=="\\fake[":
                    pass

    return ''.join(r)

def make_reference_solution(ws):
    stack = []
    r = []
    for item in parse(ws.code):
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
                    r.append(item.token)
                else:
                    assert stack[0]=="\\fake["
    return ''.join(r)

def make_page(wses):
    result = r"""
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Testing Multiple Text Areas</title>
        <link rel="stylesheet" href="codemirror-3.0/lib/codemirror.css">
        <link rel="stylesheet" href="codemirror-3.0/theme/neat.css">
        <link rel="stylesheet" href="style.css">
        <script type="text/javascript" 
         src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
        <!-- next one for one-line text inputs -->
        <script type="text/javascript" src="autoGrowInput.js"></script>
        <script type="text/javascript" 
         src="codemirror-3.0/lib/codemirror.js"></script>
        <script type="text/javascript" 
         src="codemirror-3.0/mode/clike/clike.js"></script>
        <script type="text/javascript" src="interface.js"></script>
   </head>
   <body>
"""
    for ws in wses:
       result += make_html_exercise(ws)
    result += "</body></html>"
    return result

if __name__ == "__main__":
    # testing
    import ws_MaxThree, ws_FourSwap, ws_NextYear
    all_ws = (ws_MaxThree, ws_FourSwap, ws_NextYear)
    import sys
    if len(sys.argv)>1:
        for ws in all_ws:
            print("#reference for "+ws.classname+"#")
            print(make_reference_solution(ws))
            print("#student sample for "+ws.classname+"#")
            print(make_student_solution(ws, ("000", "111", "222", "333")))
    else:
        print(make_page(all_ws))

    
