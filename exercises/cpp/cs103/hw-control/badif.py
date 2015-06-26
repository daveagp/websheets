source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int first, second;
   cin >> first >> second;
\[
   if (first > second) {
      cout << first << " is bigger than " << second << endl;
   }
   
   if (second > first) {
     cout << second << " is bigger than " << first << endl;
   }

   if (first == second) {
     cout << "Both inputs are equal" << endl;
   }
\show:
   if (first > second); {
      cout << first << " is bigger than " << second << endl;
   }
   
   if (second > first) {
     cout << second << " is bigger than " << first << endl;
   }
   else { 
     cout << "Both inputs are equal" << endl;
   }
]\
   return 0;
}
"""

lang = "C++"

description = r"""
This program takes two integer inputs and compares them to see which
is bigger. Its output should look like
<tt>99 is bigger than 3</tt> or in the case the inputs are the same,
<tt>Both inputs are equal</tt>.
<p>A starter solution is given, but it has several bugs.
"""

tests = [
    ["99 3", []],
    ["103 301", []],
    ["78 78", []],
] # stdin, args
