source_code = r"""
#include <iostream>
using namespace std;

int main() {
\[

\show:
   for (int i=0; i<12; i++) {
      if (i % 3 == 2) {
         for (int j=0; j<i; j++) {
            cout << "*";
         }
         cout << endl;
      }
   }
]\
}
"""

lang = "C++"

description = r"""
What does this program do?
"""

tests = [["", []]] # stdin, args

example = True
