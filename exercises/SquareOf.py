source_code = r"""
public static void main(String[] args) {
   int inputNum =\[Integer.parseInt(args[0])]\; // convert the input
   System.out.println(\[inputNum * inputNum]\); // print its square
}
"""

tests = r"""
   testMain("4");
   testMain("-12");
   testMain("11111");
"""

description = r"""
Write a program that takes a whole number as a command-line argument,
and prints its square. For example, <pre>java SquareOf 10</pre> should print:
<pre>100</pre>
"""

epilogue = r"""
Note that it's a little better to call
<code>Integer.parseInt(args[0])</code>
only once, rather than twice.
It's a minor point, but avoiding redundant
function calls becomes a lot more important
when you have a more complex program.
"""
