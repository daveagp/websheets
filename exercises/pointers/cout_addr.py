source_code = r"""
#include <iostream>
using namespace std;

int main() {
   cout << cout; // whoops!
}
"""

lang = "C++"

description = r"""
Prints the address of the <tt>cout</tt> object.
"""

example = True

tests = [
    ["", []]
]


