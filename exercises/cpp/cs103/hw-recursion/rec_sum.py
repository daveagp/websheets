description = r"""
Define a recursive function <tt>int sum_up_to(int n)</tt>
that computes the sum of the first <tt>n</tt> integers without using a loop.
<br>
E.g. <tt>sum_up_to(3)</tt> is 1+2+3 which is 6.
"""

source_code = r"""
#include <iostream>
using namespace std;

int sum_up_to(int n) {
   // base case, nothing to add
   if (\[n == 0]\)
      return \[0]\;
   else {
      // make a recursive call to n-1
      int rec_result = \[sum_up_to(n-1)]\;
      // add the missing number
      int total = \[rec_result + n]\;
      // return the total
      return \[total]\;
   }
}

int main() {
   int n;
   cin >> n;
   cout << sum_up_to(n);
}
"""

lang = "C++"

tests = [
    ["3", []],
    ["4", []],
    ["1", []],
    ["100", []],
]

verboten = ("#include", "for", "while", "*")

