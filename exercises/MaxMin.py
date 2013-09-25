description = r"""
Write a program <code>MaxMin</code> that reads in an arbitrary
number of integers from standard input, and prints out the
minimum and maximum values"""

source_code = r"""
public class MaxMin {
   public static void main(String[] args) {
    
      // first value read initializes min and max
      int max =\[ StdIn.readInt() ]\;
      int min =\[ max ]\;
    
      // read in the data, keep track of min and max
      while (\[! StdIn.isEmpty() ]\) {
         int value = StdIn.readInt();
\[
         min = Math.min(min, value);
         max = Math.max(max, value);
]\
      }
    
      // output
      StdOut.println("max = " + max + "   min = " + min);
   }
}"""

tests = r"""
testStdin = "23 45 17 56 32\n89 10 53 32 34\n16";
testMain();
testStdin = "1 2 3 4 5";
testMain();
testStdin = "-1 -2 -3 -4 -5";
testMain();
testStdin = "126";
testMain();
"""
