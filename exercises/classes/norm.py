attempts_until_ref = 0

source_code = r"""
#include <iostream>
#include <cmath>
using namespace std;

// point.h
class Point {
public:
   Point(double x, double y);
   double dot(Point other);
   double norm();
private:
   double x;
   double y;
};

// point.cpp
Point::Point(double x, double y) {
   // parameter names same as data members :(
   this->x = x; // woohoo
\[
   this->y = y;
]\
}

double Point::dot(Point other) {
   return x * other.x + y * other.y;
}

double Point::norm() {
   // square root of dot product with self
\[
   return sqrt(this->dot(*this));
]\
}

// test code
int main() {
   Point p(3, 4);
   Point q(2, 0);
   cout << p.dot(q) << endl;
   cout << p.norm() << endl;
   cout << q.norm() << endl;
}
"""

lang = "C++"

description = r"""
Define a two-dimensional <tt>Point</tt> class. 
<p>
The method <tt>p.dot(q)</tt> should compute the dot product $p \cdot q = p_x \times q_x + p_y \times q_y$.
<p>
The method <tt>p.norm()</tt> should compute the norm of $p$, defined as $\sqrt{p \cdot p}$.
"""

tests = [["", []]] # stdin, args


cppflags_remove = ["-Wshadow"]
