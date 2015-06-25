source_code = r"""
#include <iostream>
#include <cmath>
using namespace std;

int main() {
   // read the input
   int n;
   cin >> n;

   double values[100]; // declare an array, max size 100
   for (int i = 0; i < n; i++) {      
      // element i of the array should contain the square root of i
\[
      values[i] = sqrt(i);
]\
   }

   for (int i = 0; i < n; i++) {
      cout << "The square root of " << i << " is " << values[i] << endl;
   }
   return 0;
}
"""

lang = "C++"

description = r"""
This program should take an integer <tt>n</tt> as input, 
then print out the square roots of the numbers from <tt>0</tt> to <tt>n-1</tt>.
<p>
The input/output is provided for you. Fill in the loop so that the array
<tt>values</tt> contains the desired square roots.
<p>
Remember that <tt>sqrt(x)</tt> is the function to compute the square root of 
<tt>x</tt>.
"""

tests = [
    ["5", []],
    ["20", []],
    ["0", []],
] # stdin, args
