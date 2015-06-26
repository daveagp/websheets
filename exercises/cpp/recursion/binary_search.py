attempts_until_ref = 0

source_code = r"""
#include <iostream>
using namespace std;

int bsearch(int target, int arr[], int n) {
   // each iteration, 
   // look for 'target' in 'arr[first]..arr[last]'
   int first = 0;
   int last = n-1;
 
   while (true) {
      // empty range
      if (first>last) {
         return -1;
      }

      if (first==last) {
         // we're done, for better or worse
\[
         if (target == arr[first])
            return first;
         else
            return -1;
]\
      }

      int mid = (last+first)/2;
      // did we find it?
      if (\[target == arr[mid]]\) {
         \[return mid;]\
      }
      // continue the search in the appropriate half
      else if (target > arr[mid]) {
         \[first = mid+1;]\
      }
      else {
         \[last = mid-1;]\
      }
   }
}

int main() {
   // read target, n, then n sorted inputs
   int target, n;
   cin >> target >> n;
   int* arr = new int[n];
   for (int i=0; i<n; i++)
      cin >> arr[i];

   cout << bsearch(target, arr, n);

   delete [] arr;
   return 0;
}
"""

lang = "C++"

description = r"""
Fill out the method <tt>bsearch(int target, int arr[], int n)</tt> 
to return -1 if <tt>arr</tt> doesn't contain <tt>target</tt>, 
and otherwise return <tt>i</tt> where <tt>target == arr[i]</tt>.
<p>The <tt>main()</tt>, filled out for you, reads sample cases
containing the target, n, and list of numbers in the array.
"""

tests = [
    ["68\n15\n2 8 15 29 33 34 39 59 60 67 68 80 89 92 98", []],
    ["67\n15\n2 8 15 29 33 34 39 59 60 67 68 80 89 92 98", []],
    ["50\n15\n2 8 15 29 33 34 39 59 60 67 68 80 89 92 98", []],
    ["25\n4\n10 20 30 40", []],
    ["1\n15\n2 8 15 29 33 34 39 59 60 67 68 80 89 92 98", []],
    ["10\n8\n3 8 21 43 78 100 102 105", []],
    ["100\n8\n3 8 21 43 78 100 102 105", []],
    ["1000\n8\n3 8 21 43 78 100 102 105", []],
] # stdin, args
