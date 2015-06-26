attempts_until_ref = 0
source_code = r"""
#include <iostream>
using namespace std;

// compute product by treating a as an array
double product1(double* a, int n) {
   double running_product = 1;
   for (int i=0; i<n; i++) {
      \[running_product *= a[i];]\
   }
   return running_product;
}

// compute product by increasing a by one position at a time
double product2(double* a, int n) {
   double running_product = 1;
   while (n > 0) {
      // multiply in the next number
      running_product *= \[*a]\;
      a++; // increase the pointer by one position
      n--; // one less number to go
   }
   return running_product;
}

int main() {
   double sample_inputs[3] = {2.5, -1.0, 3.0};
   // product of all the numbers?
   cout << product1(sample_inputs, 3) << endl;
   // try another way
   cout << product2(sample_inputs, 3) << endl;
   return 0;
}
"""

lang = "C++"

description = r"""
Write a function <tt>product1</tt> that takes a <tt>double</tt> pointer
indicating the start of an array, and an <tt>int</tt> indicating the 
length of the array. It should return the product of all the numbers
in the array. Do the same thing again with another function <tt>product2</tt>,
using a different approach.
"""

tests = [
    ["", []]
]


