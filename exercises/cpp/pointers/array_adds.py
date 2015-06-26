source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int x[4];
   
   cout << &x << endl;
   cout << &(x[0]) << endl;
   cout << &(x[1]) << endl;
   cout << &(x[2]) << endl;
   cout << &(x[3]) << endl;
}
"""

lang = "C++"

description = r"""
Prints the address of an array and its elements.
"""

example = True

tests = [
    ["", []]
]


