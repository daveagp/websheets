source_code = r"""
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std; 

int main() {
   cout << cos(0) << endl;
   cout << sqrt(2) << endl;
   cout << max(34, 56) << endl;
   return 0;
}
"""

lang = "C++"

example = True

description = r"""
An example of making function calls.
"""

tests = [["", []]]
