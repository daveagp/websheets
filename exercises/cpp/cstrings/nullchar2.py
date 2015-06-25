attempts_until_ref = 0

source_code = r"""
#include <iostream>
using namespace std; // access cout and endl

int main() {
\[

\show:
   char test[] = {'1', '0', '3', '\0', 'C', 'S', '\0'};
   cout << test << endl;
]\
   return 0;
}
"""

lang = "C++"

example = True

description = r"""
The effects of the null character.
"""

tests = [["", []]] # stdin, args
