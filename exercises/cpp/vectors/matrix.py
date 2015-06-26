attempts_until_ref = 0

source_code = r"""
#include <vector>
#include <iostream>
using namespace std;

void print_matrix(vector<vector<int> > M) {
   for (int r=0; r<\[M.size()]\; r++) {
      for (int c=0; c<\[M[0].size()]\; c++) {
         cout << M[r][c] << " ";
      }
      cout << endl;
   }
}

int main() {
   // create a 3-by-3 matrix of zeros
   vector<vector<int> > nine_zeros(3, vector<int>(3, 0));
   // create a 2 row, 4 column matrix of ones
   vector<vector<int> > two_by_four\[(2, vector<int>(4, 1))]\;

   print_matrix(nine_zeros);
   cout << endl;
   print_matrix(two_by_four);
}
"""

lang = "C++"

tests = [["", []]]

description = r"""
Defining vectors-of-vectors with a given size.
"""

