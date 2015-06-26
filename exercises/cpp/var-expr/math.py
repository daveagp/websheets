source_code = r"""
#include <iostream>
#include <cstdlib>

using namespace std;

int main() {
\[
   int x, y;
   cin >> x >> y;

   cout << abs(x-y) << endl;
   cout << (x+y)/2.0 << endl;
   cout << x / y << endl;
]\
   return 0;
}"""

lang = "C++"

attempts_until_ref = 0

tests = [["20 3", []],
         ["5 4", []],
         ["100 4", []],
         ["3 20", []]]
         

description = r"""
Write a program that takes integer inputs
<code>x</code> and <code>y</code>, and outputs 4 lines containing:
<ul>
<li>Their difference
<li>Their average
<li>The integer quotient of <tt>x</tt> divided by <tt>y</tt>
</ul>
For example, if the input is <tt>20 3</tt>, the output should be
<pre>
17
11.5
6
</pre>
"""
