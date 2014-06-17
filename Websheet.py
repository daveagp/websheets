#!/usr/bin/python3

"""
Class to:
- convert websheet definition (key-value string pairs) to a Websheet instance
- pull out components: read-only and read-write parts, reference solutions
- splice together read-write inputs to make a compilable student solution

Note: the parser is a relatively cheap and dirty solution that assumes
that the delimiters never occur in comments or quotes
in the source code. While this approach should be practical,
a more full solution could be done by extending the java_syntax module.
"""

import re
import sys
import os
import exercises
import json
from java_syntax import java_syntax

indent_width = 3

def record(**dict):
    """ e.g. foo = record(bar='baz', jim=5) creates an object foo
    such that foo.bar == 'baz', foo.jim == 5 """
    result = type('', (), dict)
    def __toString():
       tos = "("
       for x in dir(result):
           if x[0] != "_": 
               tos += x + ":" + repr(getattr(result, x))+","
       return tos + ")"
    result._toString = __toString
    return result

# should be enum, but let's not require python 3.4
ChunkType = record(plain=1, blank=2, fake=3, hide=4)

class Chunk:
    def __init__(self, text, type, attr=None): # avoid aliasing
        self.text = text
        self.type = type
        if attr is None: attr={}
        self.attr = attr 
    def __repr__(self):
        return repr([self.text, self.type, self.attr])

