attempts_until_ref = 0

source_code = r"""
#include <iostream>
#include <vector>
using namespace std;

// function to get Kth entry from end of vector
// K=0 is last entry, K=1 is second-last, etc
double kth_last_entry(\[vector<double>& vec\show:vector<double> vec]\, int K) {
   return vec[vec.size()-K-1];
}

int main() {
   // create array 1/1, 1/2, ... 1/1000000
   vector<double> values;
   for (int i=1; i<=1000000; i++)
      values.push_back(1.0/i);
   
   // add it in reverse order
   double sum = 0;
   for (int K=0; K<1000000; K++)
      sum += kth_last_entry(values, K);
   cout << sum << endl;
}
"""

lang = "C++"

description = r"""
In this exercise we improve an order of growth by using references.
This program computes the millionth <i>harmonic number</i>,
$$H_{1000000} = 1/1 + 1/2 + \cdots + 1/1000000.$$
It adds the numbers in reverse order to get more numerical stability. 
"""

tests = [
    ["", []]
]

