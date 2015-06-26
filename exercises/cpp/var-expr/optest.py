source_code = r"""
#include <iostream>
#include <string>
using namespace std;

int main() {
   cout << boolalpha << showpoint;

   \[int]\ x = \[5]\; // declare a variable
   \[int]\ y = \[6]\; // declare another variable
   cout << (x \[+]\ y); // try an operator!
}
"""

lang = "C++"

description = r"""
Use this to test out different operators.
"""

tests = [["", []]] # stdin, args

example = True
