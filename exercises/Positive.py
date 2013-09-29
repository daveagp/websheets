source_code = r"""

public static \[boolean]\ \[isPositive]\(\[int]\ \[x]\) {
\[
   return (x > 0);
]\
}

// basic tests
public static void main (String[] args) {
   StdOut.println("126 is positive? " + isPositive(126));
   StdOut.println("-126 is positive? " + isPositive(-126));
   StdOut.println("0 is positive? " + isPositive(0));
}
"""

description = r"""
Write a class <code>Positive</code> with a static method <code>isPositive()</code>
that takes one integer argument, and returns the boolean value <code>true</code> if 
the argument is positive, and <code>false</code> otherwise."""

tests = r"""
testMain();
test("isPositive", randgen.nextInt(100)+1);
test("isPositive", -randgen.nextInt(100)-1);
"""
