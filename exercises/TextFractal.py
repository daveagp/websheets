source_code = r"""
public static void printRuler(int n) {
   // return if we're in the base case. 
\[
   if (n == 0) return;
]\
   // otherwise, make two recursive calls, with a length-n line in between
   printRuler(\[n-1]\);
\[
   for (int i=0; i<n; i++)
      StdOut.print('-');
   StdOut.println(); 
   printRuler(n-1);
]\
}

public static void main(String[] args) {
   // just a test
   printRuler(3);
}
"""

tests = r"""
test("printRuler", 1);
test("printRuler", 2);
test("printRuler", 3);
test("printRuler", 4);
test("printRuler", 5);
"""

description = r"""
A ruler's pattern makes shorter marks each time you divide the length
in half. Mimic this with a static method <code>printRuler(n)</code> that
prints a ruler like this whose longest line has length <code>n</code>.
For example <code>printRuler(2)</code> should print out
<pre>
-
--
-
</pre>
and <code>printRuler(3)</code> should print out
<pre>
-
--
-
---
-
--
-
</pre>
"""
