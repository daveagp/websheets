classname = "FourSwap"

code = r"""
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

// now, write code to re-arrange the values correctly,
// when a clockwise 90-degree rotation is performed

\[String tmp = top;
top = left;
left = bottom;
bottom = right;
right = tmp;
]\
StdOut.println("After rotation, top = " + top + ", bottom = " + bottom
               + ", left = " + left + ", right = " + right + ".");
\hide[
}
]\
"""

tests = r"""
   test("fourSwap", "red", "green", "blue", "yellow");
   test("fourSwap", "fuschia", "turquoise", "sienna", "vermilion");
"""

description = r"""
Complete the code so that the variables are correct after the
square is rotated clockwise by 90 degrees.
"""
