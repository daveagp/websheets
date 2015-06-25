source_code = r"""
#include <iostream>
using namespace std;

// return the absolute value of x
int abs(int x) {
\[
   if (x > 0) {
      return x;
   }
   else {
      return -x;
   }
\show:
   if (x > 0) {
      return x;
   }
   if (x <= 0) {
      return -x;
   }
]\
} 

// test it
int main() {
   cout << abs(3) << endl;
   cout << abs(-7) << endl;
   return 0;
}

"""

lang = "C++"

description = r"""
Fix the compiler error to get a working definition of abs(),
the absolute value function."""

tests = [["", []]]

attempts_until_ref = 0
