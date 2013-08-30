#!/usr/bin/python3

"""
Note: this is a relatively cheap and dirty solution that assumes
that the delimeters never occur in comments or quotes
in the source code. While this approach should be practical,
a more full solution could be done by extending java_parse.
"""

import re
import sys
from java_syntax import java_syntax

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
                # if token consists only of newlines, reduce length by 1
                if token.count("\n")==len(token): token = token[1:]

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

    def __init__(self, classname, source_code, tests, description, tester_preamble, show_class_decl):
        self.classname = classname
        self.source_code = source_code
        self.tests = tests
        self.description = description
        self.tester_preamble = tester_preamble
        self.show_class_decl = show_class_decl

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
                if stack == [r"\["]:
                    info["blank_index"] = input_counter
                    input_counter += 1
                # avoid extraneous space around user-facing read-only tokens
                if stack == [] or stack == [r"\fake["]:
                    if item.token=='\n\n':
                        item.token='\n'
                    else:
                        if item.token.startswith("\n"): item.token = item.token[1:]
                        if item.token.endswith("\n"): item.token = item.token[:-1]

            if with_delimiters or item.type=="":
                yield (item, stack, info)      

    def make_student_solution(self, student_code, package = None):
        if self.input_count != len(student_code):
            return [False, "Internal error! Wrong number of inputs"]

        r = []
        linemap = {}
        ui_lines = 1 # user interface lines
        ss_lines = 1 # student solution lines

        if self.show_class_decl: ui_lines += 1

        last_line_with_blank = -1
        blank_count_on_line = -1

        r.extend('\n' if package is None else 'package '+package+';\n')
        r.extend('public class '+self.classname+" {\n")
        ss_lines += 2

        for (item, stack, info) in self.iterate_token_list():
            if len(stack)==0:
                chunk = item.token

                r.append(chunk)
                # index java lines starting from 1
                generatedLine = 1 + sum(map(lambda st : st.count("\n"), r))

                if chunk != "" and chunk != "\n":
                    if chunk[:1] != "\n":
                        linemap[ss_lines] = ui_lines #+"D" + chunk +"D"
                    for i in range(0, item.token.count("\n")):
                        ui_lines += 1
                        ss_lines += 1
                        linemap[ss_lines] = ui_lines #+"D" + chunk +"D"

            else:
                assert len(stack)==1

                if stack==[r"\fake["]:
                    for i in range(0, item.token.count("\n")):
                        ui_lines += 1 
                
                if stack[0]==r"\[":
                    
                    i = info["blank_index"]

                    chunk = student_code[i]['code']
                    pos = student_code[i] # has 'from', 'to'

                    if ui_lines == last_line_with_blank and '\n' not in chunk:
                        blank_count_on_line += 1
                    else:
                        last_line_with_blank = ui_lines
                        blank_count_on_line = 1
                        
                    valid = java_syntax.is_valid_substitute(
                        item.token, chunk)

                    if not valid[0]:
                        import re
                        match = re.search(re.compile(r"^Error at line (\d+), column (\d+):\n(.*)$"), valid[1])
                        if match is None: # error at end of chunk
                            if "\n" in chunk:
                                user_pos = "Line "+str(pos['to']['line']-(1 if "\n" in chunk else 0))+" (at end of editable region)"
                            else:
                                user_pos = "Line "+str(pos['to']['line']-(1 if "\n" in chunk else 0))+", end of editable region " + str(blank_count_on_line)
                            return [False, user_pos + ": " + valid[1]]
                        else:
                            if match.group(1)=="0":
                                user_pos = {"line": pos['from']['line'],
                                            "col": pos['from']['ch']+int(match.group(2))}
                            else:
                                user_pos = {"line": pos['from']['line']+int(match.group(1)),
                                            "col": int(match.group(2))}
                                if "\n" not in chunk: user_pos["line"] += 1
                                user_pos = "Line " + str(user_pos["line"]+1) + ", col " + str(user_pos["col"])+" (blank " + str(blank_count_on_line) + ")"
                            return [False, 
                                    user_pos + ": " + match.group(3)]

                    # now add the user code to the combined solution
                    if pos != None:
                        # index java lines starting from 1
                        generatedLine = 1 + sum(map(lambda st : st.count("\n"), r))

                        if "\n" in chunk:
                            for i in range(1, chunk.count("\n")):
                                linemap[generatedLine+i] = pos['from']['line']+i

                        else:
                            # just a single line
                            linemap[generatedLine] = pos['from']['line']
                            
                    r.append(chunk)
                    ui_lines += chunk.count("\n")
                    ss_lines += chunk.count("\n")
                    
                elif stack[0]==r"\hide[":
                    r.append(item.token)
                    ss_lines += item.token.count("\n")
                elif stack[0]==r"\fake[":
                    pass

        r.extend("\n}")
        return [True, ''.join(r), linemap]

    def get_reference_solution(self, package = None, before_ref="", after_ref=""):
        r = []

        r.extend('\n' if package is None else 'package '+package+';\n')
        r.extend('public class '+self.classname+" {\n")

        for (item, stack, info) in self.iterate_token_list():
            if len(stack)==0:
                r.append(item.token)
            else:
                assert len(stack)==1
                if stack[0] in {r"\[", r"\hide["}:
                    r.extend([before_ref, item.token, after_ref])
                else:
                    assert stack[0]== r"\fake["

        r.extend("\n}")
        
        return ''.join(r)

    def get_json_template(self):
        r = [""]

        if self.show_class_decl:
            r[0] = "public class "+self.classname+" {\n";
        
        for (item, stack, info) in self.iterate_token_list():
            token = item.token
            if stack == [] or stack == [r"\fake["]:
                if token != "": 
                    if len(r) % 2 == 0: r += [""]
                    r[-1] += token
            elif stack == [r"\["]:
                if len(r) % 2 == 1: r += [""]
                r[-1] += "\n\n" if "\n" in token else "  "

        if self.show_class_decl:
            for i in range(len(r)):
                if i % 2 == 0: r[i] = r[i].replace("\n", "\n   ")
                if i % 2 == 1 and r[i][-1] == "\n": r[i+1] = "   "+r[i+1]
            if len(r) % 2 == 0: r.extend("")
            r[-1] += "\n}"

        return r

    @staticmethod
    def from_module(module):
        return Websheet(module.classname, module.code, 
                        module.tests, module.description,
                        module.tester_preamble if "tester_preamble" in dir(module) else None,
                        module.show_class_decl if "show_class_decl" in dir(module) else False)

