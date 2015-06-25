description = r"""
Write a recursive method <code>factorial(n)</code>
that returns n &times; (n-1) &times; (n-2) &times; &hellip; &times; 3 &times; 2 &times 1. For example, <code>factorial(4)</code> should return 24 since that is the value of 4 &times; 3 &times; 2 &times; 1.
"""

source_code = r"""
#include <iostream>
using namespace std;

 \[long]\ factorial(\[int n]\) {
   // base case
   if (\[n == 0]\) 
      return \[1]\;

   // reduction step
   // note that n! = n * (n-1) * ... * 2 * 1 = n * ((n-1) * ... * 2 * 1)
   return \[n]\ * factorial(\[n-1]\);
}

int main() {
   int n;
   cin >> n;
   cout << factorial(n);
}
"""

lang = "C++"

tests = [
    ["4", []],
    ["1", []],
    ["5", []],
    ["6", []],
    ["10", []],
    ["20", []],
]


attempts_until_ref = 0
