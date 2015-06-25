source_code = r"""
#include <iostream>
using namespace std;

\[
void countup(int n) {
  // base case
  if (n == 0) {
     cout << "Blastoff!" << endl;
  }
  // recursive case
  else {
     // recursive call
     countup(n-1);

     cout << n << endl;
  }
}
]\
"""

lang = "C++"

description = r"""
Write a recursive function <tt>countup(int n)</tt> that prints out
<tt>Blastoff!</tt>, followed by the numbers from 1 to n. For example
<tt>countup(5)</tt> should print out
<pre>
Blastoff!
1
2
3
4
5
</pre>
"""

tests = [
    ["check-function", "countup", "void", ["int"]],
    ["call-function", "countup", ['5']],
    ["call-function", "countup", ['10']],
    ["call-function", "countup", ['1']],
]

mode = "func"

attempts_until_ref = 0

verboten = ("#include", "for", "while")
