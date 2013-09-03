source_code = r"""
\hide[
public static void squareSwap(String top, String bottom,
  String left, String right) {
  String[] args = new String[0];
]\
\fake[
public static void main(String[] args) {
   // the grader will pre-define 4 variables with color names
   String top = ...; // e.g. "red" or "blue", etc
   String bottom = ...;
   String left = ...;
   String right = ...;
]\

   System.out.println("Before rotation, top = " + top + ", bottom = " + bottom
               + ", left = " + left + ", right = " + right + ".");
   // Now, write code to swap the variable values correctly,
   // to reflect a clockwise 90-degree rotation being performed.
   // The code you add doesn't need to print anything.
\[
String tmp = top;
top = left;
left = bottom;
bottom = right;
right = tmp;
]\
   System.out.println("After rotation, top = " + top + ", bottom = " + bottom
               + ", left = " + left + ", right = " + right + ".");
}
"""

tester_preamble = r"""
class OurTestCase extends BasicTestCase {
   OurTestCase(String s1, String s2, String s3, String s4) {super("squareSwap", new Object[]{s1, s2, s3, s4});}
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
Swap the 4 variables indicated in the code to match the change
that occurs when we rotate a square 90 degrees clockwise.
<br> Hint: If you get stuck, see how to swap two variables in Web Exercise 2 from
<a href="http://introcs.cs.princeton.edu/java/12types/">booksite Section 1.2</a>. One of the important ideas from there needs to be used here.
<div><img style='height:150px;margin-top:5px' src='exercises/FourSwap.ipe.png'></div>
"""
