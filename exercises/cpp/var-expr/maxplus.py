source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int x = 2147483647; // max integer
   cout << x + 1; // what is this?

   return 0;
}
"""

lang = "C++"

description = r"""
What is bigger than the biggest integer?
"""

tests = [["", []]] # stdin, args

example = True
