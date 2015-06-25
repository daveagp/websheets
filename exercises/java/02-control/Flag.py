description = r"""
The official flag of COS 126 is a right triangle pointing up-left,
with <code>n</code> rows and <code>n</code> columns, made out of
backslashes, where <code>n</code> is a command-line argument.
Write a program to print it out for any positive integer <code>n</code>:
for example
<code>java Flag 5</code> should print out
<pre>
\\\\\
\\\\
\\\
\\
\
</pre>
This tests two things: escaping in strings, and nested loops.
"""

source_code = r"""
public static void main(String[] args) {
   int n = Integer.parseInt(args[0]);
   for (int i=0; \[i<n; i++]\) {
      for (int j\[=0; j<n-i; j++]\) {
         System.out.\[print("\\")]\;
      }
      System.out.\[println()]\;
   }
}
"""

tests = r"""
testMain("5");
testMain(randgen.nextInt(10)+10+"");
testMain("1");
"""
