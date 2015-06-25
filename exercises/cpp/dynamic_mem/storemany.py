source_code = r"""
#include <iostream>
#include <cstring>
using namespace std;


int main() {
   int n;
   int* data;
\[
  n = 0;
  // note: this is a correct, but inefficient solution!
  // better: keep extra space and double the size when full
  while (true) {
     int val;
     cin >> val;
     if (val == -1) break;

     // this is the nth item
     n++;
     int* old_data = data;
     data = new int[n];
     for (int i=0; i<n-1; i++) {
        data[i] = old_data[i];
     }
     data[n-1] = val;
     if (n != 1) delete[] old_data;
  }
]\
   // print everything out, twice
   for (int i=0; i<n; i++) {
      cout << data[i] << " ";
   }
   for (int i=0; i<n; i++) {
      cout << data[i] << " ";
   }
   delete[] data;
   return 0;
}
"""

lang = "C++"

description = r"""
Write a program that will read a sequence of integers of any length
from input, with <tt>-1</tt> indicating the end of input. Then it
should print out that sequence twice. For example if the input is
<pre>
2014 10 7 -1
</pre>
then the output should be
<pre>
2014 10 7 2014 10 7
</pre>
"""

import random as _random

tests = [
    ["2014 10 7 -1", []],
    [" ".join([str(_random.randint(0, 99)) for _ in range(10)])+" -1", []],    
    [" ".join([str(_random.randint(0, 99)) for _ in range(10000)])+" -1", []],    
]


