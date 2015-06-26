description = r"""
Input 3 integer command line arguments whose numbers are in ascending order.
Print the average of the 3 integers. 
Then print true if the average of the 3 numbers is greater than the middle 
number. Print false otherwise. For example, <code>java AboveAverage 2 5 8</code>
should print out 
<pre>
Average is: 5.0
false
</pre>
"""

source_code = r"""
public class AboveAverage {
      public static void main(String[] args) {
\[
          int a = Integer.parseInt(args[0]);
          int b = Integer.parseInt(args[1]);
          int c = Integer.parseInt(args[2]);
          double avg = (a + b + c) / 3.0;
          System.out.println("Average is: " + avg);
          boolean isGreater = (avg > b);
          System.out.println(isGreater);
]\
      }
}
"""

tests = r"""
for (int[] a : new int[][]{
{1, 2, 3},
{3, 5, 7},
{3, 5, 9},
{1, 2, 3},
{2, 10, 30},
{2, 3, 6}}) 
testMain(a[0]*5+randgen.nextInt(5)+"", 
a[1]*5+randgen.nextInt(5)+"", 
a[2]*5+randgen.nextInt(5)+"");
testMain("5", "8", "8");
testMain("4", "4", "9");
testMain("3", "5", "9");
testMain("10", "10", "10");
expectException = true;
testMain("10.0", "10", "10");
expectException = true;
testMain("10", "10.0", "10");
expectException = true;
testMain("10", "10", "10.0");
"""
