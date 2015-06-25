lang = "C++"

attempts_until_ref = 0

description = r"""
Please see <a href="http://bits.usc.edu/cs103/programming-exam/">the programming exam page</a>.
<br>
We recommend doing this practice in a timed environment; give yourself 90 minutes.
"""

source_code = r"""
// NOTE: The actual exam will not use Websheets (instead, the PA submit system).
// It's recommended to practice and test on your own machine and copy here to check.
 \[

/****************************************************************************
* Solution for Hats Part 2
*
* Read in list size and permutations of that size.
* Determine the max cycle length of each permutation.
* Compute and print the average max cycle length.
*****************************************************************************/

#include <iostream>
using namespace std;

// determine longest cycle to get own hat back
int maxCycleLength(int arr[], int N) {
   int max = 0;       // max cycle length
   int cycle;         // current cycle length

   // for each person
   for (int i = 0; i < N; i++) {
      int j = i;
      cycle = 1; // minimal cycle has 1 person 

      // while person j doesn't have person i's hat
      while (arr[j] != i+1) {
         j = arr[j] - 1;  // new person j to look for
         cycle++;
      }
                        
      if (max < cycle) max = cycle;  // new longest cycle
   }

   // return longest cycle length
   return max;
}
    
int main() {
   // the # of items in the permutation
   int N;
   cin >> N;
 
   // space to hold permutation
   int arr[100];

   // running sum for max cycle lengths
   int sum = 0;

   // how many derangements have we seen?
   int count = 0;
        
   // Read until there are no more permutations left on StdIn.
   while (!cin.fail()) {
      // fill array
      for (int i = 0; i < N; i++) {
         cin >> arr[i];
      }

      if (!cin.fail()) {
         // count it and find its max cycle length
         count++;
         sum += maxCycleLength(arr, N);
      }
   }    
   // compute and print average with the given format
   cout << "Average max cycle length: " << (double) sum / count << endl;
}
]\
"""

import urllib.request as _r

tests = [
["9\n9 8 7 6 5 4 3 2 1\n3 7 6 9 8 2 1 5 4", []],
["6\n1 2 6 4 3 5\n6 1 5 4 3 2", []],
["""9
1  2  3  4  5  6  7  8  9
9  8  7  6  5  4  3  2  1
2  1  4  3  6  5  8  7  9
8  9  2  1  4  7  5  3  6
3  7  6  9  8  2  1  5  4""", []],
[_r.urlopen('http://www.cs.princeton.edu/~cos126/docs/data/Hats/1000perms15.txt').read().decode('Latin-1'), []]]
