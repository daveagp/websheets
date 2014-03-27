source_code = r"""
// this is just for reference. it is too slow for large n
public static long recursiveCat(int n) {
   if (n==0)
      return 1;
   long result = 0;
   for (int i=0; i<n; i++)
      result += recursiveCat(i)*recursiveCat(n-i-1);
   return result;
}

public static long dynamicCat(int n) {
   // intialize an array with indices from 0 to n
   long[] dp = \[new long[n+1]]\;
   // set the base case manually
  \[dp[0] = 1]\;

   // compute the rest of the sequence
   for (int k\[=1; k<=n; k++]\) {
\[
      dp[k] = 0; // not necessary, but for clarity
      for (int i=0; i<k; i++)
         dp[k] += dp[i]*dp[k-i-1];
]\
   }
   return dp[n];
}

public static void main(String[] args) {
   for (int i=0; i<=35; i++) {
      StdOut.println("The "+i+"th Catalan number is "+dynamicCat(i));
   }
}
"""

tests = r"""
test("dynamicCat", 0);
test("dynamicCat", 1);
test("dynamicCat", 2);
test("dynamicCat", 3);
test("dynamicCat", 4);
testMain();
"""

description = r"""
The <a href="http://en.wikipedia.org/wiki/Catalan_number">Catalan numbers</a>
are a fascinating sequence of integers that enumerate binary trees,
triangulations, valid parenthesizations, and other ubiquituous combinatorial
families. Their recursive definition is
<ul>
<li> $C_0 = 1$</li>
<li>for $\displaystyle n > 0, C_n = \sum_{i=0}^{n-1} (C_i \times C_{n-i-1})$</li>
</li>
</ul>
It is straightforward to write this as a recursive static method, 
provided as <tt>recursiveCat()</tt> for your reference below,
but it is too slow. Write a static method <tt>dynamicCat(n)</tt>
that computes the <i>n</i>th Catalan number using dynamic programming.
<p><i>Hint</i>: you will need nested loops.</p>
<p><i>Remark</i>: the code below is not optimal since it
re-computes the dynamic programming table over and over, but this is 
not a big deal for this exercise. There are also closed formulas
for Catalan numbers.</p>
"""
