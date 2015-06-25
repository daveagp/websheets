source_code = r"""
#include <iostream>
using namespace std;

double* find_min(double* a, int n) {
\[
   double* result = a; // start with first element by default
   for (int i=0; i<n; i++) {
      if (a[i] < *result) {
         result = a + i;
      }
   }
   return result;
]\
}

int main() {
   int n;
   cin >> n;
   double arr[100];
   for (int i=0; i<n; i++) cin >> arr[i];
\hide[
   double arr0[100];
   for (int i=0; i<n; i++) arr0[i] = arr[i];
]\

   // call your function and save result
   double* min_loc = find_min(arr, n);
   
\fake[
   cout << ...;    // there is some hidden testing code here
]\
\hide[
   for (int i=0; i<n; i++) if (arr0[i] != arr[i]) {
      cout << "Error: your function min_loc altered the array element " << i << endl;
   }
   if (min_loc < arr - 1 || min_loc > arr + n)
      cout << "Error: returned a pointer far outside the arr" << endl;
   else if (min_loc == arr - 1)
      cout << "Error: returned a pointer 8 bytes before start of arr" << endl;
   else if (min_loc == arr + n)
      cout << "Error: returned a pointer 8 bytes after end of arr" << endl;
   else {
      cout << "Returned a pointer " << 8*(min_loc-arr) << " bytes after start of arr" << endl;
   }
]\
   cout << "Pointed-to value is " << *min_loc << endl;

   // change that variable to 1000
   *min_loc = 1000;
   // run your code again
   min_loc = find_min(arr, n);
   
\fake[
   cout << ...;    // there is some hidden testing code here
]\
\hide[
   if (min_loc < arr - 1 || min_loc > arr + n)
      cout << "Error: returned a pointer far outside the arr" << endl;
   else if (min_loc == arr - 1)
      cout << "Error: returned a pointer 8 bytes before start of arr" << endl;
   else if (min_loc == arr + n)
      cout << "Error: returned a pointer 8 bytes after end of arr" << endl;
   else {
      cout << "Returned a pointer " << 8*(min_loc-arr) << " bytes after start of arr" << endl;
   }
]\
   cout << "Pointed-to value is " << *min_loc << endl;
}
"""

lang = "C++"

description = r"""
Write a function <tt>find_min</tt> that takes a <tt>double</tt> pointer
indicating the start of an array, and an <tt>int</tt> indicating the 
length of the array. It should return a pointer to the minimum number
in the array.
<p>You can assume there are no ties.
"""

tests = [
    ["3\n8.5 1.1 6.3", []],
    ["5\n10 20 30 40 50", []],
    ["4\n-1 -2 -3 -4", []],
]


