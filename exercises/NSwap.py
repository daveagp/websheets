source_code = r"""
public static void main(String[] args) {
   // the grader will pre-define an array of color names
   String[] colors = \fake[...; // e.g. new String[] {"red", "blue", "green"};]\ \hide[args.clone();]\ 
   int n = colors.length; // for convenience

   System.out.println("Before n-swapping:");
   for (int i=0; i<n; i++)
      System.out.println("color " + i + " is " + colors[i]);
 
   // your swapping code here:
\[
   String tmp = colors[n-1];
   for (int i=n-1; i>=1; i--)
      colors[i] = colors[i-1];
   colors[0] = tmp;
]\
   System.out.println("After n-swapping:");
   for (int i=0; i<n; i++)
      System.out.println("color " + i + " is " + colors[i]);
}
"""

tests = r"""
HTMLdescription = "Running with <tt>colors[] = {\"red\", \"green\", \"blue\"}</tt>";
testMain("red", "green", "blue");

HTMLdescription = "Running with <tt>colors[] = {\"fuschia\", \"turquoise\", \"sienna\", \"vermilion\"}</tt>";
testMain("fuschia", "turquoise", "sienna", "vermilion");

HTMLdescription = "Running with <tt>colors[] = {\"a\", \"b\", \"c\", \"d\", \"e\", \"f\", \"g\", \"h\"}</tt>"; 
testMain("a", "b", "c", "d", "e", "f", "g", "h");

HTMLdescription = "Running with <tt>colors[] = {\"monocolor\"}</tt>";
testMain("monocolor");
"""

description = r"""
This is an extension of the <a href='?group=SquareSwap'>SquareSwap</a> websheet.
Given an array <code>colors</code> of <code>n</code> strings,
move each string one position later in the array; and, you
must move the one at the end to the start.
"""

