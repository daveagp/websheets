source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int limit;
   cin >> limit;

   // start a counter at 0: print 0*0 first
   int counter = 0;
   
   while (\[counter * counter <= limit]\) // while counter^2 at most limit
   {
      \[cout << counter * counter << endl]\; // print out square of counter
      \[counter = counter + 1;]\; // increase counter by one
   }

   return 0;
}
"""

lang = "C++"

description = r"""
This program should take a positive input <tt>limit</tt> and print out
all the square numbers less than or equal to <tt>limit</tt>, one per line.
For example if the input is <tt>13</tt> it should print out 
<pre>0
1
4
9
</pre>
"""

tests = [
    ["13", []],
    ["25", []],
    ["200", []],
    ["1", []],
    ["0", []],
] # stdin, args
