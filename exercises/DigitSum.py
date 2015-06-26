description = r"""
Write a program that takes an integer command-line argument,
and outputs the sum of its digits, by using <tt>while</tt> loop."""

source_code = r"""
public static void main(String[] args) {
   int n = Integer.parseInt(args[0]);
   int total = 0; // running sum
   
   while (\[n > 0]\) {
\[
      total = total + n%10;
      n = n/10;
]\
   }

   System.out.println(total);
}
"""

tests = """
testMain("123");
testMain("2014");
testMain("7");
"""
