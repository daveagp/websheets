description = r"""
Read 3 integer values from the command line and print them
in ascending order. For example, <code>java ThreeSort 8 2 5</code>
should print out 
<pre>
2 5 8
</pre>
Hint: use functions from the <code>Math</code> library,
and a little algebra."""

source_code = r"""
public class ThreeSort {
    public static void main(String[] args) {
\[
        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        int c = Integer.parseInt(args[2]);
        int smallest = Math.min(a, Math.min(b, c));
        int biggest = Math.max(a, Math.max(b, c));
        // the main trick: the original sum equals the sorted sum
        int middle = a + b + c - smallest - biggest;
        System.out.print(smallest + " ");
        System.out.print(middle + " ");
        System.out.println(biggest);
]\
    }
}
"""

tests = r"""
for (int[] a : new int[][]{
{1, 2, 3},
{3, 1, 2},
{3, 2, 1},
{1, 3, 2},
{2, 1, 3},
{2, 3, 1}}) 
testMain(a[0]*5+randgen.nextInt(5)+"", 
a[1]*5+randgen.nextInt(5)+"", 
a[2]*5+randgen.nextInt(5)+"");
testMain("8", "8", "5");
testMain("8", "5", "8");
testMain("5", "8", "8");
testMain("9", "4", "4");
testMain("4", "9", "4");
testMain("4", "4", "9");
testMain("10", "10", "10");
"""
