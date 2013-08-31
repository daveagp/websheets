source_code = r"""
\hide[
public static void fourSwap(String top, String bottom,
  String left, String right) {
]\
\fake[
// the grader will pre-define 4 variables with color names
String top = ...; // e.g. "red" or "blue", etc
String bottom = ...;
String left = ...;
String right = ...;
]\

System.out.println("Before rotation, top = " + top + ", bottom = " + bottom
               + ", left = " + left + ", right = " + right + ".");
// now, write code to re-arrange the values correctly,
// when a clockwise 90-degree rotation is performed
// you code doesn't need to print anything, just change the
// values of the variables
\[
String tmp = top;
top = left;
left = bottom;
bottom = right;
right = tmp;
]\
System.out.println("After rotation, top = " + top + ", bottom = " + bottom
               + ", left = " + left + ", right = " + right + ".");
\hide[
}
]\
"""

tester_preamble = r"""
class OurTestCase extends BasicTestCase {
   OurTestCase(String s1, String s2, String s3, String s4) {super("fourSwap", new Object[]{s1, s2, s3, s4});}
   protected void describe() {
   System.out.println("We set "
   +code("top = " + repr(args[0]))+", "
   +code("bottom = " + repr(args[1]))+", "
   +code("left = "+repr(args[2]))+", "
   +"and "+code("right = "+repr(args[3]))+". Then we ran your code");
}
}
"""

tests = r"""
  new OurTestCase("red", "green", "blue", "yellow").execute();
  new OurTestCase("fuschia", "turquoise", "sienna", "vermilion").execute();
//   test("fourSwap", "fuschia", "turquoise", "sienna", "vermilion");
"""

description = r"""
Complete the code so that the variables are correct after the
square is rotated clockwise by 90 degrees.
<div><img style='height:150px;margin-top:5px' src='exercises/FourSwap.ipe.png'></div>
"""
