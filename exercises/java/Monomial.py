description = r"""
Create a class Monomial that represents functions of the form $x \mapsto ax^b$, 
where <i>a</i> is a real number and <i>b</i> is an integer. It should have the following API:
<pre>
public Monomial(double coeff, int exp)// constructor, create a new monomial a*x^b
public double evaluate(double x)      // return the value of a*x^b
public String toString()              // return the String "a*x^b"
</pre>
We will test your code by running a pre-defined <tt>main</tt> method 
that takes a list of command-line arguments and evaluates them on several
monomials.
"""

source_code = r"""
// private instance variables
\[
private double a;
private int b;
]\

// public methods (API)
\[
// constructor, create a new monomial a*x^b
public Monomial(double coeff, int exp) {
   a = coeff;
   b = exp;
}

// return the value of a*x^b
public double evaluate(double x) {
   return a*Math.pow(x, b);
}

// return the String "a*x^b"
]\ 
\[public String]\ toString() {
   // use the rounding to 3 decimals indicated below
   return String.format("%.3f", \[a]\) + \["*x^" + b]\;
}

// test main: print out a table of several monomials' values, evaluated for
// different values of x specified as command-line arguments
public static void main(String[] args) {
   Monomial negativeX = new Monomial(-1.0, 1);
   Monomial squaredX = new Monomial(1.0, 2);
   Monomial half = new Monomial(0.5, 0);
   Monomial scaledRecip = new Monomial(-12.6, -1);
   
   // print out a header row. toString() is called implicitly!
   StdOut.printf("%12s%12s%12s%12s%14s\n", 
                 "x", negativeX, squaredX, half, scaledRecip); 

   for (int i=0; i<args.length; i++) {
      // print out a row of the table
      double x = Double.parseDouble(args[i]);
      StdOut.printf("%12.3f%12.3f%12.3f%12.3f%14.3f\n", 
                     x, 
                     negativeX.evaluate(x), 
                     squaredX.evaluate(x),
                     half.evaluate(x),
                     scaledRecip.evaluate(x)); 
   }
}
"""

tests = r"""
saveAs = "mono";
testConstructor(4.0, 3);
testOn("mono", "toString");
testOn("mono", "evaluate", 4.5);
testMain(1, 2, 6, 126);
"""
