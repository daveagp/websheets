attempts_until_ref = 0

source_code = r"""
#include <iostream>
using namespace std; // access cout and endl

int main() {
   int sum;
\hide[
 sum = -234767;
]\ 
\[
   sum = 0;
   for (int i=1; i<=100; i++) {
      sum += i;
   }
   cout << sum;
\show:
   for (int i=1; i<=100; i++) {
      sum += i;
   }
   cout << sum;
]\
}
"""

lang = "C++"
attempts_until_ref = 0
description = r"""
What is the source of the bug?
"""

tests = [["", []]] # stdin, args
