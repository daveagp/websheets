source_code = r"""
#include <iostream>
using namespace std;

// declare the return type, function name, and arguments
 \[double]\ discriminant (double a, \[double b, double c]\) {
   // return the computed value
\[
   return b*b-4*a*c;
]\
  }
"""

lang = "C++"

mode = "func"

description = r"""
Define a function <tt>discriminant(a, b, c)</tt> that takes
three <tt>double</tt> arguments, and returns the value of
$$b^2-4ac$$
<b>Note: don't use <tt>cout</tt></b> in your code. 
Just <tt>return</tt> the appropriate value. The grader will 
automatically add print statements as it sees fit.
"""

tests = [
    ["check-function", "discriminant", "double", ["double"]*3],
    ["call-function", "discriminant", ["1", "1", "1"]],
    ["call-function", "discriminant", ["1", "4", "4"]],
    ["call-function", "discriminant", ["2", "3", "5"]],
    ["call-function", "discriminant", ["1.4", "0.2", "3.9"]],
    ["call-function", "discriminant", ["-5.4", "2.02", "7.3"]]
]


