source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int x;
   cin >> x;
   // print out either x or negative x
\[   
   if (x > 0) {
     cout << x;
   }
   else {
     cout << -x;
   }
]\
   return 0;
}
"""

lang = "C++"

description = r"""
Complete this program so that when the input <tt>x</tt> is positive, 
it prints <tt>x</tt>, and when it is negative, it prints <tt>-x</tt>.
<br>Hint: use <tt><b>else</b></tt>.
"""

tests = [
    ["1", []],
    ["10", []],
    ["-5", []],
    ["-103", []],
    ["0", []],
] # stdin, args
