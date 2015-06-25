source_code = r"""
/* 
 This program takes no input, and outputs a greeting.
 By David Pritchard (dpritcha)
*/

#include <iostream>
using namespace std; // access cout and endl

int main(int argc, char *argv[]) {
   cout << "Hello, world!";
   cout << endl; // end the line
   return 0; // by convention
}
"""

lang = "C++"

example = True

description = r"""
A very verbose "Hello, World!" program.
"""

tests = [["", []]] # stdin, args
