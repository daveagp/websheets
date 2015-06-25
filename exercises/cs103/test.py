source_code = r"""
#include <iostream>
using namespace std;

// return type, function name, argument list
 \[double]\ recip(\[int]\ x) {
   // return the correct value
\[

\show:
   return 1.0/x;
]\
}
"""

lang = "C++"

mode = "func"

description = r"""
Define a function <tt>recip</tt> that takes an integer argument
<tt>x</tt>, and returns its reciprocal. For example
<tt>recip(10)</tt> should be 0.1, and <tt>recip(3)</tt> should be 
0.333333&hellip;
<p>
<b>Note: don't use <tt>cout</tt></b> in your code. 
Just <tt>return</tt> the appropriate value. The grader will 
automatically add print statements as it sees fit.
<p>Special checking for input equal to 0 is not required.
"""

tests = [
    ["check-function", "recip", "double", ["int"]],
    ["call-function", "recip", ["10"]],
    ["call-function", "recip", ["3"]],
    ["call-function", "recip", ["103"]],
     ["call-function", "recip", ["-5"]]
]


