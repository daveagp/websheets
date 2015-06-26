source_code = r"""
#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
\[
   cout << "Hi!" << endl;
   \show:
   cout << "Hi!\n";
   while (true) {
   }
]\
}
"""

example = True

lang = "C++"

description = r"""
How can we force immediate printing?
"""

tests = [
    ["", []]
]


