source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int x;
   cin >> x;
   // if x is equal to thirteen, print out "Unlucky"
\[   
   if (x == 13) {
     cout << "Unlucky";
   }
]\
   return 0;
}
"""

lang = "C++"

description = r"""
Complete this program so that when the input <tt>x</tt> is thirteen,
the program prints out <tt>Unlucky</tt> and otherwise, does nothing.
<br>Hint: use <tt><b>if</b></tt>.
<br>If you're not sure how to test if two numbers are equal, see page 83.
"""

tests = [
    ["12", []],
    ["13", []],
    ["14", []],
    ["-13", []]
] # stdin, args
