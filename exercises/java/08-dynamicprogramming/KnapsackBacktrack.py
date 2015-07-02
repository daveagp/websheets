source_code = r"""
// void method, prints out value and description of best solution
public static void printBest(int[] itemWeights, int capacity) {
   int numItems = itemWeights.length; // for convenience
   // canMake[j][i]: can we make weight exactly j, using a subset of the
   //                items 0, 1, ..., i-1?
   boolean[][] canMake = new boolean[capacity+1][numItems+1];

   /****************************************************************/
   /*** hidden code here correctly fills out canMake[][] for you ***/
   /****************************************************************/

\hide[
   canMake = new boolean[capacity+1][numItems+1];

   // if no items are allowed (i==0), the only weight we can make is 0
   canMake[0][0] = true;

   for (int i=1; i<=numItems; i++) {
      for (int j=0; j<=capacity; j++) {
         // if we can get a total weight of j using a subset of the first
         // i items, we can do the same with a subset of the first i-1,
         // by simply not taking the ith item
         canMake[j][i] = canMake[j][i-1];

         // if we take the ith item, to make weight j, the subset of items
         // up to i must have weight j-itemWeights[i-1]
         if (j >= itemWeights[i-1] && canMake[j-itemWeights[i-1]][i-1])
            canMake[j][i] = true;
      }
   }
]\   
   // find biggest weight <= capacity that can be made
   int optWeight = 0;
   for (int j=0; j<=capacity; j++)
      if (canMake[j][numItems]) optWeight = j;
   StdOut.print("Optimal weight is " + optWeight);
   
   // keep track of which items we must take in the optimal solution
   boolean[] useItem = new boolean[numItems]; // initially all false
   
   // repeatedly reduce the number of items and see if we must use
   // last item or not. update optWeight to the weight we must select
   // from amongst the remaining items.
   while (numItems > 0) { 
      // canMake[optWeight][numItems] is true. what caused it?
      // it must be that either (a) canMake[optWeight][numItems-1] is true,
      // or (b) canMake[optWeight-itemWeights[numItems-1]][numItems-1] is true.
      // track back to whichever one of those is true.
      if (\[canMake[optWeight][numItems-1]]\) { // case (a)
         // we will *not* use item numItems-1
         useItem[numItems-1] = \[false]\;
         // optWeight does not change
      }
      else { // case (b)
         // we have to use item numItems-1
         \[useItem[numItems-1] = true]\;
         // reduce optWeight by that item's weight
         optWeight -= \[itemWeights[numItems-1]]\;
      }
      // we've now reduced the bactracking to a smaller problem
      numItems--;
   }
   // at the end, optWeight and numItems should be 0, and useItem is filled.

   StdOut.print(" and optimal solution uses: ");
   for (int i=0; i<useItem.length; i++) {
      if (useItem[i]) StdOut.print(itemWeights[i]+" ");
   } 
   StdOut.println();
}

public static void main(String[] args) {
   int[] testWeights = {5, 7, 10, 11};
   printBest(testWeights, 20); // should be 18 (7+11)
   printBest(testWeights, 100); // should be 33 (5+7+10+11)
   printBest(testWeights, 33); // again, 33
   printBest(testWeights, 32); // 28 (7+10+11)
   printBest(testWeights, 4); // 0, nothing fits
}
"""

description = r"""
This is a continuation of the problem
<a href="javascript:websheets.load('java/08-dynamicprogramming/Knapsack')">Knapsack</a>
(read it first). 
Like in that problem, you will 
write a static method that takes two arguments,
<tt>int[] itemWeights, int capacity</tt> representing item weights
you can choose, and the maximum weight you can steal.
But this time, we ask you to <i>find</i> and print the best solution, rather
than just the weight of it. 

<p>
To help accomplish this, we pre-compute an array <tt>canMake[][]</tt>,
 a <tt>boolean[capacity+1][numItems+1]</tt> so that <tt>canMake[j][i]</tt>
 is true if and only if we can make weight exactly <tt>j</tt> using
 a subset of the items indexed <tt>0, 1, &hellip; i-1</tt>.
<p>
Determine which items are members of this best solution.
Print out their weights in the order they appear in the input.
(We'll only test the input on instances with unique solutions,
so your outputs should exactly match ours.)
"""

tests = r"""
testMain();
test("printBest", new int[]{1, 2, 4, 8, 16, 32, 64, 128}, 126);
test("printBest", new int[]{7, 45, 21, 34, 99, 55}, 126);
test("printBest", new int[]{621}, 126);
test("printBest", new int[]{468, 246, 852, 456, 234, 567, 234, 159, 345, 258, 987, 333, 852, 234, 531, 963, 999, 642, 258, 741, 951, 456, 543, 357, 234, 456, 159, 876, 345, 234, 741}, 15000);
"""
