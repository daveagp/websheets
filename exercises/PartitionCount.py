description = r"""
How many ways can you distribute <i>n</i> different objects into <i>k</i>
nonempty bundles? Traditionally this number is denoted by 
$\displaystyle\left\{{n \atop k}\right\},$ for example $\displaystyle\left\{{4 \atop 2}\right\}=7$ because 4 
objects &mdash; call them A, B, C, D &mdash; can be distributed 
into two bundles 
in the seven ways
<div style='text-align:center'>A-BCD B-ACD C-ABD D-ABC AB-CD AC-BD AD-BC</div>
To determine the value of these numbers, we will use the recurrence relation
<ul>
<li>for $\displaystyle n,k>0, \left\{{n \atop k}\right\} 
= k\left\{{n-1 \atop k}\right\}+\left\{{n-1 \atop k-1}\right\}$</li>
<li>with the base cases $\displaystyle\left\{{0\atop 0}\right\}=1$ and
for $\displaystyle n>0, 
\left\{{n \atop 0}\right\}=0$ and for 
$\displaystyle k>0, \left\{{0 \atop k}\right\}=0$
</li>
</ul>
Write a static method <code>bundleWays(n, k)</code> that uses
dynamic programming to compute $\displaystyle\left\{{n \atop k}\right\}.$
Using a recursive method will be too slow.
"""

source_code = r"""
public static long bundleWays(int n, int k) {
\[
   long[][] dp = new long[n+1][k+1];
   
   // base cases are automatically set to zero, except this one:
   dp[0][0] = 1;

   // compute numbers from bottom-up
   for (int i=1; i<=n; i++) {
      for (int j=1; j<=k; j++) {
         dp[i][j] = j*dp[i-1][j] + dp[i-1][j-1];
      }
   }

   return dp[n][k];
]\
}

public static void main(String[] args) {
   for (int n=0; n<=5; n++) {
      for (int k=0; k<=n; k++)
         StdOut.printf("{%d %d} = %-3d  ", n, k, bundleWays(n, k));
      StdOut.println();
   }
}
"""

tests = r"""
test("bundleWays", 4, 2);
testMain();
test("bundleWays", 25, 2);
test("bundleWays", 25, 9);
test("bundleWays", 25, 10);
test("bundleWays", 25, 11);
test("bundleWays", 25, 20);
"""

 
