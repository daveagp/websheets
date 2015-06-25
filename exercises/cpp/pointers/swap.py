source_code = r"""
#include <iostream>
using namespace std;

void exchange(int* a, \[int* b]\)
{
\[
   int tmp = *a;
   *a = *b;
   *b = tmp;
]\
}

int main() {
   int x = 4, y = 5;
   cout << "Before exchange, x is " << x << " and y is " << y << endl;
   exchange(&x, &y);
   cout << "After exchange, x is " << x << " and y is " << y << endl;
   return 0;
}
"""

lang = "C++"

description = r"""
Define a function <tt>exchange</tt> that takes two <tt>int</tt> pointers
as inputs. It should exchange the values held at the locations
pointed to by its arguments.
"""

tests = [
    ["", []]
]

attempts_until_ref = 0

