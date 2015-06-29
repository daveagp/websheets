source_code = r"""
#include <iostream>
using namespace std;

void countdown(int n) {
  // whoops!
\[
  if (n == 0)
\show:
  if (n == 100) // whoops!
]\
   {
      cout << "Blastoff!" << endl;
   }
   // recursive case
   else {
      cout << n << endl;
      // recursive call
      countdown(n-1);
   }
}

int main() {
   countdown(5);
}
"""

example = True

remarks = "The purpose of this example is to use wwhen discussing the meaning of 'stack overflow' and the goal of a base case."

lang = "C++"

description = r"""
Using a recursive function.
"""

tests = [
    ["", []]
]


