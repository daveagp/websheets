source_code = r"""
#include <iostream>
using namespace std;

\[
bool is_even(int x) {
   return (x%2 == 0);
}
]\
"""

lang = "C++"

mode = "func"

description = r"""
Define a function <tt>is_even</tt> that takes an integer argument
<tt>x</tt>, and returns the <tt>bool</tt> value <tt>true</tt> when
<tt>x</tt> is even, and <tt>false</tt> otherwise.
<p>
<b>Note: don't use <tt>cout</tt></b> in your code. 
Just <tt>return</tt> the appropriate value. The grader will 
automatically add print statements as it sees fit.
"""

tests = [
    ["check-function", "is_even", "bool", ["int"]],
    ["call-function", "is_even", ["11"]],
    ["call-function", "is_even", ["4"]],
    ["call-function", "is_even", ["103"]],
    ["call-function", "is_even", ["52"]]
]


