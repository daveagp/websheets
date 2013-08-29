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
                if stack == [r"\["]:
                    info["blank_index"] = input_counter
                    input_counter += 1

            if with_delimiters or item.type=="":
                yield (item, stack, info)      

    def make_student_solution(self, student_code):
        if self.input_count != len(student_code):
            return [False, "Internal error! Wrong number of inputs"]

        r = []

        for (item, stack, info) in self.iterate_token_list():
            if len(stack)==0:
                r.append(item.token)
            else:
                assert len(stack)==1
                if stack[0]==r"\[":
                    i = info["blank_index"]

                    if type(student_code[i]) == str:
                        chunk = student_code[i]
                        pos = None
                    else:
                        chunk = student_code[i]['code']
                        pos = student_code[i]
                        
                    valid = java_syntax.is_valid_substitute(
                        item.token, chunk)
                    if not valid[0]:
                        import re
                        match = re.search(re.compile(r"^Error at line (\d+), column (\d+):\n(.*)$"), valid[1])
                        if match is None:
                            user_pos = "end of region"
                            if pos is not None:
                                user_pos = "line "+str(pos['to']['line']+(1 if "\n" not in chunk else 0))
                            return [False, 
                                    "Error in input area "+str(i)+" ("+user_pos+"): "+valid[1]]
                        else:
                            user_pos = "chunk-line "+match.group(1)+", chunk-col "+match.group(2)
                            if pos is not None:
                                if match.group(1)=="0":
                                    user_pos = {"line": pos['from']['line'],
                                                "col": pos['from']['ch']+int(match.group(2))}
                                else:
                                    user_pos = {"line": pos['from']['line']+int(match.group(1)),
                                                "col": int(match.group(2))}
                                if "\n" in chunk: user_pos["line"] -= 1
                                user_pos = "line " + str(user_pos["line"]+1) + ", col " + str(user_pos["col"])
                            return [False, 
                                    "Error in input area "+str(i)+" ("+user_pos+"): "+match.group(3)]

                    r.append(chunk)
                elif stack[0]==r"\hide[":
                    r.append(item.token)
                elif stack[0]==r"\fake[":
                    pass
    
        return [True, ''.join(r)]

    def make_reference_solution(self, before_ref="", after_ref=""):
        r = []

        for (item, stack, info) in self.iterate_token_list():
            if len(stack)==0:
                r.append(item.token)
            else:
                assert len(stack)==1
                if stack[0] in {r"\[", r"\hide["}:
                    r.extend([before_ref, item.token, after_ref])
                else:
                    assert stack[0]== r"\fake["
        return ''.join(r)

    def get_json_chunks(self):
        r = [""]
        
        for (item, stack, info) in self.iterate_token_list():
            token = item.token
            if stack == [] or stack == [r"\fake["]:
                if token.startswith("\n"): token = token[1:]
                if token.endswith("\n"): token = token[:-1]
                if token != "": 
                    if len(r) % 2 == 0: r += [""]
                    r[-1] += token
            elif stack == [r"\["]:
                if len(r) % 2 == 1: r += [""]
                r[-1] += "\n\n" if "\n" in token else "  "
                
        return r

    @staticmethod
    def from_module(module):
        return Websheet(module.classname, module.code, 
                        module.tests, module.description)

if __name__ == "__main__":

    if sys.argv[1:] == ["json"]:
        import ws_MaxThree, ws_FourSwap, ws_NextYear

        websheets = [Websheet.from_module(m) 
                     for m in (ws_MaxThree, ws_FourSwap, ws_NextYear)]

        # test of json chunking
        for w in websheets:
            print(w.get_json_chunks())
        sys.exit(0)

    if sys.argv[1:] == ["interactive"]:
        import ws_MaxThree, ws_FourSwap, ws_NextYear

        websheets = [Websheet.from_module(m) 
                     for m in (ws_MaxThree, ws_FourSwap, ws_NextYear)]
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

    # call Websheet.py chunks ws_MaxThree and input [" int ", "  int a, int b, int c ", "..."] 
    if sys.argv[1] == "chunks":
        module = __import__(sys.argv[2])
        websheet = Websheet.from_module(module)
        user_input = input() # assume json all on one line
        import json
        user_chunks = json.loads(user_input)
        print(websheet.make_student_solution(user_chunks))

    if sys.argv[1] == "get_json_template":
        module = __import__(sys.argv[2])
        websheet = Websheet.from_module(module)
        import json
        print(json.dumps(websheet.get_json_chunks()))

    # call Websheet.py poschunks ws_MaxThree and input [{code: " int ", from: ..., to: ...}, ...]
    if sys.argv[1] == "poschunks":
        module = __import__(sys.argv[2])
        websheet = Websheet.from_module(module)
        user_input = input() # assume json all on one line
        import json
        user_poschunks = json.loads(user_input)
        print(json.dumps(websheet.make_student_solution(user_poschunks)))
        
