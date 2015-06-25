source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int value;
 
   // declare and initialize boolean variable
   \[bool]\ saw_thirteen = \[false]\;

   while (cin >> value) { // loop through all inputs
      if (\[value == 13]\) {
         // we saw a thirteen!
         \[saw_thirteen = true;]\
      }
   } // end of loop

   // did we see a thirteen?
   if (\[saw_thirteen]\) {
      cout << "Unlucky";
   }

   return 0;
}
"""

lang = "C++"

description = r"""
This program should take a list of integers as input (the list can 
be of any length).
If any of the integers was 13, your program should print out
<tt>Unlucky</tt>. If none of the integers was 13, it should print nothing.
<p>
Use the loop to process all the input, a boolean variable to remember
whether you've seen a thirteen, 
and an <tT>if</tt> statement to check each input, and
another <tT>if</tt> statement to decide
whether to print.
"""

tests = [
    ["1 2 3", []],
    ["11 12 13", []],
    ["1 2 3 5 8 13 21 34", []],
    ["13 13 13", []],
    ["1 4 9 16 25", []]
] # stdin, args