class Websheet:

    @staticmethod
    def chunkify(source):
        """
        Websheet source is converted internally into a list of chunks.
        Each chunk has
        type: plain, blank, fake, or hide
        text: string. if non-plain and contains an \n, it must
              start with \n, and implicitly ends with \n
        attr: dict of additional properties (like "show" for blank)

        Returns [False, "error string"] or [True, list of chunks]
        """

        open_delim = {r'\[', r'\hide[', r'\fake['}
        close_delim = {']\\'} # rawstring can't end in \
        delim = open_delim | close_delim

        typemap = {r"\[":ChunkType.blank,
                   r"\hide[":ChunkType.hide,
                   r"\fake[":ChunkType.fake}

        # normalize by collapsing whitespace around syntactically correct
        # delimiters for multi-line regions.
        for d in delim | {r"\show:"}:
            source = re.sub("\n[ \t]*"+re.escape(d)+"[ \t]*\n",
                            "\n"+d.replace("\\", "\\\\")+"\n",
                            source)

        # replace ]\ at end of line, if not the only thing on line,
        # with ]\_ (space). This is so RHS of inline joins never start with \n
        # e.g. "...(w);]\" at end of line in CircularQuote
        source = re.sub(r"(.)\]\\$", r"\1]\ ", source, flags=re.MULTILINE)

        # analogous thing at start of line, although no websheets so far use it
        source = re.sub(r"^\[\\(.)", r" \[\1", source, flags=re.MULTILINE)

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
                        " followed by another opening delimiter "
                        +close.group(0)]

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

                if chunk.type == ChunkType.blank:
                    # sized blank
                    chunk.attr["show"] = "\n"*max(2, contained.count("\n"))
                    # maybe generalize later
                    p = contained.find("\n\\show:\n")
                    if p != -1:
                        chunk.text = contained[:p+1] # include \n
                        chunk.attr["show"] = contained[p+7:] # include \n

                result.append(chunk)

            else: # inline case
                if interstitial != "":
                    result.append(Chunk(interstitial, ChunkType.plain))
                    
                chunk = Chunk(contained, typemap[match.group(0)])

                if chunk.type == ChunkType.blank:
                    def normalize(text):
                        if not text.startswith(" "): text = " " + text
                        if not text.endswith(" "): text = text + " "
                        return text
            
                    # maybe generalize later
                    p = contained.find("\\show:")
                    if p != -1:
                        chunk.text = normalize(contained[:p]) 
                        chunk.attr["show"] = normalize(contained[p+6:])
                    else:
                        chunk.text = normalize(contained)
                        # sized blank
                        chunk.attr["show"] = " " * len(chunk.text)

                result.append(chunk)

            last_close_end = close.end()

        interstitial = source[last_close_end:]

        result.append(Chunk(interstitial, ChunkType.plain))

        # do some sanity checking
        for i in range(0, len(result)):
            def err(msg, info = None):
                return [False, "Failed sanity check: chunk " + str(i) + " "
                        + msg + ":\n" + repr(result[i].text) +
                        ("" if info is None else "\n" + repr(info)) ]
            if len(result[i].text)<1: return err("is too short")
            if (result[i].type != ChunkType.plain and "\n" in result[i].text):
                if len(result[i].text)<2: return err("is too short")
                if result[i].text[0] != '\n': return err("has bad start")
                if result[i].text[-1] != '\n': return err("has bad end")
            if (i > 0 and
                ((result[i-1].text[-1] == "\n") !=
                 (result[i].text[0] == "\n"))):
                return err("joins incorrectly with previous chunk")
            if "show" in result[i].attr:
                if (("\n" in result[i].attr["show"])
                    != ("\n" in result[i].text)):
                    return err("has wrong show shape", result[i].attr["show"])
                if "\n" in result[i].attr["show"]:
                    show_text = result[i].attr["show"]
                    if len(show_text)<2: return err("show is too short")
                    if show_text[0] != '\n': return err("show has bad start")
                    if show_text[-1] != '\n': return err("show has bad end")

        # parsed ok
        return [True, result]

    def __init__(self, field_dict):
        """
        Constructor, accepts a string-to-string dictionary of field names,
        values. Some are mandatory and some are optional; optional ones
        will appear anyway as fields, but just with default values.
        """

        mandatory_fields = ["classname", "source_code", "tests", "description"]

        # optional fields AND default values
        optional_fields = {"tester_preamble": None, "show_class_decl": True,
                           "epilogue": None, "dependencies": [], "imports": [],
                           "lang": "Java", "slug": None}
        if "lang" in field_dict:
            optional_fields["show_class_decl"] = False

        for field in mandatory_fields:
            setattr(self, field, field_dict[field])

        for field in optional_fields:
            setattr(self, field,
                    field_dict[field] if field in field_dict
                    else optional_fields[field])

        if self.slug is None:
            self.slug = self.classname
            
        for field in field_dict:
            if (not field.startswith("_") and
                field not in mandatory_fields and
                field not in optional_fields): 
                raise Exception("Unknown field" + field)

        # normalize so starts, ends with newline if not already present
        if not self.source_code.startswith("\n"):
            self.source_code = "\n"+self.source_code
        if not self.source_code.endswith("\n"):
            self.source_code = self.source_code+"\n"

        # as a convenience, add public class classname { ... } if not there
        if (self.lang == "Java" and
            "public class "+self.classname not in self.source_code):
            # indent if outer declaration will be visible
            def indent(s):
                needsfix = s.endswith("\n")
                s = s.replace("\n", "\n" + (" "*indent_width))
                if needsfix: s = s[:-indent_width]
                return s

            if self.show_class_decl:
                self.source_code = indent(self.source_code)
            self.source_code = ("\npublic class " + self.classname + " {" +
                                self.source_code+"}\n")

        # hide class declaration if requested.
        # note! for this to work, comments should go inside of class decl.
        
        if not self.show_class_decl:
            # hide thing at start
            self.source_code = re.sub( 
                "^public class "+self.classname+r" *\{ *$",
                r"\hide["+"\n"+"public class "+self.classname+" {\n"+"]\\\\",
                self.source_code,
                flags=re.MULTILINE)
            # hide thing at end
            self.source_code = re.sub(
                "\n}\s*$",
                "\n" + r"\hide[" + "\n" + "}" + "\n" + "]\\\\" + "\n",
                self.source_code)

        chunkify_result = Websheet.chunkify(self.source_code)

        if not chunkify_result[0]:
            raise Exception("Could not parse websheet source code: " 
                            + chunkify_result[1])

        self.chunks = chunkify_result[1]

        if len(self.imports) > 0:
            import_text = "\n" + "".join("import "+i+";\n"
                                         for i in self.imports)
            self.chunks = ([Chunk(import_text, ChunkType.plain)]
                           + self.chunks)

        self.chunks = ([Chunk("\nimport stdlibpack.*;\n", ChunkType.hide)]
                       + self.chunks)

        #print(repr(self.chunks))
        
        self.input_count = 0
        for chunk in self.chunks:
            if chunk.type == ChunkType.blank:
                self.input_count += 1

    def combine_with_template(self, student_code, package = None):
        """
        student_code: a list of chunks, one for each blank region in the UI

        returns [False, "error string"] -- usually error means student
          did some syntactically bad thing like unmatched parens within a blank
        or [True, combined code, map from student solution line#s to ui line#s]
        """
        
        if self.input_count != len(student_code):
            return [False, "Internal error! Wrong number of inputs"]

        r = [] # resulting text of combined solution, to be joined later
        linemap = {}
        ui_lines = 1 # user interface lines
        cs_lines = 1 # combined solution lines
        ui_endswith_newline = True
        cs_endswith_newline = True

        def add_text(text, to_ui, to_ss):
            nonlocal r, linemap, ui_lines, cs_lines
            nonlocal ui_endswith_newline, cs_endswith_newline

            #print([text, to_ui, to_ss])
            
            # adjustment: when a chunk ends with a newline and is followed
            # by a chunk starting with a newline, that's only one line
            if to_ui and ui_endswith_newline and text.startswith("\n"):
                ui_lines -= 1
            if to_ss and cs_endswith_newline and text.startswith("\n"):
                cs_lines -= 1

            if to_ui and to_ss:
                for i in range(text.count("\n")):
                    linemap[cs_lines+i+1] = ui_lines+i+1

            if to_ui:
                ui_lines += text.count("\n")
                ui_endswith_newline = text.endswith("\n")

            if to_ss:
                if cs_endswith_newline and text.startswith("\n"):
                    r.append(text[1:])
                else:
                    r.append(text)

                cs_lines += text.count("\n")
                cs_endswith_newline = text.endswith("\n")
            
        last_line_with_blank = -1
        blank_count_on_line = -1

        add_text('\n' if package is None else 'package '+package+';\n',
                 False, True)

        blanks_processed = 0

        for chunk in self.chunks:
            if chunk.type == ChunkType.plain:
                add_text(chunk.text, True, True)

            elif chunk.type == ChunkType.fake:
                add_text(chunk.text, True, False)
                
            elif chunk.type == ChunkType.hide:
                add_text(chunk.text, False, True)

            elif chunk.type == ChunkType.blank:
                    
                i = blanks_processed
                blanks_processed += 1

                user_text = student_code[i]

                # deprecated: in place of a code chunk,
                # you can pass a dict with "code" as the code chunk,
                # plus other attributes. here we just pull out the text
                if isinstance(user_text, dict):
                    user_text = user_text["code"]

                if (len(user_text)) < 2:
                    return ["False", "Internal error: User chunk " + str(i)
                            + " too short: " + user_text]
                if "\n" in user_text:
                    if "\n" not in chunk.text:
                        return ["False", "Internal error: User chunk " + str(i)
                                + " shouldn't be multiline: " + user_text]
                    if user_text[0] != '\n':
                        return ["False", "Internal error: User chunk " + str(i)
                                + " multiline but doesn't start with newline"] 
                    if user_text[-1] != '\n':
                        return ["False", "Internal error: User chunk " + str(i)
                                + " multiline but doesn't end with newline"]

                if ui_lines == last_line_with_blank and '\n' not in chunk.text:
                    blank_count_on_line += 1
                else:
                    last_line_with_blank = ui_lines
                    blank_count_on_line = 1

                valid = java_syntax.is_valid_substitute(
                    chunk.text, user_text)

                if not valid[0]:
                    # not valid substitute.
                    # report error that makes sense for ui user sees
                    match = re.search(
                        re.compile(
                        r"^Error at line (\d+), column (\d+):\n(.*)$"),
                        valid[1])

                    if match is None: # error at end of chunk
                        user_pos = ui_lines + user_text.count("\n") 
                        if "\n" in user_text:
                            user_pos -= 2
                            pos_desc = "Line "+str(user_pos)
                        else:
                            pos_desc = ("Line "+str(user_pos)+
                                        ", editable region "
                                        + str(blank_count_on_line))
                        return [False, pos_desc + ":\n" + valid[1]]

                    else: # error within chunk
                        user_line = ui_lines + int(match.group(1))
                        return [False, "Line "+str(user_line)
                                + ": " + match.group(3)]

                add_text(user_text, True, True)
                
        return [True, ''.join(r), linemap]

    def get_reference_solution(self, package = None):
        """
        Get the reference solution for use in grading. Note that the UI
        exposes this in a different way, using get_reference_snippets
        and then combine_with_template.
        """
        r = []

        r += ['\n' if package is None else 'package '+package+';\n']

        for chunk in self.chunks:
            if chunk.type in {ChunkType.plain,
                              ChunkType.blank, ChunkType.hide}:
                if r[-1].endswith("\n") != chunk.text.startswith("\n"):
                    raise Exception("Sanity check failed: " + repr([r[-1], chunk.text]))
                if r[-1].endswith("\n"):
                    r.append(chunk.text[1:])
                else:
                    r.append(chunk.text)
        
        return ''.join(r)

    def get_reference_snippets(self):
        """
        Get snippets of reference solution in a format that
        they can be displayed in the UI
        """
        return [chunk.text for chunk in self.chunks
                if chunk.type == ChunkType.blank]
        
    def get_initial_snippets(self):
        """
        Get contents of blank areas as they would appear to someone
        opening a problem for the first time.
        """
        return [chunk.attr["show"] for chunk in self.chunks
                if chunk.type == ChunkType.blank]
         
    def get_json_template(self):
        """
        Return an odd-length alternating list of strings:
        the first (0th), third, etc are read-only,
        the other positions are editable areas for the student.
        Note that each editable area either starts and ends with a space,
        or starts and ends with a newline. (The UI always assumes this.)
        """

        r = ["\n"]

        for chunk in self.chunks:
            if chunk.type in {ChunkType.plain, ChunkType.fake}:
                if (r[-1].endswith("\n")):
                    if not r[0].startswith("\n"):
                        raise Exception("Sanity check failed!")
                    r[-1] += chunk.text[1:]
                else:
                    r[-1] += chunk.text
            elif chunk.type == ChunkType.blank:
                r += [chunk.attr["show"]]
                r += [""]

        # absorb newlines into the editable part
        for i in range(len(r)-1):
            if r[i].endswith("\n") or r[i+1].startswith("\n"):
                if not (r[i].endswith("\n") and r[i+1].startswith("\n")):
                    raise Exception("Sanity check failed!")
                if (i%2 == 0): r[i] = r[i][:-1]
                else: r[i+1] = r[i+1][1:]

        # remove trailing newlines from last read-only region and start of first
        while r[-1].endswith("\n"): r[-1] = r[-1][:-1]
        if not (r[0].startswith("\n")):
            #print(repr(r))
            raise Exception("Sanity check failed!")
        r[0] = r[0][1:]
        
        return r

    def prefetch_urls(self, stringify = False):
        """
        Go through the "tests" field. Look for anything of the form
        testStdinURL = "...";
        and prefetch their data from the web. Return a dict whose keys
        are those urls and whose values are their contents (bytes objects)
        If stringify is True, the bytes objects are converted into strings
        (containing only unicode code points 0-255)
        """
        result = {} # empty dict
        for match in re.finditer(r'testStdinURL *= *"(.*)";', self.tests):
            from urllib.request import urlopen
            url = match.group(1)
            result[url] = urlopen(url).read()
            if stringify: result[url] = "".join(chr(e) for e in result[url])
        return result
            
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
        dicted["slug"] = module.__name__.split(".")[-1]
        return Websheet(dicted)

    @staticmethod
    def from_filesystem(slug):
        return Websheet.from_module(getattr(__import__("exercises." + slug), slug))

    @staticmethod
    def list_filesystem():
        r = []
        for file in os.listdir("exercises"):
            if file.endswith(".py") and not file.startswith("_"): r.append(file[:-3])
        r.sort()
        return r

    def testing_ui(self):
        import config
        r = {}
        r["json_template"] = self.get_json_template()
        r["initial_snippets"] = self.get_initial_snippets()
        r["reference_snippets"] = self.get_reference_snippets()
        r["reference_solution"] = self.get_reference_solution("reference")
        r["combined_with_initial"] = self.combine_with_template(r["initial_snippets"], "combined.initial")
        r["combined_with_reference"] = self.combine_with_template(r["reference_snippets"], "combined.reference")
        r["daveagp"] = config.load_submission("daveagp@gmail.com", self.slug, maxId = 876)
        r["combined_with_daveagp"] = self.combine_with_template(r["daveagp"], "combined.daveagp")
        return json.loads(json.dumps(r)) # to remove things like numeric keys

    def regression_ui(self):

        def print_differences(old, new, desc):

            def rangey(obj):        
                if isinstance(obj, dict): return obj.keys()
                if isinstance(obj, list): return range(len(obj))
                return None

            result = False
            
            oldrange = rangey(old)
            newrange = rangey(new)
            
            # not both have members
            if (oldrange == None) or (newrange == None):
                if old != new:
                    print(desc+" was " + repr(old) + " now " + repr(new))
                return True

            for x in oldrange:
                if x not in newrange:
                    print(desc+"["+repr(x)+"] was " + repr(old[x]) +
                          "now doesn't exist")
                    result = True

            for x in newrange:
                if x not in oldrange:
                    print(desc+"["+repr(x)+"] didn't exist, now "
                          + repr(new[x]))
                    result = True

            for x in newrange:
                if x in oldrange:
                    if print_differences(old[x], new[x], desc+"["+repr(x)+"]"):
                        result = True

            return result

        regressed = False
        current_result = self.testing_ui()
        old_result = json.load(open("_regression_/"+self.slug+".json"))
        if print_differences(old_result,
                             current_result,
                             "websheet " + self.slug + " key "):
            regressed = True
        return regressed

    def regression_save(self):
        outf=open("_regression_/"+self.slug+".json", 'w')
        print(json.dumps(self.testing_ui(),indent=4, separators=(',', ': '), sort_keys=True),
              file=outf)
        outf.close()

