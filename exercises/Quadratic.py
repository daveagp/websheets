description = """
Given command-line arguments
<code>b</code> and <code>c</code>, print out the 
roots of <code>x<sup>2</sup> + bx + c = 0</code>. They are given by
the formula
<div style='text-align:center'>
<img style='width:150px' src='exercises/Quadratic.png'></div>
If the <b>discriminant</b> <code>b<sup>2</sup>-4c</code> is 
negative, instead print out <code>There are no roots</code> and
if the discriminant is zero then print out only one root (since they
are the same). When there are two roots, print the <b>smaller</b> one first.
"""

source_code = r"""
public static void main(String[] args) {
   double b = Double.parseDouble(args[0]);
   double c = Double.parseDouble(args[1]);
\[
   double disc = (b*b-4*c);
   double root1 = (-b-Math.sqrt(disc))/2;
   double root2 = (-b+Math.sqrt(disc))/2;
   if (disc == 0)
      System.out.println(root1);
   else if (disc < 0)
      System.out.println("There are no roots");
   else {
      System.out.println(root1);
      System.out.println(root2);
   }
]\
}
"""

tests = """
oneRealPerLine = true;
testMain(-1, -1);
testMain(0, -2);
testMain(0, 2);
testMain(-4, 4);
testMain(randgen.nextInt(10)+10, randgen.nextInt(20));
"""
