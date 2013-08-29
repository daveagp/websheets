classname = "MaxThree"

code = r"""
public static \[int]\ max3(\[int a, int b, int c]\) {
\[
   int result = Math.max(a, b);
   result = Math.max(result, c);
   return result;
]\
}
"""

tests = r"""
   test("max3", 3, 5, 7);
   test("max3", 7, 5, 3);
   test("max3", 2, 2, 1);
"""

description = r"""
Write a function <code>max3()</code> that returns 
the largest of three integers."""
