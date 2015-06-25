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
* Solution for Hats Part 1
*
* Read in list size and permutations of that size.
* Determine if each is a "derangement". 
* Print out the first derangement if it exists.
* Print out the number of derangements.
*****************************************************************************/

#include <iostream>
using namespace std;

// print the first derangement with the given format
void printD(int r[], int length) {
   cout << "First derangement:";
   for (int i = 0; i < length; i++)
      cout << " " << r[i];
   cout << endl;
}
    
// return true if r holds a derangement, false otherwise
bool isD(int r[], int length) {
   for (int i = 0; i < length; i++) {
      if (r[i] == i+1) //i+1 to account for C++ 0-based arrays
         return false;
   }
   return true;
}

int main() {
   // the # of items in permutation
   int N;
   cin >> N;

   // space to hold permutation
   int arr[100];

   // how many derangements have we seen?
   int count = 0;          
        
   // Read until there are no more permutations left on StdIn.
   while (!cin.fail()) {
      // fill array
      for (int i = 0; i < N; i++)
         cin >> arr[i];

      if (!cin.fail()) {

         // if arr is a derangement, count i
         // and print it if it's the first.
         if (isD(arr, N)) { 
            if (count == 0) 
               printD(arr, N); 
            count++; 
         }
      }
   }
   cout << "Number of derangements: " << count << endl;;
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
