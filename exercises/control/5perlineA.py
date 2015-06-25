source_code = r"""
#include <iostream>
using namespace std;

int main() {
\[
for (int i=100; i<=200; i++) {
   cout << i << " ";
   if (i%5 == 4) cout << endl;}
\show:
   int i;
   // print integers from 100 to 200, 5 per line
   for (i = 100; i < 200; i+=5) {
      for (j = 0; j < 5; j+=1) {
         cout << i + j << " ";
      }
      cout << endl;
   }
   cout << i;
]\
   return 0;
}
"""

lang = "C++"
attempts_until_ref = 0

description = r"""
Print the integers from 100 to 200, five per line.
"""

tests = [["", []]]
