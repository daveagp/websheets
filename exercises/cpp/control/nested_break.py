source_code = r"""
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
   // declare variables
\[
   int N;
   bool done = false;
\show:
   int N;
]\

   cin >> N;

   for (int i=1; \[i<10 && !done\show:i<10]\; i++) {
      for (int j=1; j<10; j++) {
         // print entry
         cout << setw(3) << i*j;

         // quit if needed
         if (i*j == N) {
\[
            done = true;
            break;
\show:
            break;
]\
         }
      }
      cout << endl;
   }

   cout << endl << "All done!";
}
"""

lang = "C++"

description = r"""
Write a program that does a <i>times table search</i>. 
It takes as input an integer N.
It will print
out consecutive elements of a 9x9 times table, stopping printing
if it finds N in the table. For instance if the input is <tt>15</tt>, 
it should output
<pre>
  1  2  3  4  5  6  7  8  9
  2  4  6  8 10 12 14 16 18
  3  6  9 12 15

All done!
</pre>
If the input doesn't appear in the table, all 9x9 entries should be printed.
<br>
A solution is given, but it uses <tt>break</tt> incorrectly: it assumes 
that it will stops all loops, but in reality it only stops the innermost loop.
Fix it by using a boolean control variable.
"""

tests = [
    ["15", []],
    ["12", []],
    ["51", []],
    ["49", []],
] # stdin, args

attempts_until_ref = 0

verboten = ["return"]
