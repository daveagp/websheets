source_code = r"""
public static int maxPath(int[][] cellValue) {
   int m = cellValue.length;    // height
   int n = cellValue[0].length; // width

   // opt[i][j]: max value attainable if starting at position [i][j]
   int[][] opt = new int[m][n];
   // base case: corner
   opt[m-1][n-1] = cellValue[m-1][n-1];
   // pseudo-base case: right column, have to go down
   for (int i=m-2; i>=0; i--)
      opt[i][n-1] = cellValue[i][n-1] + opt[i+1][n-1];
   // pseudo-base case: bottom row, have to go right
   for (int j\[=n-2; j>=0; j--]\)
      \[opt[m-1][j] = cellValue[m-1][j] + opt[m-1][j+1]]\;
   // general case
   for (int i\[=m-2; i>=0; i--]\) {
      for (int j\[=n-2; j>=0; j--]\) {
         // a choice! take better choice of down and right
         opt[i][j] = cellValue[i][j] + Math.\[max]\(\[opt[i+1][j]]\,
                                                    \[opt[i][j+1]]\);
      }
   }
   // value in top-left corner
   return \[opt[0][0]]\;
}

public static void main(String[] args) {
   int[][] testRoom =
    {{1, 1, 0, 2, 0},
     {0, 2, 0, 2, 0},
     {0, 1, 0, 0, 1},
     {3, 0, 0, 0, 1}};
   StdOut.println(maxPath(testRoom));
}
"""

description = r"""
<style> .ss {font-family:sans-serif} </style>
Nintendo's new minimalist video game controller only has two buttons,
<span class='ss'>down</span>
 and 
<span class='ss'>right</span>.
In the platform launch title Super Mario Multiverse,
every level is a rectangular grid of cells 
where Mario starts in the top-left corner. Some
cells of the grid have coins with a value, and other cells
are empty. The player has to press <span class='ss'>down</span>
 and <span class='ss'>right</span> in some order until
they get to the bottom-right corner, and their score is the sum total of
the value of 
all coins they hit along the way. Write a program
to find the maximum possible score for any level.

<p>
We represent a level by an <tt>int[][] cellValue</tt> where 
<tt>cellValue[i][j]</tt> is the cell <tt>i</tt>th from the top
and <tt>j</tt>th from the left (counting from 0, so the top-left cell is
<tt>[0][0]</tt>). A positive value means a coin with that value,
and a value of 0 means no coin is in that cell. For example, suppose
<tt>cellValue</tt> is the <tt>int[4][5]</tt> described by
<pre>
{{1, 1, 0, 2, 0},
 {0, 2, 0, 2, 0},
 {0, 1, 0, 0, 1},
 {3, 0, 0, 0, 1}}
</pre>
Mario has lots of possible paths. Remember he must go from the top-left
to the bottom-right using only steps <span class='ss'>right</span>
 (R) and <span class='ss'>down</span> (D).
If he goes D-D-D-R-R-R-R, he gets a score of 1+3+1=5. The path
R-D-R-R-D-R-D achieves a score of 1+1+2+2+1+1=8, which happens to be 
the maximum possible for this room.
<p>
Write a static method <code>int maxPath(int[][] cellValue)</code>
that computes the maximum score for a level given in this format. 
Use dynamic programming: compute, for each position, the best value 
you can get if you start in that cell.
"""

tests = r"""
testMain();
test("maxPath", (Object)new int[][]{{31, 2, 0}, {5, 26, 6}, {0, 4, 33}});
test("maxPath", (Object)new int[][]{{0, 2, 31}, {6, 26, 5}, {33, 4, 0}});
test("maxPath", (Object)new int[][]{{5, 3, 1}, {0, 3, 4}, {5, 3, 4}, {0, 2, 1}});
test("maxPath", (Object)new int[][]{{1, 2, 3, 4}});
test("maxPath", (Object)new int[][]{{1}, {2}, {3}, {4}});
test("maxPath", (Object)new int[][]{{1, 5, 8, 4, 1, 0, 2, 4, 0, 6}, {8, 3, 6, 8, 6, 4, 6, 2, 8, 0}, {3, 6, 0, 1, 1, 9, 8, 4, 2, 0}, {2, 0, 4, 4, 1, 9, 1, 3, 3, 3}, {2, 0, 4, 8, 9, 6, 5, 0, 8, 2}, {9, 5, 7, 6, 0, 0, 5, 4, 4, 3}, {7, 4, 9, 1, 4, 4, 1, 4, 8, 2}, {6, 1, 4, 7, 0, 8, 5, 8, 3, 8}, {9, 6, 0, 2, 3, 6, 6, 4, 5, 2}, {5, 0, 5, 1, 6, 1, 4, 3, 5, 0}});
"""
