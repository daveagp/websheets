source_code = r"""
public static \[long]\ factorial(\[int n]\) {
   // base case
   if (\[n == 0]\) 
      return \[1]\;

   // reduction step
   // note that n! = n * (n-1) * ... * 2 * 1 = n * ((n-1) * ... * 2 * 1)
   return \[n]\ * factorial(\[n-1]\);
}

public static void main(String[] args) {
   StdOut.println(factorial(4));  // should be 24
   StdOut.println(factorial(10)); // should be 3628800
   StdOut.println(factorial(20)); // watch for overflow. what return type?
}"""

description = r"""
Write a recursive method <code>factorial(n)</code>
that returns n &times; (n-1) &times; (n-2) &times; &hellip; &times; 3 &times; 2 &times 1. For example, <code>factorial(4)</code> should return 24 since that is the value of 1 &times; 2 &times; 3 &times; 4.
"""

tests = r"""
testMain();
test("factorial", 1);
test("factorial", 6);
test("factorial", 11);
"""
