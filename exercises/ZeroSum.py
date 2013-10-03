description = r"""
<div>
Is it possible to assign + and - signs to the numbers
<pre>
1434 3243 343 5 293 3408 123 487 93 12 2984 29
</pre>
so that the sum is 0? With recursion, we can try all possible combinations
of + and - for each number to find out. We will in fact solve a slightly more
general problem with an arbitrary target.
Write a recursive static method
<pre>boolean canMake(int target, int[] nums, int startIndex)</pre>
which sees if any assignment of +/- signs to the numbers
<pre>nums[startIndex], nums[startIndex+1], &hellip;, nums[nums.length-1]</pre> gives the total 
<code>target</code>. To do this, it should:
<ul>
<li>return true if startIndex is the same 
as nums.length (we examined all numbers) and target is zero, this means we hit the target
for this guessed choice of signs</li>
<li>return false if startIndex is the same
as nums.length (we examined all numbers) and target is not zero, this means we missed the target
for this guessed choice of signs</li>
<li>otherwise, recursively call <code>canMake</code> on 
<code>target &pm; nums[startIndex]</code> with <code>startIndex+1</code>
and if return true if <i>either one</i> returns true
</li>
</ul>
(Using startIndex is simpler and more efficient than trying to
shrink the array
in every step.)
"""

source_code = r"""
public static boolean canMake(int target, int[] nums, int startIndex) {
\[
   // we've given a sign to all numbers
   if (startIndex == nums.length) {
      if (target == 0) 
         return true;  // hit the target
      else
         return false; // missed the target
   }

   // try both possibilities, propagating any hit
   if (canMake(target + nums[startIndex], nums, startIndex+1))
      return true;

   if (canMake(target - nums[startIndex], nums, startIndex+1))
      return true;

   // neither recursive call found a solution
   return false;
]\
}

public static void main(String[] args) {
   int[] testArr = {1434, 3243, 343, 5, 293, 3408, 123, 487, 93, 12, 2984, 29};
   // should print true because
   // -1434+3243-343-5-293-3408-123-487-93-12+2984-29 = 0
   StdOut.println(canMake(0, testArr, 0)); // true
   testArr = new int[] {1, 2};
   // no way to make zero
   StdOut.println(canMake(0, testArr, 0)); // false
}
"""

tests = r"""
testMain();
test("canMake", 0, new int[] {1, 1, 1, 1, 1, 1}, 0);
test("canMake", 0, new int[] {1, 1, 1, 1, 1, 1, 1}, 0);
test("canMake", 0, new int[] {1, 2, 3, 4, 5, 6}, 0);
test("canMake", 0, new int[] {1, 2, 3, 4, 5, 6, 7}, 0);
test("canMake", 0, new int[] {1000, 100000, 100, 111111, 10, 1, 10000}, 0);
test("canMake", 0, new int[] {9, 16, 25}, 0);
test("canMake", 0, new int[] {0, 0, 0}, 0);
test("canMake", 0, new int[] {1435, 3243, 343, 5, 293, 3408, 123, 487, 93, 12, 2984, 29}, 0);
"""
