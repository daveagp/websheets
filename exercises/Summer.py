description = r"""
Write a program <code>Summer</code> whose API contains
two overloaded (same-name) public static methods
<ul>
<li>
<code>sum(double[] a)</code>,
which returns the sum of the elements of <code>a</code>
</li>
<li>
<code>sum(int[] a)</code>,
which returns the sum of the elements of <code>a</code>
</li>
</ul>
"""

source_code = r"""
\[
public static double sum(double[] a) {
   double result = 0;
   for (int i=0; i < a.length; i++)
      result += a[i]; 
   return result;
}

public static int sum(int[] a) {
   int result = 0;
   for (int i=0; i < a.length; i++)
      result += a[i]; 
   return result;
}
]\
// basic tests
public static void main(String[] args) {
   StdOut.println(sum(new int[]{1, 2, 6}));
   StdOut.println(sum(new double[]{Math.PI, Math.E, Math.log(2)}));
}
"""

tests = r"""
oneRealPerLine = true;
testMain();
test("sum", (Object)new int[]{-5, -4, -3, -2, -1});
test("sum", (Object)new double[]{1E10, 1E11, 1E12});
"""
