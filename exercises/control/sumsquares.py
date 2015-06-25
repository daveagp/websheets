source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int total = 0; // start at 0

   for (int i = 1; i <= 10; i += 1) // i = 1, 2, ... 10
   {
      total = total + i*i; // increase total
   }

   cout << total;
   return 0;
}
"""

lang = "C++"

description = r"""
This program computes the sum of the first 10 integers' squares.
"""

tests = [
    ["", []],
] # stdin, args

example = True
