attempts_until_ref = 0

source_code = r"""
#include <iostream>
using namespace std;

\[ bool ]\ streq(\[ char a[], char b[] ]\) {
\[
   int i=0;
   while (true) {
      if (a[i] == '\0' && b[i] == '\0')
         return true; // got to end
      if (a[i] != b[i])
         return false; // different OR one ended earlier
      i++;
   }  
]\
}
"""

lang = "C++func"

description = r"""
Define a function <tt>streq</tt> that takes 
two character arrays as input,
and checks whether they are equal (contain the same text). 
"""

tests = [
    ["check-function", "streq", "bool", ["char[]"]*2],
    ["call-function", "streq", ['"programming"']*2],
    ["call-function", "streq", ['"programming"', '"programs"']],
    ["call-function", "streq", ['"hi"', '"bye"']],
    ["call-function", "streq", ['"hi"', '"hippie"']],
    ["call-function", "streq", ['"thistle"', '"this"']],
]


