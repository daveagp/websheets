source_code = r"""
#include <iostream>
using namespace std;

void f(int* y)  {
   cout << *y;
}

int main() {
   int x[] = {103, 104};
   f(x);
}
"""

lang = "C++"

description = r"""
Arrays and pointers are often interchangeable.
"""

example = True

tests = [
    ["", []]
]


