source_code = r"""
#include <iostream>
using namespace std;

// Copy the characters from the src array to the destination array.
//  The arguments are passed as src followed by dest and both are
//  character arrays (C-Strings).  By definition of the C-Library, the
//  strcpy() function should return the src array.

 \[ char*  ]\ strcpy( \[  char*  src, char* dest  ]\ ) {
   // return the src array
\[
   int i=0;
   while( src[i] ){
     dest[i] = src[i]; i++;
   }
   dest[i] = 0;
]\
   return src;
}
"""

lang = "C++func"

description = r"""
Define a function <tt>strcpy()</tt> that takes a 'src' character array and
'dest' character array as input.  <tt>src</tt> and <tt>dest</tt> are  null-terminated character arrays. Return the <tt>src</tt> array.
"""

attempts_until_ref = 0

tests = [
    ["check-function", "strcpy", "char*", ["char[]", "char[]"]],
    ["call-function", "strcpy", ['"hi world"', '"         "']],
    ["call-function", "strcpy", ['"hi"', '"   "']],
    ["call-function", "strcpy", ['""', '" "']],
]


