source_code = r"""
#include <string>
#include <iostream>
using namespace std;

void stars(int n) {
   if (\[n == 13]\) {
      // print out frowny
      \[cout << ":(";]\
      // the function is done
      \[return;]\
   }
   for (\[int i=0; i<n; i++]\) {
      cout << "*";
   }
}
"""

lang = "C++"

mode = "func"

description = r"""
Define a function <tt>stars</tt> that takes an integer argument
<tt>n</tt>. It should print out <tt>n</tt> stars. 
<p>However, if <tt>n</tt>
is 13, which is bad luck, print out a sad face <tt>":("</tt> instead
and don't print any stars.
"""

tests = [
    ["check-function", "stars", "void", ["int"]],
    ["call-function", "stars", ["10"]],
    ["call-function", "stars", ["3"]],
    ["call-function", "stars", ["13"]],
]


