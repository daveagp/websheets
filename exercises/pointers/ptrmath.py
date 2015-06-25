source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int x[] = {20, 14};
   int* y = &(x[0]); // start at first element
   y = y + 1;
   cout << *y; // what's y pointing to?
}
"""

lang = "C++"

description = r"""
Pointer arithmetic.
"""

example = True

tests = [
    ["", []]
]


