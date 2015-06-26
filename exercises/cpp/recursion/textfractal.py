description = r"""
A ruler's pattern makes shorter marks each time you divide the length
in half. Mimic this with a static method <code>printRuler(n)</code> that
prints a ruler like this whose longest line has length <code>n</code>.
For example <code>printRuler(2)</code> should print out
<pre>
-
--
-
</pre>
and <code>printRuler(3)</code> should print out
<pre>
-
--
-
---
-
--
-
</pre>
"""
source_code = r"""
#include <iostream>
using namespace std;

void printRuler(int n) {
   // return if we're in the base case. 
\[
   if (n == 0) return;
]\
   // otherwise, make two recursive calls, with a length-n line in between
   printRuler(\[n-1]\);
\[
   for (int i=0; i<n; i++)
      cout << '-';
   cout << endl;
   printRuler(n-1);
]\
}

int main() {
   int n;
   cin >> n;
   printRuler(n);
}
"""

tests = [
    ["1", []],
    ["2", []],
    ["3", []],
    ["4", []],
    ["5", []],
]


attempts_until_ref = 0
lang = "C++"
