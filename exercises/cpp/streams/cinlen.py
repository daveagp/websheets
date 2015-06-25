source_code = r"""
#include <iostream>
#include <cstring>
using namespace std;

int main() {
   int result = 0;
   while (\[!cin.fail()]\) {
\[
      // get the next character
      char ch = (char) cin.get();
      if (!cin.fail())
         result++;
]\
   }
   cout << \[result]\ << endl;
   return 0;
}
"""

lang = "C++"

description = r"""
Write a <i>file size calculator</i>: it should tell you how long
its input <tt>cin</tt> was. For instance, if <tt>word.txt</tt> contains
<tt>Hello</tt>, then <tt>./cinlen &lt; word.txt</tt> should print <tt>5</tt>.
<p>
You will need to use <tt>get</tt> and <tt>fail</tt>. Remember that <tt>fail</tt> returns <tt>true</tt> <i>after</i> reading past the end of the file.
"""

cppflags_remove = ["-Wall"]
cppflags_add = ["-Wall", "-Wno-unused-variable"]

tests = [
    ["Hello", []],
    ["2  spaces", []],
    ["/==\\\n|oo|\n\\==/", []],
]


