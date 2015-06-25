attempts_until_ref = 0

source_code = r"""
#include <iostream>
using namespace std;

void reset(int& x) // pass a _reference_ (pointer)
{
   x = 0;          // writes to address passed in
}

int main() {
   int num = 103;
   reset(num);     // pass by _reference_ (implicit pointer)
   cout << num;
}
"""

lang = "C++"

description = r"""
Resetting a variable using pass-by-reference syntax.
"""

tests = [
    ["", []]
]

example = True