if __name__ == "__main__":

    if sys.argv[1:] == ["json"]:
        import ws_MaxThree, ws_FourSwap, ws_NextYear

        websheets = [Websheet.from_module(m) 
                     for m in (ws_MaxThree, ws_FourSwap, ws_NextYear)]

        # test of json chunking
        for w in websheets:
            print(w.get_json_template())
        sys.exit(0)

    if sys.argv[1:] == ["interactive"]:
        import ws_MaxThree, ws_FourSwap, ws_NextYear

        websheets = [Websheet.from_module(m) 
                     for m in (ws_MaxThree, ws_FourSwap, ws_NextYear)]
        while True:  
            print("#reference for "+w.classname+"#")
            print(w.get_reference_solution(before_ref = "<r>", after_ref = "</r>"))
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

    # call Websheet.py get_reference_solution ws_MaxThree
    if sys.argv[1] == "get_reference_solution":
        module = __import__(sys.argv[2])
        websheet = Websheet.from_module(module)
        import json
        print(json.dumps(websheet.get_reference_solution("Ref_Sols")))
        sys.exit(0)

    # call Websheet.py get_json_template ws_MaxThree
    if sys.argv[1] == "get_json_template":
        module = __import__(sys.argv[2])
        websheet = Websheet.from_module(module)
        import json
        print(json.dumps(websheet.get_json_template()))
        sys.exit(0)

    # call Websheet.py get_html_template ws_MaxThree
    if sys.argv[1] == "get_html_template":
        module = __import__(sys.argv[2])
        websheet = Websheet.from_module(module)
        import json
        print(json.dumps({"code":websheet.get_json_template(),"description":websheet.description}))
        sys.exit(0)

    # call Websheet.py make_student_solution ws_MaxThree stu and input [{code: " int ", from: ..., to: ...}, ...]
    if sys.argv[1] == "make_student_solution":
        module = __import__(sys.argv[2])
        websheet = Websheet.from_module(module)
        user_input = input() # assume json all on one line
        import json
        user_poschunks = json.loads(user_input)
        print(json.dumps(websheet.make_student_solution(user_poschunks, "student."+sys.argv[3] if len(sys.argv) > 3 else None)))
        sys.exit(0)

    print("Invalid command for Websheet module")
    sys.exit(1)
