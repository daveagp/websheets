source_code = r"""
#include <iostream>
#include <cmath>
using namespace std;

double length(double dx, double dy) {
\[
   return sqrt(dx*dx + dy*dy);
]\
}

double distance(double x1, double y1, \[double x2, double y2]\) {
   return length(\[x1-x2, y1-y2]\);
}
"""

lang = "C++"

mode = "func"

description = r"""
In this exercise, you will define a 2D vector length function, and you will
use that to help you define a 2D distance function.
<p>
Given a 2D vector denoted $(dx, dy)$, its length, denoted $|(dx, dy)|$,
is given by the formula
$$|(dx, dy)| = \sqrt{dx^2+dy^2}$$
First, define a C++ function <tt>length(dx, dy)</tt> 
that returns the length of the vector
$(dx, dy)$. Remember that <tt>sqrt()</tt>
computes the square root of a number.
<p>
Additionally, given a pair of 2D points,
call them $(x_1, y_1)$ and $(x_2, y_2)$,
the vector from one to the other is defined as
$$|(x_1-x_2, y_1-y_2)|$$
and the distance between those two points is defined as that vector's length: 
$$\textrm{distance}(x_1, y_1, x_2, y_2) = |(x_1-x_2, y_1-y_2)|$$
Here is an illustration of this definition; the vector's length is the distance between the points.
<div style='text-align:center'><img src='http://bits.usc.edu/websheets/exercises/cs103/hw-functions/dist.ipe.png'></div>

Define a function <tt>distance(x1, y1, x2, y2)</tt>
that computes the distance between two points, using the <tt>length</tt> function that you
previously defined as a subroutine. 
"""

tests = [
    ["check-function", "length", "double", ["double"]*2],
    ["call-function", "length", ["3", "4"]],
    ["call-function", "length", ["1", "1"]],
    ["call-function", "length", ["1.2", "-0.5"]],
    ["check-function", "distance", "double", ["double"]*4],
    ["call-function", "distance", ["0", "0", "3", "4"]],
    ["call-function", "distance", ["10", "100", "13", "104"]],
    ["call-function", "distance", ["-2.3", "1", "1.5", "-2.2"]
]
    
                                       ]


