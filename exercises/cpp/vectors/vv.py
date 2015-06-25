attempts_until_ref = 0

source_code = r"""
#include <vector>
#include <iostream>
using namespace std;

int main() {
   // declare
\[
   vector<vector<int> > matrix;
\show:
   vector<vector<int>> matrix;
]\

   // fill in
   vector<int> row1;
   row1.push_back(1);
   row1.push_back(5);
   vector<int> row2;
   row2.push_back(2);
   row2.push_back(8);
   matrix.push_back(row1);
   matrix.push_back(row2);

   // print out
   for (int r=0; r<2; r++) {
      for (int c=0; c<2; c++) {
         // print out entry at row r, column c
         cout << matrix\[[r][c]]\ << " ";
      }
     cout << endl;
   }
}
"""

lang = "C++"

tests = [["", []]]

description = r"""
Declare a vector of vectors. It is trying to create this matrix:
$$\begin{bmatrix}1 & 5 \\ 2 & 8\end{bmatrix}$$
"""

