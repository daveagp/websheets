attempts_until_ref = 0

source_code = r"""
#include <iostream>
using namespace std;

void swap_elements(int arr[], int i, int j) {
\[
   int tmp = arr[i];
   arr[i] = arr[j];
   arr[j] = tmp;
]\
}

int main() {
   // read n, i, j, then n inputs
   int the_inputs[100];
   int n, i, j;
   cin >> n >> i >> j;
   for (int k=0; k<n; k++) cin >> the_inputs[k];
   cout << "Before calling your function, the array contains: ";
   for (int k=0; k<n; k++) cout << the_inputs[k] << " ";
   cout << endl;

   // call YOUR function
   swap_elements(the_inputs, i, j);

   // is the output correct?
   cout << "After calling your function, the array contains: ";
   for (int k=0; k<n; k++) cout << the_inputs[k] << " ";
   return 0;
}
"""

lang = "C++"

description = r"""
Define a function <tt>void swap_elements(int arr[], int i, int j)</tt> 
that takes an array <tt>arr</tt>,
and swaps the elements at positions <tt>i</tt> and <tt>j</tt>.
<p>You should <b>not</b> use cin or cout, that part is done for you
in order to facilitate testing.
"""

tests = [
    ["3 0 1\n2014 9 17", []],
    ["8 5 7\n99 11 17 71 39 0 93 38", []],
    ["8 3 3\n99 11 17 71 39 0 93 38", []],
] # stdin, args
