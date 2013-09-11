description = """
Given command-line arguments
<code>b</code> and <code>c</code>, print out the 
roots of <code>x<sup>2</sup> + bx + c = 0</code>. They are given by
the formula
<div><img src='Quadratic.png'></div>
If the <b>discriminant</b> <code>b<sup>2</sup>-4c</code> is 
negative, instead print out <code>There are no roots</code> and
if the discriminant is zero then print out only one root (since they
are the same).
"""

source_code = """
public static void main(String[] args) {
   double b = Double.parseDouble(args[0]);
   double c = Double.parseDouble(args[1]);
   double disc = (b*b-4*c);
   if 
}
"""

tests = """
"""
