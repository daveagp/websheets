source_code = r"""
#include <string>
#include <iostream>
using namespace std;

\[
void exclaim(string word) {
   cout << word;
   cout << "!";
}
]\
"""

lang = "C++"

mode = "func"

description = r"""
Define a function <tt>exclaim</tt> that takes 
a <tt>string</tt> input and prints it out, followed by an exclamation point.
For example, if you call <tt>exclaim("void")</tt> it should print 
<pre>
void!
</pre>
It should not return anything. What does this make its return type?
"""

tests = [
    ["check-function", "exclaim", "void", ["string"]],
    ["call-function", "exclaim", ['"void"']],
    ["call-function", "exclaim", ['"C++"']],
    ["call-function", "exclaim", ['"exclaim"']],
]


