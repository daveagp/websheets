source_code = r"""
#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
   cout << boolalpha;

   cout << "Fail before read? " << cin.fail() << endl;

   int i;
   cin >> i;

   cout << "Fail after read?  " << cin.fail() << endl;
}
"""

example = True

lang = "C++"

description = r"""
Failing. The input will be <tt>eleventeen</tt>.
"""

tests = [
    ["eleventeen", []]
]


