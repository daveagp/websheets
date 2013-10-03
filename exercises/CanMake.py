description = r"""
Is it possible to assign + and - signs to the numbers
<pre>
1434 3243 343 5 293 3408 123 487 93 12 2984
</pre>
so that the sum is 0? With recursion, we can try all possible combinations
of + and - for each number to find out. We need to solve a slightly more
general problem with an arbitrary target.
<div>
Write a recursive static method
<pre>boolean canGet(int target, int[] nums, int startIndex)</pre>
which sees if any assignment of +/- signs to <code>nums[startIndex],
nums[startIndex+1], ..., nums[nums.length-1]</code> gives the total 
<code>target</code>. To do this, it should:
<ul>
<li>return true if startIndex is the same 
as nums.length and target is zero, this means we hit the target
for this choice of signs</li>
<li>return false if startIndex is the same
as nums.length and target is zero, this means we missed the target
for this choice of signs</li>
<li>otherwise, recursively call <code>canGet</code> on both choices
<code>target &pm; nums[startIndex]</code> with <code>startIndex+1</code>
and if return true if <i>either one</i> returns true
</li>
</ul>
(We use startIndex because it is simpler than trying to change the array
in every step.)
"""

source_code = r"""
public static boolean canGet(int target, int[] nums, int startIndex) {
   if (startIndex == nums.length) {
      if (target == 0) 
         return true;
      else
         return false;
   }

   if (canGet(target + nums[startIndex], nums, startIndex+1))
      return true;

   if (canGet(target - nums[startIndex], nums, startIndex+1))
      return true;

   // neither recursive call found a solution
   return false;
}

public static void main(String[] args) {
   int[] testNums = {1434, 3243, 343, 5, 293, 3408, 123, 487, 93, 12, 2984};
   StdOut.println(canGet(0, testNums, 0));
}
"""




tests = r"""
testMain();
"""
