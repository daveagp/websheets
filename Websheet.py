#!/usr/bin/python3

"""
Note: this is a relatively cheap and dirty solution that assumes
that the delimiters never occur in comments or quotes
in the source code. While this approach should be practical,
a more full solution could be done by extending java_parse.
"""

import re
import sys
import os
import exercises
import json
from java_syntax import java_syntax

def record(**dict):
    """ e.g. foo = record(bar='baz', jim=5) creates an object foo
    such that foo.bar == 'baz', foo.jim == 5 """
    return type('', (), dict)

ChunkType = record(plain=1, blank=2, fake=3, hide=4)

class Chunk:
    def __init__(self, text, type, attr=None):
        self.text = text
        self.type = type
        if attr is None: attr={}
        self.attr = attr 
    def __repr__(self):
        return repr([self.text, self.type, self.attr])

class Websheet:

    @staticmethod
    def sized_blank(token):
        return "\n"*max(2, token.count("\n")) if "\n" in token else " "*max(2, len(token))

    """
    Websheet source is converted internally into a list of chunks.
    Each chunk has
    type: plain, blank, fake, or hide
    text: string. starts and ends with space if inline, \n if multiline
                  except for plain type, first and last character must be same
    attr: dict of additional properties (like "show" for blank)
    """

    @staticmethod
    def chunkify(source):

        # normalize so starts, ends with newline if not already present
        if (source[:1]!="\n"):
            source = "\n"+source
        if (source[-1:]!="\n"):
            source = source+"\n"

        open_delim = {r'\[', r'\hide[', r'\fake['}
        close_delim = {']\\'} # rawstring can't end in \
        delim = open_delim | close_delim

        typemap = {r"\[":ChunkType.blank,
                   r"\hide[":ChunkType.hide,
                   r"\fake[":ChunkType.fake}

        # normalize by collapsing whitespace around syntactically correct
        # delimiters for multi-line regions
        for d in delim | {r"\show:"}:
            source = re.sub("\n[ \t]*"+re.escape(d)+"[ \t]*\n",
                            "\n"+d.replace("\\", "\\\\")+"\n",
                            source)

        delim_expr = '|'.join(re.escape(d) for d in delim)

        delim_iter = re.finditer(delim_expr, source)

        last_close_end = 0
        result = []
        
        while True:
            match = next(delim_iter, None)
            if match is None: break
            if match.group(0) in close_delim:
                return [False, "Found closing delimiter \\] not matching"+
                        " any earlier opening delimiter"]
            close = next(delim_iter, None)
            if close is None:
                return [False, "Found opening delimiter "+match.group(0)+
                        " without a matching close delimiter \\]"]
            if close.group(0) not in close_delim:
                return [False, "Found opening delimiter "+match.group(0)+
                        " followed by another opening delimiter "+close.group(0)]

            contained = source[match.end():close.start()]
            interstitial = source[last_close_end:match.start()]

            if "\n" in contained:
                if (source[match.start()-1] != "\n"
                    or source[match.end()] != "\n"):
                    return [False, "Improper multi-line-start delimiter " +
                            source[source.rindex("\n", 0, match.start()):
                                   source.index("\n", match.end())]]
                if (source[close.start()-1] != "\n"
                    or source[close.end()] != "\n"):
                    return [False, "Improper multi-line-end delimiter " +
                            source[source.rindex("\n", 0, close.start()):
                                   source.index("\n", close.end())]]
                if interstitial != "\n":
                    result.append(Chunk(interstitial, ChunkType.plain))
                    
                chunk = Chunk(contained, typemap[match.group(0)])

                p = contained.find("\n\\show:\n")
                if p != -1:
                    chunk.text = contained[:p+1] # include \n
                    chunk.attr["show"] = contained[p+7:] # include \n
                result.append(chunk)
            else:
                if interstitial != "":
                    result.append(Chunk(interstitial, ChunkType.plain))
                    
                chunk = Chunk(contained, typemap[match.group(0)])

                p = contained.find("\\show:")
                if p != -1:
                    chunk.text = contained[:p] 
                    chunk.attr["show"] = contained[p+6:]
                result.append(chunk)
            last_close_end = close.end()

        interstitial = source[last_close_end:]
        if interstitial != "\n":
            result.append(Chunk(interstitial, ChunkType.plain))

        return [True, result]

    def __init__(self, field_dict):

        mandatory_fields = ["classname", "source_code", "tests", "description"]

        # optional fields AND default values
        optional_fields = {"tester_preamble": None, "add_class_decl": True,
                           "epilogue": None, "dependencies": [], "imports": []}

        if re.match("^\n*public class") is not None:
            optional_fields["add_class_decl"] = False
        
        for field in mandatory_fields:
            setattr(self, field, field_dict[field])

        for field in optional_fields:
            setattr(self, field, field_dict[field] if field in field_dict else optional_fields[field])

        if self.add_class_decl:
            self.source_code.replace("\n", "\n   ")
            self.source_code = ("public class " + self.classname + "{\n" +
                                self.source_code+"}")

        chunks = Websheet.chunkify(self.source_code)

        if not chunks[0]:
            raise Exception("Could not parse websheet source code: " 
                            + chunks[1])

        self.chunks = chunks[1]

        self.input_count = 0
        for chunk in self.chunks:
            if chunk.type == ChunkType.blank:
                self.input_count += 1                

    def make_student_solution(self, student_code, package = None):
        if self.input_count != len(student_code):
            return [False, "Internal error! Wrong number of inputs"]

        r = []
        linemap = {}
        ui_lines = 1 # user interface lines
        ss_lines = 1 # student solution lines

        last_line_with_blank = -1
        blank_count_on_line = -1

        r.extend('\n' if package is None else 'package '+package+';\n')
        r.extend('import stdlibpack.*;\n')
        
        for i in self.imports:
            r.extend('import '+i+'\n')
            ss_lines += 1
            ui_lines += 1

        r.extend('public class '+self.classname+" {\n")
        ss_lines += 3

        for (item, stack, info) in self.iterate_token_list():
            if len(stack)==0:
                chunk = item.token

                r.append(chunk)
                # index java lines starting from 1
                generatedLine = 1 + sum(map(lambda st : st.count("\n"), r))

                if chunk != "" and chunk != "\n":
                    if chunk[:1] != "\n":
                        linemap[ss_lines] = ui_lines 
                    for i in range(0, item.token.count("\n")):
                        ui_lines += 1
                        ss_lines += 1
                        linemap[ss_lines] = ui_lines 

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
                        match = re.search(re.compile(r"^Error at line (\d+), column (\d+):\n(.*)$"), valid[1])
                        if match is None: # error at end of chunk
                            if "\n" in chunk:
                                user_pos = "Line "+str(pos['to']['line']-(1 if "\n" in chunk else 0))+", in editable region"
                            else:
                                user_pos = "Line "+str(pos['to']['line']-(1 if "\n" in chunk else 0))+", editable region " + str(blank_count_on_line)
                            return [False, user_pos + ":\n" + valid[1]]
                        else:
                            if match.group(1)=="0":
                                user_pos = {"line": pos['from']['line'],
                                            "col": pos['from']['ch']+int(match.group(2))}
                            else:
                                user_pos = {"line": pos['from']['line']+int(match.group(1)),
                                            "col": int(match.group(2))}
                                if "\n" not in chunk: user_pos["line"] += 1
                            user_pos = "Line " + str(user_pos["line"]+1) + ", col " + str(user_pos["col"])+" (blank " + str(blank_count_on_line) + ")\n"
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
                    ui_lines += max(0, chunk.count("\n")-2) # probably not always accurate!
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
        r.extend('import stdlibpack.*;\n')
        for i in self.imports:
            r.extend('import '+i+'\n')

        r.extend('public class '+self.classname+" {\n")

        for (item, stack, info) in self.iterate_token_list():
            if len(stack)==0:
                r.append(item.token)
            else:
                assert len(stack)==1
                if stack[0] in {r"\[", r"\hide["}:
                    r.extend([before_ref, item.token, after_ref])
                else:
                    assert stack[0] == r"\fake[" or stack[0] == r"\default["

        r.extend("\n}")
        
        return ''.join(r)

    def get_reference_snippets(self):
        r = []
        for (item, stack, info) in self.iterate_token_list():
            if stack == [r"\["]:
                if "\n" in item.token: 
                    r.append(item.token)
                else:
                    r.append(item.token)

        return r
        
    def get_initial_snippets(self):
        r = []
        for (item, stack, info) in self.iterate_token_list():
            if stack == [r"\["]:
                r.append(Websheet.sized_blank(item.token))
            if stack == [r"\default["]:
                r[-1] = item.token
        return r
        
    def get_json_template(self):
        r = [""]

        for (item, stack, info) in self.iterate_token_list():
            token = item.token
            if stack == [] or stack == [r"\fake["]:
                if token != "": 
                    if len(r) % 2 == 0: r += [""]
                    r[-1] += token
            elif stack == [r"\["]:
                if len(r) % 2 == 1: r += [""]
                r[-1] += Websheet.sized_blank(token)

        for i in self.imports:
            r[0] = 'import '+i+'\n' + r[0]

        # second pass : trim excess newlines from fixed text adjacent to multi-line blanks
        for i in range(0, len(r), 2):
            if r[i].startswith("\n") and (i==0 or "\n" in r[i-1]):
                r[i] = r[i][1:]
            if r[i].endswith("\n") and (i==len(r)-1 or "\n" in r[i+1]):
                r[i] = r[i][:-1]

        return r

    def make_tester(self):        
        return (
"package tester;\n" +
"import java.util.Random;\n" +
"import static framework.GenericTester.*;\n" +
"public class " + self.classname + " extends framework.GenericTester {\n" +
"{className=\"" + self.classname + "\";}" +
"protected void runTests() {" +
self.tests +
"\n}" +
("" if self.tester_preamble is None else self.tester_preamble) +
" public static void main(String[] args) {" +
self.classname + " to = new " + self.classname + "();\n" + 
"to.genericMain(args);\n" + 
"}\n}"
)


    @staticmethod
    def from_module(module):
        # convert module to a dict
        dicted = {attname: getattr(module, attname) for attname in dir(module)}
        if "classname" not in dicted:
            dicted["classname"] = module.__name__.split(".")[-1]
        return Websheet(dicted)

    @staticmethod
    def from_filesystem(slug):
        return Websheet.from_module(getattr(__import__("exercises." + slug), slug))

