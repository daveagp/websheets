description = r"""
<div>
Is it possible to assign + and &ndash; signs to the numbers
<pre>
1434 3243 343 5 293 3408 123 487 93 12 2984 29
</pre>
so that the sum is 0? With recursion, we can try all possible combinations
of + and &ndash; for each number to find out. There are $2^n$ ways to assign
+ or &ndash; signs to $n$ numbers, and recursion can accomplish this by making
two recursive calls (one for +, one for &ndash;) at each of $n$ levels.
Each branch of the recursive call tree will keep a running sum of the numbers
it has assigned signs so far. To implement this in Java,
write a recursive static method
<pre>boolean testAllCombs(int runningSum, int[] nums, int seenSoFar)</pre>
which tries every assignment of +/&ndash; signs to the numbers
<pre>nums[seenSoFar], nums[seenSoFar+1], &hellip;, nums[nums.length-1]</pre> and adds each sum of signed numbers to
<code>runningSum</code>. To do this and acheieve the overall goal, your method should:
<ol>
<li>return true if <tt>seenSoFar</tt> is the same 
as nums.length (we examined all numbers) and runningSum is zero, this means we got 0 as the sum
for the choice of signs on this leaf of the recursive call tree</li>
<li>return false if <tt>seenSoFar</tt> is the same
as nums.length (we examined all numbers) and runningSum is not zero, this means we missed 0 as the sum for the choice of signs
on this leaf of the recursive call tree</li>
<li>otherwise, recursively call <code>testAllCombs</code> on 
<code>runningSum &pm; nums[seenSoFar]</code> and with <code>seenSoFar+1</code> in place of <code>seenSoFar</code>;
return true if <i>either one</i> of the two recursive calls returns true
</li>
</ol>
Using seenSoFar is analogous to the level of a fractal, to control 
the recursion depth and ensure that each number is included (as + or 
&ndash;) exactly once
in each branch.
Other than this, how is this recursive method used to achieve our goal?
To test if <tt>int[] arr</tt> has a zero-sum signing, 
we make an initial call with <tt>testAllCombs(0, arr, 0)</tt>.
If there is some 0-sum signing, then some call
on the bottom level (seenSoFar = nums.length) has a runningSum of 
0 and by rule 1, returns
true. By rule 2, this true value is propagated up the recursive call tree 
to return true at the top.
"""

source_code = r"""
public static boolean testAllCombs(int runningSum, int[] nums, int seenSoFar) {
\[
   // we've given a sign to all numbers
   if (seenSoFar == nums.length) {
      if (runningSum == 0) 
         return true;  // hit the runningSum
      else
         return false; // missed the runningSum
   }

   // try both possibilities, propagating any hit
   if (testAllCombs(runningSum + nums[seenSoFar], nums, seenSoFar+1))
      return true;

   if (testAllCombs(runningSum - nums[seenSoFar], nums, seenSoFar+1))
      return true;

   // neither recursive call found a solution
   return false;
]\
}

public static void main(String[] args) {
   int[] testArr = {1434, 3243, 343, 5, 293, 3408, 123, 487, 93, 12, 2984, 29};
   // should print true because
   // -1434+3243-343-5-293-3408-123-487-93-12+2984-29 = 0
   StdOut.println(testAllCombs(0, testArr, 0)); // true
   testArr = new int[] {1, 2};
   // no way to make zero
   StdOut.println(testAllCombs(0, testArr, 0)); // false
}
"""

tests = r"""
testMain();
test("testAllCombs", 0, new int[] {1, 1, 1, 1, 1, 1}, 0);
test("testAllCombs", 0, new int[] {1, 1, 1, 1, 1, 1, 1}, 0);
test("testAllCombs", 0, new int[] {1, 2, 3, 4, 5, 6}, 0);
test("testAllCombs", 0, new int[] {1, 2, 3, 4, 5, 6, 7}, 0);
test("testAllCombs", 0, new int[] {1000, 100000, 100, 111111, 10, 1, 10000}, 0);
test("testAllCombs", 0, new int[] {9, 16, 25}, 0);
test("testAllCombs", 0, new int[] {0, 0, 0}, 0);
test("testAllCombs", 0, new int[] {1435, 3243, 343, 5, 293, 3408, 123, 487, 93, 12, 2984, 29}, 0);
test("testAllCombs", 0, new int[] {1434, 3253, 343, 5, 293, 3408, 123, 487, 93, 22, 2984, 29}, 0);
"""
