source_code = r"""
public static void main(String[] args) {
   // the grader will pre-define an array of color names
\fake[

   String[] colors = ...; // e.g. new String[] {"red", "blue", "green"};
]\
\hide[
   String[] colors = new String[args.length];
   for (int i=0; i<args.length; i++) colors[i] = args[i];
]\

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

tester_preamble = r"""
class OurTestCase extends BasicTestCase {
   OurTestCase(String... S ) {super("main", new Object[]{S});}
   protected void describe() {
   System.out.print("Running your code on a test case");
}
}
"""

tests = r"""
  new OurTestCase("red", "green", "blue").execute();
  new OurTestCase("fuschia", "turquoise", "sienna", "vermilion").execute();
  new OurTestCase("a", "b", "c", "d", "e", "f", "g", "h").execute();
  new OurTestCase("monocolor").execute();
//   test("fourSwap", "fuschia", "turquoise", "sienna", "vermilion");
"""

description = r"""
This is an extension of the <b>SquareSwap</b> websheet.
Given an array <code>colors</code> of <code>n</code> strings,
move each string one position later in the array, except you
must move the one at the end to the start.
"""

