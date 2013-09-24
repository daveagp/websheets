description = r"""
Write a program <code>NOrdered</code> that takes any
number of integer command-line arguments. If they are in strictly
increasing or strictly descreasing order, it should print <code>true</code>.
Otherwise it should print <code>false</code>.
"""

source_code = r"""
public static void main(String[] args) {
   int n = args.length; // for convenience
\[
   int[] vals = new int[n];
   for (int i=0; i<n; i++)
      vals[i] = Integer.parseInt(args[i]);
   
   // check for increasing
   boolean increasing = true;
   for (int i=0; i<n-1; i++) // one shorter than usual
      increasing = increasing && (vals[i] > vals[i+1]);

   // check for decreasing
   boolean decreasing = true;
   for (int i=0; i<n-1; i++) // one shorter than usual
      decreasing = decreasing && (vals[i] < vals[i+1]);

   System.out.println(increasing || decreasing);
]\
}
"""

tests = r"""
testMain(1, 2, 6);
testMain(100, 25, 10, 5, 1);
testMain(9, 999, 99);
testMain(10, 15, 15, 20);
testMain(1, 2, 3, 4, 5, 4, 3, 2, 1);
testMain(10, 100);
testMain(10, 10);
testMain(1, 10, 2, 11, 3, 12);
testMain(126);
"""
