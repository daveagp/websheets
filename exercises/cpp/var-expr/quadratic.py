source_code = r"""
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
   int a, b, c;

   cout << "Enter the integer coefficients separated by spaces: " << endl;
   cin >> a >> b >> c;
\[
   int det = b*b - 4*a*c;
   double r1 = (-b + sqrt(det)) / (2 * a);
   double r2 = (-b - sqrt(det)) / (2 * a);
\show:
   int det = b*b - 4*a*c; // GOOD IDEA: reuse complex subexpression as variable
   int r1 = -b + sqrt(det) / 2 * a;
   int r2 = -b - sqrt(det) / 2 * a;
]\
   cout << "The roots are: " << r1 << " and " << r2 << endl;

   return 0;
}"""

lang = "C++"
attempts_until_ref = 0

tests = [["1 -6 8", []],
         ["2 8 8", []],
         ["1 -1 -1", []]]

description = r"""
Given integer inputs
<code>a</code>, <code>b</code> and <code>c</code>, print out the 
roots of <code>ax<sup>2</sup> + bx + c = 0</code>. They are given by
the formula
$$\Large \frac{-b \pm \sqrt{b^2-4ac}}{2a}$$
A starter solution is given, but it is buggy! Fix it.

<p>Note that we won't be able to detect imaginary roots until
next week when we have <tt>if</tt> statements.
"""
