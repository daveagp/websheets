
source_code = r"""
#include <iostream>
#include <cstdlib>
#include <algorithm>
using namespace std; 
\[
int main(int argc, char* argv[]) {
   double A = atof(argv[1]);
   double B = atof(argv[2]);
   double C = atof(argv[3]);

   double smallest = min(A, min(B, C));
   double largest = max(A, max(B, C));
   double middle = A+B+C - smallest - largest;

   if (largest >= smallest + middle) {
      cout << "impossible" << endl;
      return 0;
   }

   if (largest*largest == smallest*smallest + middle*middle) {
      cout << "right";
   }
   else if (largest*largest > smallest*smallest + middle*middle) {
      cout << "obtuse";
   }
   else {
      cout << "acute";
   }

   cout << " ";

   if (largest == middle && middle == smallest) {
      cout << "equilateral";
   }
   else if (largest == middle || middle == smallest) {
      cout << "isoceles";
   }
   else {
      cout << "scalene";
   }

   cout << endl;
}
]\
"""

lang = "C++"

attempts_until_ref = 0

description = r"""
<p>Write a program <code>triangle</code> that takes three command-line 
arguments, representing the side lengths of a triangle.

<p>First, you should check that the sides are actually possible. This means
that
<ul>
<li>All three sides are positive
<li>Each side is shorter than the sum of the other two sides 
(the <a href="http://en.wikipedia.org/wiki/Triangle_inequality">triangle 
inequality</a>)
</ul>
If it's not possible to build a triangle with those sides, 
print out <tt>impossible</tt> and nothing else.

If it's possible to build a triangle with those sides, you
will print out two facts about the triangle. 
<ol>
<li>The first fact should be <tt>right</tt>, <tt>acute</tt>, or
<tt>obtuse</tt>. In a right triangle, the longest side squared equals
the sum of the squares of the other two sides (the 
<a href="http://en.wikipedia.org/wiki/Pythagorean_theorem">Pythagorean
theorem</a>).
If the longest side's square is larger than the sum of the
other two sides, the triangle is obtuse. If smaller, it's called acute.
<li>The second fact should be <tt>equilateral</tt>, <tt>isoceles</tt>,
or <tt>scalene</tt>. In an equilateral triangle, all three sides are 
equal. In an isoceles triangle, exactly two sides are equal. In a scalene
triangle, all sides have different lengths.
</ol>

For example:
<ul>
<li><tt>triangle 10 10 10</tt> should print <tt>acute equilateral</tt>
<li><tt>triangle 3 4 5</tt> should print <tt>right scalene</tt>
<li><tt>triangle 100 60 60</tt> should print <tt>obtuse isoceles</tt>
<li><tt>triangle 100 40 40</tt> should print <tt>impossible</tt>
</ul>

Highlight the following box if you need a hint.
<span style='border:1px solid black; color: white'>
It will simplify things if you start by creating variables
representing the longest, shortest, and other side length.
</span>
"""

tests = [["", ["10", "10", "10"]],
         ["", ["3", "4", "5"]],
         ["", ["100", "60", "60"]],
         ["", ["100", "40", "40"]],
         ["", ["100", "50", "50"]],
         ["", ["50", "40", "30"]],
         ["", ["5", "13", "12"]],
         ["", ["50", "30", "50"]],
         ["", ["30", "30", "50"]],
         ["", ["29", "30", "31"]],
         ["", ["2", "3", "4"]],
         ["", ["-2", "-3", "-4"]],
         ["", ["0", "0", "0"]],
         ["", ["25", "25", "35.3553390593273762"]],
]
