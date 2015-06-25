source_code = r"""
#include <iostream>
using namespace std;

void sort2(int* a, int* b)
{
   if (\[*a > *b\show:a > b]\) {
\[
      int tmp = *a;
      *a = *b;
      *b = tmp;
]\
   }
}

int main() {
   int x = 4, y = 5, p = 3, q = 9, m = 5, n = 2, u = 8, v = 1;
   cout << "Before sort2(&x, &y), x is " << x << " and y is " << y << ". ";
   sort2(&x, &y);
   cout << "After x is " << x << " and y is " << y << endl;
   cout << "Before sort2(&q, &p), q is " << q << " and p is " << p << ". ";
   sort2(&q, &p);
   cout << "After q is " << q << " and p is " << p << endl;
   cout << "Before sort2(&m, &n), m is " << m << " and n is " << n << ". ";
   sort2(&m, &n);
   cout << "After m is " << m << " and n is " << n << endl;
   cout << "Before sort2(&v, &u), v is " << v << " and u is " << u << ". ";
   sort2(&v, &u);
   cout << "After v is " << v << " and u is " << u << endl;
}
"""

lang = "C++"

description = r"""
Define a function <tt>sort2</tt> that takes two <tt>int</tt> pointers
as inputs. It should <b>sort</b> them so that the value pointed to by the 
first argument is less
than or equal to the second.
<p>Hint: use the swap idiom. Also, note that the given code has a bug.
"""

tests = [
    ["", []]
]


