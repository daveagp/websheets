source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int i = 5;
   int* addr; // type declaration
   addr = &i; // addr gets the address of i

   // two dereferences, one read, one write:
   cout << *addr << endl; // what is stored at addr?
   *addr = 10; // store 10 where addr points

   cout << i << endl; // what is stored in i?
}
"""

lang = "C++"

description = r"""
Examples of fundamental pointer operations.
"""

example = True

tests = [
    ["", []]
]


