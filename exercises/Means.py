description = r"""
Write a program <code>Means</code> that takes a command-line input
<code>N</code> and then reads in <code>N</code> double values from
standard input. It should print out several means (averages) of the numbers,
which we 
define below; let <i>x</i><sub>1</sub>, <i>x</i><sub>2</sub>,
&hellip; <i>x</i><sub>N</sub> denote the numbers.  
<ul>
<li>the arithmetic mean is (<i>x</i><sub>1</sub> + <i>x</i><sub>2</sub> + &hellip; + <i>x</i><sub>N</sub>)/N </li>
<li>the geometric mean is (<i>x</i><sub>1</sub> &times; <i>x</i><sub>2</sub> &times; &hellip; &times; <i>x</i><sub>N</sub>)<sup>1/N</sup> </li>
<li>the harmonic mean is N/(1/<i>x</i><sub>1</sub> +  1/<i>x</i><sub>2</sub> + &hellip; + 1/<i>x</i><sub>N</sub>)</li>
</ul> 
Print all three of these means out.
In order that the means are well-defined, you may assume the inputs
are positive. We will provide the output format for you to round to three decimal places. For example, <code>java Means 5</code> with standard input
<pre>1.0 2.0 3.0 4.0 5.0</pre> should output
<pre>
Arithmetic mean: 3.000
Geometric mean: 2.605
Harmonic mean: 2.190
</pre>"""

tests = r"""
testStdin = "1.0 2.0 3.0 4.0 5.0";
testMain(5);
testStdin = "4 8 15 16 23 42\nThese are the numbers from LOST\n(Your program should not read this, only the N numbers.)"; 
testMain(6);
testStdin = "126 126 126";
testMain(3);
"""

source_code = r"""
public static void main(String[] args) {
\[
   int N = Integer.parseInt(args[0]);
   double sum = 0; // running sum
   double prod = 1; // running product
   double recipsum = 0; // running sum of reciprocals

   for (int i=0; i<N; i++) {
      double val = StdIn.readDouble();
      sum += val;
      prod *= val;
      recipsum += 1/val;
   }
]\
   double arithmetic = \[sum/N]\;
   double geometric = \[Math.pow(prod, 1.0/N)]\;
   double harmonic = \[N/recipsum]\;

   StdOut.printf("Arithmetic mean: %.3f\n", arithmetic);
   StdOut.printf("Geometric mean: %.3f\n", geometric);
   StdOut.printf("Harmonic mean: %.3f\n", harmonic);
}"""
