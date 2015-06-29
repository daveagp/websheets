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
<p><i>The goal here is to get the program to produce the output <tt>Hi!</tt> before it crashes.
Initially, for a reason that will be explained in class, nothing is being output.</i>
"""

tests = [
    ["", []]
]


