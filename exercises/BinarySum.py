description = r"""
Write a recursive static method <code>binaryDigitSum(n)</code> that
takes a nonnegative integer <code>n</code> and
<ul>
<li>if <code>n</code> is zero, returns zero</li>
<li>if <code>n</code> is odd, returns one plus <code>binaryDigitSum(n/2)</code>
</li>
<li>if <code>n</code> is even and not zero, returns <code>binaryDigitSum(n/2)
</code></li>
"""

source_code = r"""
// sum of the binary digits of n
\[public static int binaryDigitSum(int n) {
   if (n==0) return 0;

   if (n%2 == 1) // is n odd?
      return 1 + binaryDigitSum(n/2);

   // n is even and positive
   return binaryDigitSum(n/2);
}
]\

public static void main(String[] args) {
   StdOut.println(binaryDigitSum(5)); // should be 2, 5 is 101
   StdOut.println(binaryDigitSum(25)); // should be 3, 25 is 11001
}
"""
tests = r"""
testMain();
test("binaryDigitSum", 0);
test("binaryDigitSum", 1);
test("binaryDigitSum", 2);
test("binaryDigitSum", 3);
test("binaryDigitSum", 4);
test("binaryDigitSum", 126);
test("binaryDigitSum", 255);
test("binaryDigitSum", 256);
"""
