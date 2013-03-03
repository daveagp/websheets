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

class Websheet:

    open_delim = {r'\[', r'\hide[', r'\fake['}
    close_delim = {']\\'} # not rawstring to make emacs happy

    @staticmethod
    def parse_websheet_source(source):
        # allowing source to start with a newline 
        # makes the source files prettier
        if (source[:1]=="\n"):
            source = source[1:]

        result = []
        pos = 0
        n = len(source)
        
        regex = '|'.join(re.escape(delim) for delim in 
                         (Websheet.open_delim | 
                          Websheet.close_delim)) # set union
        
        depth = 0
        
        for token in re.split('('+regex+')', source):
            if token in Websheet.open_delim:
                depth += 1
                type = "open"
            elif token in Websheet.close_delim:
                depth -= 1
                type = "close"
            else:
                type = ""

            result.append(record(depth=depth, token=token, type=type))
        
            if depth < 0:
                return [False, 
                        'Error in websheet source code:'+
                        ' too many closing delimiters']
            if depth > 1:
                return [False, 'Error in websheet source code:'+
                        ' nesting not currently allowed']
        if depth != 0:
            return [False, 'Error in websheet source code:'+
                    ' not enough closing delimiters']

        return [True, result]

    def __init__(self, classname, source_code, tests, description):
        self.classname = classname
        self.source_code = source_code
        self.tests = tests
        self.description = description

        parsed = Websheet.parse_websheet_source(source_code)

        if not parsed[0]:
            raise Exception("Could not parse websheet source code: " 
                            + parsed[1])

        self.input_count = 0
        for token in parsed[1]:
            if token.type == "open" and token.token == r"\[":
                self.input_count += 1
                
        self.token_list = parsed[1]

    def iterate_token_list(self, with_delimiters = False):
        stack = []
        input_counter = 0
        for item in self.token_list:
            info = {}
            if item.type=="open":
                stack.append(item.token)
            elif item.type=="close":
                stack.pop()
            else:
                assert item.type==""
                if stack == ["\\["]:
                    info["blank_index"] = input_counter
                    input_counter += 1

            if with_delimiters or item.type=="":
                yield (item, stack, info)      

    def make_html_exercise(self):
        r = []
        r.append('<h3>' + self.classname + '</h3>\n')
        r.append('<div class="exercise">\n')
        r.append('<div class="section preamble">\n' 
                 + self.description 
                 + "\n</div>\n")
        r.append('<div class="section code">')
        
        for (item, stack, info) in self.iterate_token_list():
            if len(stack)==0:
                r.append(item.token)
            else:
                assert len(stack)==1
                if stack[0]=="\\[":
                    if "\n" in item.token:
                        rows = 1 + item.token.count('\n')
                        r.append(("<textarea cols=60 rows={} name='wsi{}'>"+
                                 "</textarea>").
                                 format(rows, info["blank_index"]))
                    else:
                        cols = 3 + len(item.token)
                        r.append(('<input class="oneliner" type="text"'+
                                  ' size="{}" name="wsi{}"/>').
                                 format(cols, info["blank_index"]))
                elif stack[0]=="\\fake[":
                    r.append(item.token)
                elif stack[0]=="\\hide[":
                    pass

        r.append("""</div> <!--code-->
<div class="section">
<table class="actions"><tr><td>
<input type="button" value="Submit" class="exercise-submit">
</td></tr></table>
<div class="results"></div>
</div> <!--tail section-->
</div> <!--exercise-->""")

        return ''.join(r)

    def make_student_solution(self, student_code):
        if self.input_count != len(student_code):
            return [False, "Wrong number of inputs"]

        r = []

        for (item, stack, info) in self.iterate_token_list():
            if len(stack)==0:
                r.append(item.token)
            else:
                assert len(stack)==1
                if stack[0]=="\\[":
                    i = info["blank_index"]
                    valid = java_syntax.is_valid_substitute(
                        item.token, student_code[i])
                    if not valid[0]:
                        return [False, 
                                "Error in input area "+str(i)+": "+
                                valid[1]]
                    r.append(student_code[i])
                elif stack[0]=="\\hide[":
                    r.append(item.token)
                elif stack[0]=="\\fake[":
                    pass
    
        return [True, ''.join(r)]

    def make_reference_solution(self, before_ref="", after_ref=""):
        r = []

        for (item, stack, info) in self.iterate_token_list():
            if len(stack)==0:
                r.append(item.token)
            else:
                assert len(stack)==1
                if stack[0] in {"\\[", "\\hide["}:
                    r.extend([before_ref, item.token, after_ref])
                else:
                    assert stack[0]=="\\fake["
        return ''.join(r)

    @staticmethod
    def make_page(websheets):
        r = []
        r.append(r"""
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Testing Multiple Text Areas</title>
        <link rel="stylesheet" href="codemirror/lib/codemirror.css">
        <link rel="stylesheet" href="codemirror/theme/neat.css">
        <link rel="stylesheet" href="style.css">
        <script type="text/javascript" 
         src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js">
        </script>
        <!-- next one for one-line text inputs -->
        <script type="text/javascript" src="autoGrowInput.js"></script>
        <script type="text/javascript" 
         src="codemirror/lib/codemirror.js"></script>
        <script type="text/javascript" 
         src="codemirror/mode/clike/clike.js"></script>
        <script type="text/javascript" src="interface.js"></script>
   </head>
   <body>
""")
        for websheet in websheets:
            r.append(websheet.make_html_exercise())
        r.append("</body></html>")
        return ''.join(r)

    @staticmethod
    def from_module(module):
        return Websheet(module.classname, module.code, 
                        module.tests, module.description)

if __name__ == "__main__":
    # testing
    import ws_MaxThree, ws_FourSwap, ws_NextYear

    websheets = [Websheet.from_module(m) 
                 for m in (ws_MaxThree, ws_FourSwap, ws_NextYear)]

    if len(sys.argv) == 1:
        print(Websheet.make_page(websheets))
    else:
        for w in websheets:
          while True:  
            print("#reference for "+w.classname+"#")
            print(w.make_reference_solution("<r>", "</r>"))
            stulist = []
            for i in range(w.input_count):
                r = ""
                while True:
                    inp = input("Enter more for input #"+str(i)
                                +" (blank to stop): ")
                    if inp != "":
                        if r != "": r += "\n"
                        r += inp
                    else:
                        break
                if i==0 and r =="": break
                stulist.append(r)
            if stulist==[]: break
            print("#student sample for "+w.classname+"#")
            ss = w.make_student_solution(stulist)
            if ss[0]:
                print("Accepted:\n"+ss[1])
            else:
                print("Error:", ss[1])

    
