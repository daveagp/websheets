source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int n;
   cin >> n;

   // declare an array called "pows"
   int pows[100]; // works for inputs up to 100

   // fill out the array
\[
   pows[0] = 1;
   for (int i=1; i<n; i++)
      pows[i] = pows[i-1]*2;
]\

   // output
   for (int i=0; i<n; i++)
      cout << "2^" << i << " is " << pows[i] << endl;
   return 0;
}
"""

lang = "C++"

description = r"""
Write a program that takes an input <tt>n</tt>, and 
fills out the array <tt>pows</tt> with the first 
<tt>n</tt> powers of 2.
<br>For example, <tt>pows[0]</tt> should be 1, <tt>pows[1]</tt> should be 2,
<tt>pows[2]</tt> should be 4, etc.
<br>Hint: you can't use <tt>pow</tt>, but what is the pattern in the numbers?
<br>The printing code is provided for you.
"""

tests = [
    ["4", []],
    ["10", []],
    ["32", []],
] # stdin, args

attempts_until_ref = 0
