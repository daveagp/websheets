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
Write a program that takes an integer number as a command-line argument,
and prints its square. For example, <pre>java SquareOf 10</pre> should print:
<pre>100</pre>
Use simple multiplication rather than using exponents.
"""

epilogue = r"""
<i>Note:</i> It's better to call
<code>Integer.parseInt(args[0])</code>
once rather than twice; 
avoiding redundant
function calls becomes more important
for more complex programs. (Here it also helps readability.)
"""
