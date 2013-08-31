source_code = r"""
public static void main(String[] args) {
   int inputNum = \[Integer.parseInt(args[0])]\; // save the input
   System.out.println(\[inputNum * inputNum]\); // print its square
}
"""

tests = r"""
   testMain("4");
   testMain("-12");
   testMain("11111");
"""

description = r"""
Write a program that takes one command-line argument,
which is an integer, and prints its square.
<br>For best style, don't call <code>Integer.parseInt()</code> more than once.
"""
