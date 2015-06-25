source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int x = 5; // declare variable called x, set equal to 5
   cout << x * 2; // print out two times x

   x = 6; // change x. type not needed
   cout << x * 2; // what is printed?

   return 0;
}
"""

lang = "C++"

description = r"""
An example of variables.
"""

tests = [["", []]] # stdin, args

example = True
