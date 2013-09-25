description = r"""
Write a program <code>Squish</code> that reads in a sequence of integers 
from standard input and prints out the integers, but 
removing repeated values that appear consecutively. For example, if the input is
<pre>1 2 2 1 5 1 1 7 7 7 7 1 1 1 1 1 1 1 1 1</pre>your program should print out 
<pre>1 2 1 5 1 7 1</pre>
For simplicity, don't add a space or newline at the end. You may assume there is at least one input."""

source_code = r"""
public static void main(String[] args) {
\[
   int val = StdIn.readInt();
   StdOut.print(val);
   while (!StdIn.isEmpty()) {
      int next = StdIn.readInt();
      if (val != next) {
         val = next;
         System.out.print(" "+val);
      }
   }
]\
}
"""

tests = r"""
testStdin = "3 4 4 5 6 7 7 8 3 4 5 6 5 5 5 5 5 3";
testMain();
testStdin = "1 2 2 1 5 1 1 7 7 7 7 1 1 1 1 1 1 1 1 1";
testMain();
testStdin = "3";
testMain();
testStdin = "3 3 3 3 3";
testMain();
testStdin = "1 1 2 5 8 13 21 0 -0 -5";
testMain();
"""
