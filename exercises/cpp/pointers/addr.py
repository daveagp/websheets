source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int a;
   int b[10];
   double c;
   int d;
   
   cout << "address of a: " << &a << endl;
   cout << "address of b: " << &b << endl;
   cout << "address of c: " << &c << endl;
   cout << "address of d: " << &d << endl;
}
"""

lang = "C++"

description = r"""
Prints the address of several variables.
"""

example = True

tests = [
    ["", []]
]


