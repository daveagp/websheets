source_code = r"""
#include <iostream>
#include <cstdlib>
using namespace std;

// main should accept command-line arguments
int main(\[int argc, char* argv[]]\) {

\[
   cout << "Hello, " << argv[1] << "!";
]\
   return 0;
}
"""

lang = "C++"

description = r"""
Write a program <tt>hello</tt> which prints a greeting to the person
named on the command line. E.g.:
<pre><b>$</b> <i>./hello Joe</i></pre>
should print out
<pre>Hello, Joe!</pre>
"""

tests = [
    ["", ["Joe"]],
    ["", ["World"]],
    ["", ["goodbye"]],
]

attempts_until_ref = 0
