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
String tmp = top; // save old value in new temp variable
top = left;       // write over old value
left = bottom;    // write over old value
bottom = right;   // write over old value
right = tmp;      // complete the swap using saved value
]\
   System.out.println("After rotation, top = " + top + ", bottom = " + bottom
               + ", left = " + left + ", right = " + right + ".");
}
"""

tests = r"""
title = "We set <tt>top = red, bottom = green, left = blue, right = yellow</tt> and ran your code";
test("squareSwap", "red", "green", "blue", "yellow");

title = "We set <tt>top = fuschia, bottom = turquoise, left = sienna, right = vermilion</tt> and ran your code";
test("squareSwap", "fuschia", "turquoise", "sienna", "vermilion");
"""

description = r"""
Swap the 4 variables indicated in the code to match the change
that occurs when we rotate a square 90 degrees clockwise.
<br> Hint: If you get stuck, see how to swap two variables in Web Exercise 2 from
<a href="http://introcs.cs.princeton.edu/java/12types/">booksite Section 1.2</a>. One of the important ideas from there needs to be used here.
<div><img style='height:150px;margin-top:5px' src='http://cscircles.cemc.uwaterloo.ca/websheets/exercises/java/00-intro/FourSwap.ipe.png'></div>
"""

#hide_class_decl = True
