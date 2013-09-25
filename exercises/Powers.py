description = r"""
Write a program <code>Powers</code> that takes in two numbers from standard input:
a double <code>k</code> and an integer <code>N</code>. It should print out the
first <code>k</code> powers of <code>N</code> (using the format given in the template).
For example running with standard input <code>2.0 5</code> should output
<pre>
2.0000
4.0000
8.0000
16.000
32.000
</pre>
"""


source_code = r"""
public static void main(String[] args) {
\[
   double k = StdIn.readDouble();
   int N = StdIn.readInt();
]\
   for (\[int i=1; i<=N; i++]\) {
\[
      double power = Math.pow(k, i); // not very efficient :(
]\
      // you must define a variable called power somewhere
      StdOut.printf("%.5g\n", power); // print to 5 decimal places
   }
}"""

tests = r"""
oneRealPerLine = true;
testStdin = "2.0 8";
testMain();
testStdin = "1.1 3";
testMain();
testStdin = "-1 4";
testMain();
testStdin = "126 10";
testMain();
"""
