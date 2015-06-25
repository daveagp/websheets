source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int n;
   cin >> n;
\[
   for (int i=0; i<n; i++) {
      if (i % 2 == 0)
         for (int j=0; j<n; j++) {
            if (j % 2 == 0)
               cout << "*";
            else
               cout << " ";
         }
      else
         for (int j=0; j<n; j++) {
            if (j % 2 == 1)
               cout << "*";
            else
               cout << " ";
         }
      cout << endl;
   }  
]\
   return 0;
}
"""

lang = "C++"

description = r"""
This program takes an integer input <tt>n</tt>.
Print out a checkerboard with <tt>n</tt> rows and 
<tt>n</tt> columns in a checkerboard pattern of stars; e.g. when <tt>n</tt>
is 4:
<pre>
* * 
 * *
* *
 * *
</pre>
The top-left should always be a star.
"""

tests = [
    ["4", []],
    ["5", []],
    ["10", []],
    ["15", []],
] # stdin, args

attempts_until_ref = 0