def basic_test():
    c = Websheet.chunkify(
r"""foo
\[bar\show:moo  ]\
  
\fake[
fakeeke
]\
man """)
    print(repr(c))
    if c[0]:
        for e in c[1]:
            print(repr(e))
    else:
        print(c[1])

if __name__ == "__main__":

    # call Websheet.py json
    if sys.argv[1:] == ["json"]:
        websheets = [Websheet.from_filesystem(slug) for slug in ("MaxThree", "FourSwap", "NextYear")]

        # test of json chunking
        for w in websheets:
            print(w.get_json_template())
        sys.exit(0)

    # call Websheet.py interactive
    if sys.argv[1:] == ["interactive"]:
        websheets = [Websheet.from_filesystem(slug) for slug in ("MaxThree", "FourSwap", "NextYear")]

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


    # call Websheet.py get_reference_solution MaxThree
    if sys.argv[1] == "get_reference_solution":
        websheet = Websheet.from_filesystem(sys.argv[2])
        print(json.dumps(websheet.get_reference_solution("Ref_Sols")))
        sys.exit(0)

    # call Websheet.py get_json_template MaxThree
    if sys.argv[1] == "get_json_template":
        websheet = Websheet.from_filesystem(sys.argv[2])
        print(json.dumps(websheet.get_json_template()))
        sys.exit(0)

    # call Websheet.py get_html_template MaxThree
    if sys.argv[1] == "get_html_template":
        websheet = Websheet.from_filesystem(sys.argv[2])
        print(json.dumps({"code":websheet.get_json_template(),"description":websheet.description}))
        sys.exit(0)

    # call Websheet.py make_student_solution MaxThree stu and input [{code: " int ", from: ..., to: ...}, ...]
    if sys.argv[1] == "make_student_solution":
        websheet = Websheet.from_filesystem(sys.argv[2])
        user_input = input() # assume json all on one line
        user_poschunks = json.loads(user_input)
        print(json.dumps(websheet.make_student_solution(user_poschunks, "student."+sys.argv[3] if len(sys.argv) > 3 else None)))
        sys.exit(0)

    # call Websheet.py list
    if sys.argv[1:] == ["list"]:
        r = []
        for file in os.listdir("exercises"):
            if file.endswith(".py") and not file.startswith("_"): r.append(file[:-3])
        r.sort()
        print(json.dumps(r))
        sys.exit(0)

    print("Invalid command for Websheet")
    sys.exit(1)
