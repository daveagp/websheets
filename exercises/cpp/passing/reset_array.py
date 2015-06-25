attempts_until_ref = 0
source_code = r"""
#include <iostream>
using namespace std;

void reset_array(int arr[], int n) {
\[
   for (int i=0; i<n; i++)
      arr[i] = 0;
]\
}

int main() {
   int the_inputs[100];
   int n;
   // read n, then n inputs
   cin >> n;
   for (int i=0; i<n; i++) cin >> the_inputs[i];
   // call YOUR function
   reset_array(the_inputs, n);
   // is the output correct?
   cout << "After calling your function, the array contains: ";
   for (int i=0; i<n; i++) cout << the_inputs[i] << " ";
   return 0;
}
"""

lang = "C++"

description = r"""
Define a function <tt>void reset_array(int arr[], int n)</tt> 
that takes an array <tt>arr</tt> of length <tt>n</tt>, 
and resets all of its entries to zero.
<p>You should <b>not</b> use cin or cout, that part is done for you
in order to facilitate testing.
"""

tests = [
    ["3\n2014 9 17", []],
    ["8\n99 11 17 71 39 0 93 38", []],
] # stdin, args
