source_code = r"""
#include <iostream>
using namespace std;

// you'll define this further below.
double rec_sqrt_helper(double x, double lo, double hi);

// function to compute the square root of x. Assumes x >= 0.
double rec_sqrt(double x) {

   // since sqrt(x) is between 0 and x+1, use that initial range
   double initial_lo = \[0]\;
   double initial_hi = \[x+1]\;

   // start the binary search
   return rec_sqrt_helper(\[x, initial_lo, initial_hi]\);
}

// recursive function. finds sqrt(x) within range lo..hi
double rec_sqrt_helper(double x, double lo, double hi) {
   
   // base case. if range is very small, accept it as sqrt
   if (hi - lo < 1E-8) {
      return lo; // return some point in range
   }

   // recursive case. 

   double mid = \[(lo+hi)/2]\; // midpoint between lo and hi
   // is mid smaller or bigger than sqrt(x)?
   // i.e. is mid^2 smaller or bigger than x?

   if (\[mid*mid < x]\) {
      // recurse on the appropriate half of the range
      return rec_sqrt_helper(\[x, mid, hi]\);
   }
   else {
      // recurse on the appropriate half of the range
      return \[rec_sqrt_helper(x, lo, mid)]\;
   }   
}

"""

description = r"""
Using recursion, define a function <tt>rec_sqrt(x)</tt>
that computes the square root of <tt>x</tt>. 
We will use binary search: think of it as binary-searching 
the real line for the number $y$ satisfying $y^2=x$.
<p>We will use recursive binary search. Each time, the recursive function
should be told the target value <tt>x</tt>, as well as 
lower bounds and upper bounds for where $\sqrt{x}$ could live.
The binary search will be recursive: each recursive call cuts
the search range in half.
<p>Since <tt>rec_sqrt(x)</tt> only takes one argument, recursing on the 
"range" needs more work. 
Let's define a second function, call it <tt>rec_sqrt_helper(x, lo, hi)</tt>
that is actually recursive: it does binary search in the specified range.
<p>Then <tt>rec_sqrt(x)</tt> only needs to get things started by calling
the helper function once.
"""

tests = [
    ["check-function", "rec_sqrt", "double", ["double"]],
    ["call-function", "rec_sqrt", ['16']],
    ["call-function", "rec_sqrt", ['103']],
    ["call-function", "rec_sqrt", ['1.23456']],
    ["call-function", "rec_sqrt", ['23432.989']],
    ["call-function", "rec_sqrt", ['0.25']],
    ["call-function", "rec_sqrt", ['4E14']],
    ["call-function", "rec_sqrt", ['9E-6']],
]

attempts_until_ref = 0

lang = "C++func"

verboten = ("#include", "for", "while")
