source_code = r"""
public static int maxFits(int[] itemWeights, int capacity) {
   int numItems = itemWeights.length; // for convenience
\[
   // canMake[j][i]: can we make weight exactly j, using a subset of the
   //                items 0, 1, ..., i-1?
   boolean[][] canMake = new boolean[capacity+1][numItems+1];

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
   
   // find biggest weight <= capacity that can be made
   int result = 0;
   for (int j=0; j<=capacity; j++)
      if (canMake[j][numItems]) result = j;
   return result;
]\
}

public static void main(String[] args) {
   int[] testWeights = {5, 7, 10, 11};
   StdOut.println(maxFits(testWeights, 20)); // should be 18 (7+11)
   StdOut.println(maxFits(testWeights, 100)); // should be 33 (5+7+10+11)
   StdOut.println(maxFits(testWeights, 33)); // again, 33
   StdOut.println(maxFits(testWeights, 32)); // 28 (7+10+11)
   StdOut.println(maxFits(testWeights, 4)); // 0, nothing fits
}
"""

description = r"""
There are many variants of the <i>knapsack problem</i>. In this one,
you are given a list (an <tt>int</tt> array) of the weights of different
items in a house you are robbing. You also have a knapsack of a fixed
weight capacity. You want to choose some of the items and leave the others
so that 
<ol>
<li>
the total weight of the items
you select is as large as possible (steal as much as possible), but </li>
<li>
the total weight of the items you select
must not be larger than the capacity (or else the knapsack will rip).
</li>
</ol>

For example, if the item weights are
5, 7, 10, and 11, and the capacity is 20, then the largest weight you can
take is 18 (the item of weight 7 and the item of weight 11). No 
subset of these 4 items has total weight 19 or 20, so this is the best
you can do.

<p>
Write a static method <tt>int maxFits(int[] itemWeights, int capacity)</tt>
to compute the maximum weight you can steal. Several recursive approaches
are possible, but they are too slow. Instead, use a dynamic programming
approach that computes:
<ul>
<li>
If you steal either no items or only the first item,
for each weight <tt>i=0</tt> &hellip; <tt>capacity</tt>, is it possible to
steal a total weight of exactly i?
<li>
If you steal only a subset of the first two items,
for each weight <tt>i=0</tt> &hellip; <tt>capacity</tt>, is it possible to
steal a total weight of exactly i?
</li>
<li>Same as before, but only a subset of the first three items?</li>
<li>And so on, until you determine all weights that could be stolen
using any subset whatsoever of the items.</li>
</ul>
This can be computed using a 2D array of booleans, or a 1D array if
you are careful.
Finally,
report the maximum weight up to <tt>capacity</tt> that can be stolen.
<p>
Many variations of this problem are interesting. What if you can steal multiple copies of any
item?
What if each item
has a dollar value (unrelated to its weight) and you want to 
steal a maximum-value subset? What if there are both weight and size limits
(and each item's size is given)? How do you <i>find</i> the best subset? (See
 the next problem <a href="?group=KnapsackBacktrack">KnapsackBacktrack</a>.)

"""

tests = r"""
testMain();
test("maxFits", new int[]{2, 2, 2, 2, 2, 2}, 5);
test("maxFits", new int[]{1, 2, 4, 8, 16, 32, 64, 128}, 126);
test("maxFits", new int[]{7, 45, 21, 34, 99, 55}, 126);
test("maxFits", new int[]{621}, 126);
test("maxFits", new int[]{468, 246, 852, 456, 234, 567, 234, 159, 345, 258, 987, 333, 852, 234, 531, 963, 999, 642, 258, 741, 951, 456, 543, 357, 234, 456, 159, 876, 345, 234, 741}, 15000);
"""
