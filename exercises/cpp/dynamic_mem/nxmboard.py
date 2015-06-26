source_code = r"""
#include <iostream>
using namespace std;

// Given the values N and M, create an N row x M column
//  2D array with a checkerboard pattern

int main() {
   int n, m;
   cout << "Enter the size of the array: " << endl;
   cin >> n >> m;
\hide[
for (int __z=0; __z<1000000; __z++) {
]\

   // Select the right type for the nums value which stores
   //   what is returned by ordered_array()
   \[int**]\ board = new int*[n];

   for (int i=0; i < n; i++) {
      \[board[i] = new int[m];]\
   }

\hide[
if (__z==999999) {
]\
   for (int i=0; i < n; i++) {
      for (int j=0; j < m; j++) {
         board[i][j] = (i+j)%2;
      }
   }

   for (int i=0; i < n; i++) {
      for (int j=0; j < m; j++) {
         cout << board[i][j] << " ";
      }
      cout << endl;
   }
\hide[
}
]\
  
   // Do your cleanup here
  \[
    for (int i=0; i < n; i++) {
       delete[] board[i];
    }
    delete[] board; 
  ]\
\hide[
}
]\
   return 0;
}
"""

lang = "C++"

description = r"""
Write a program to dynamically allocate an NxM 2-D array as an array of arrays
(i.e. array of pointers) and create a checkerboard pattern of 1's and 0's.
Then free up all your memory.
<p> 
Your program will be run a million times. So make sure not to leak any
memory!
"""

tests = [
    ["3 4", [""]],
    ["8 4", [""]],
]

attempts_until_ref = 0
