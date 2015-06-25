source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int hr, min, sec;
   cout << "Enter hours and minutes separated by a space: " << endl;

   // now receive the hours and minutes as input from the user,
   // and use them to compute the number of seconds
\[
   cin >> hr >> min;
   sec = 3600*hr + 60*min;
]\

   cout << "That translates to " << sec << " seconds!" << endl;
   return 0;
}
"""

lang = "C++"

description = r"""
This program should read in an integer number of 
hours and minutes from the user
(placing them in the <code>hr</code> and <code>min</code> variables).  You
should then compute the equivalent number of seconds in the <code>sec</code>
variable.  The answer will be output to the screen.
"""

tests = [["0 40", []],
         ["20 1", []],] # stdin, args
