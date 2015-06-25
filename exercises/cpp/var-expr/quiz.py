source_code = r"""
#include <iostream>
using namespace std; 

int main() {
\[
   cout << (double) 12 / 15 * 100; // what was my percent score on the quiz?
\show:
   cout << (12 / 15) * 100; // what was my percent score on the quiz?
]\
   return 0;
}
"""

lang = "C++"
attempts_until_ref = 0

description = r"""
An example of integer division.
"""

tests = [["", []]]
