source_code = r"""
#include <iostream>
using namespace std;

// return the length (# non-null characters) of the C-string
// (null-terminated character array) passed as an argument
 \[int]\ strlen(\[char src[]]\)
{
\[
   int x = 0;
   while (src[x] != '\0') {
      x++;
   }
   return x;
]\
}
"""

lang = "C++"

mode = "func"

description = r"""
Define a function <tt>strlen</tt> that takes a single character array as input, 
<tt>src</tt>.  <tt>src</tt> is a null-terminated character array. Return
the number of non-null characters in the string.  Example:  "hi" should return
2 while "" should return 0.
"""

tests = [
    ["check-function", "strlen", "int", ["char[]"]],
    ["call-function", "strlen", ['"hi"']],
    ["call-function", "strlen", ['""']],
    ["call-function", "strlen", ['"hello world"']],
    ["call-function", "strlen", ['"Walk your bike!"']],
]