if __name__ == "__main__":

    # call Websheet.py get_reference_solution MaxThree
    if sys.argv[1] == "get_reference_solution":
        websheet = Websheet.from_filesystem(sys.argv[2])
        print(json.dumps(websheet.get_reference_solution("reference")))

    # call Websheet.py get_json_template MaxThree
    elif sys.argv[1] == "get_json_template":
        websheet = Websheet.from_filesystem(sys.argv[2])
        print(json.dumps(websheet.get_json_template()))

    # call Websheet.py get_html_template MaxThree
    elif sys.argv[1] == "get_html_template":
        websheet = Websheet.from_filesystem(sys.argv[2])
        print(json.dumps({"code":websheet.get_json_template(),"description":websheet.description}))

    # call Websheet.py combine_with_template MaxThree stu and input [{code: " int ", from: ..., to: ...}, ...]
    elif sys.argv[1] == "combine_with_template":
        websheet = Websheet.from_filesystem(sys.argv[2])
        user_input = input() # assume json all on one line
        user_poschunks = json.loads(user_input)
        print(json.dumps(websheet.combine_with_template(user_poschunks, "student."+sys.argv[3] if len(sys.argv) > 3 else None)))

    elif sys.argv[1] == "testing_ui":
        print(json.dumps(Websheet.from_filesystem(sys.argv[2]).testing_ui()))

    elif sys.argv[1] == "testall_ui":
        wslist = Websheet.list_filesystem()
        print(json.dumps({slug: Websheet.from_filesystem(slug).testing_ui() for slug in wslist}
                         ,indent=4, separators=(',', ': '))) # pretty!

    elif sys.argv[1] == "regression_save":
        Websheet.from_filesystem(sys.argv[2]).regression_save()

    elif sys.argv[1] == "regression_save_all":
        for slug in Websheet.list_filesystem():
            print(slug)
            Websheet.from_filesystem(slug).regression_save()

    elif sys.argv[1] == "regression":
        Websheet.from_filesystem(sys.argv[2]).regression_ui()

    elif sys.argv[1] == "regression_all":
        for slug in Websheet.list_filesystem():
            print(slug)
            Websheet.from_filesystem(slug).regression_ui()

    elif sys.argv[1] == "list":
        print(json.dumps(Websheet.list_filesystem()))

    else:
        print("Invalid command for Websheet")
        sys.exit(1)
