attempts_until_ref = 0

source_code = r"""
#include <iostream>
using namespace std;

void replace_first(int arr[], int n, int target, int replacement) {
\[
   for (int i=0; i<n; i++) {
      if (arr[i] == target) {
         arr[i] = replacement;
         return; // don't change any more!
      }
   }
]\
}

int main() {
   // read n, t, r, then n inputs
   int the_inputs[100];
   int n, t, r;
   cin >> n >> t >> r;
   for (int i=0; i<n; i++) cin >> the_inputs[i];
   cout << "Before calling your function, the array contains: ";
   for (int i=0; i<n; i++) cout << the_inputs[i] << " ";
   cout << endl;

   // call YOUR function
   replace_first(the_inputs, n, t, r);

   // is the output correct?
   cout << "After calling your function, the array contains: ";
   for (int i=0; i<n; i++) cout << the_inputs[i] << " ";
   return 0;
}
"""

lang = "C++"

description = r"""
Define a function <tt>void replace_first(int arr[], int n, int target, 
int replacement)</tt> 
that takes an array <tt>arr</tt> of length <tt>n</tt>,
finds the <i>first</i> entry whose value equals <tt>target</tt>, and
changes its value to <tt>replacement</tt>. If no such entry exists, do nothing.
<p>You should <b>not</b> use cin or cout, that part is done for you
in order to facilitate testing.
"""

tests = [
    ["3 9 10\n2014 9 17", []],
    ["8 39 103\n99 11 17 71 39 0 93 38", []],
    ["8 39 103\n99 11 17 71 39 0 39 38", []],
] # stdin, args
