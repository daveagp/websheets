source_code = r"""
#include <iostream>
#include <algorithm>
using namespace std;

int maxPath(int n, int** cellValue) {
   // opt[i][j]: max value attainable if starting at position [i][j]
   int opt[n][n]; // bad style!

   // base case: corner
   opt[n-1][n-1] = cellValue[n-1][n-1];
   // pseudo-base case: right column, have to go down
   for (int i=n-2; i>=0; i--)
      opt[i][n-1] = cellValue[i][n-1] + opt[i+1][n-1];
   // pseudo-base case: bottom row, have to go right
   for (int j\[=n-2; j>=0; j--]\)
      \[opt[n-1][j] = cellValue[n-1][j] + opt[n-1][j+1]]\;
   // general case
   for (int i\[=n-2; i>=0; i--]\) {
      for (int j\[=n-2; j>=0; j--]\) {
         // a choice! take better choice of down and right
         opt[i][j] = cellValue[i][j] + \[max]\(\[opt[i+1][j]]\,
                                             \[opt[i][j+1]]\);
      }
   }
   // value in top-left corner
   return \[opt[0][0]]\;
}

int main() {
   int n;
   cin >> n;
   int** coins = new int*[n];
   for (int i=0; i<n; i++) coins[i] = new int[n];
   for (int i=0; i<n; i++)
      for (int j=0; j<n; j++)
         cin >> coins[i][j];
   cout << maxPath(n, coins);
}
"""

description = r"""
<style> .ss {font-family:sans-serif} </style>
Nintendo's new minimalist video game controller only has two buttons,
<span class='ss'>down</span>
 and 
<span class='ss'>right</span>.
In the platform launch title Super Mario Multiverse,
every level is a square grid of cells 
where Mario starts in the top-left corner. Some
cells of the grid have coins with a value, and other cells
are empty. The player has to press <span class='ss'>down</span>
 and <span class='ss'>right</span> in some order until
they get to the bottom-right corner, and their score is the sum total of
the value of 
all coins they hit along the way. Write a program
to find the maximum possible score for any level.

<p>
We represent a level by an integer <tt>n</tt> giving the square room size,
then an <tt>n</tt>-by-<tt>n</tt> grid <tt>cellValue</tt> where 
<tt>cellValue[i][j]</tt> is the cell <tt>i</tt>th from the top
and <tt>j</tt>th from the left.
A positive value means a coin with that value,
and a value of 0 means no coin is in that cell. 

<p>
For example, suppose the input is
<pre>
5
1 1 0 2 0
0 2 0 2 0
0 1 0 0 1
3 0 0 0 1
0 0 0 0 0
</pre>
Mario has lots of possible paths. Remember he must go from the top-left
to the bottom-right using only steps <span class='ss'>right</span>
 (R) and <span class='ss'>down</span> (D).
If he goes D-D-D-R-R-R-R-D, he gets a score of 1+3+1=5. The path
R-D-R-R-D-R-D-D achieves a score of 1+1+2+2+1+1=8, which happens to be 
the maximum possible for this room.
<p>
Write a function <code>int maxPath(int n, int** cellValue)</code>
that computes the maximum score for a level given in this format. 
Use dynamic programming: compute, for each position, the best value 
you can get if you start in that cell.
"""

lang = "C++"

attempts_until_ref = 0

tests = [
    ["5\n1 1 0 2 0\n0 2 0 2 0\n0 1 0 0 1\n3 0 0 0 1\n0 0 0 0 0", []],
    ["3\n31 2 0\n5 26 6\n0 4 33", []],
    ["3\n0 2 31\n6 26 5\n33 4 0", []],
    ["4\n5 3 1 0\n0 3 4 0\n5 3 4 0\n0 2 1 0", []],
    ["2\n1 2\n3 4", []],
    ["10\n1 5 8 4 1 0 2 4 0 6\n8 3 6 8 6 4 6 2 8 0\n3 6 0 1 1 9 8 4 2 0\n2 0 4 4 1 9 1 3 3 3\n2 0 4 8 9 6 5 0 8 2\n9 5 7 6 0 0 5 4 4 3\n7 4 9 1 4 4 1 4 8 2\n6 1 4 7 0 8 5 8 3 8\n9 6 0 2 3 6 6 4 5 2\n5 0 5 1 6 1 4 3 5 0", []],
]

