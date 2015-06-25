description = """
<p>
Given command-line arguments
<code>b</code> and <code>c</code>, print out the 
roots of <code>x<sup>2</sup> + bx + c = 0</code>. They are given by
the formula
$$\Large (-b \pm \sqrt{b^2-4c})/2$$
If the <b>discriminant</b> <code>b<sup>2</sup>-4c</code> is 
negative, instead print out <code>There are no roots</code>.
When there are two roots, print the <b>smaller</b> one first.
When the discriminant is zero*, print out the single number <code>-b/2</code>:
both roots have this value.
<p>
*: Because of floating-point inaccuracy, it's better to check if the discriminant is very close to zero, say within 10<sup>-6</sup>. You could use a condition like <code>Math.abs(disc) < 1E-6</code>. 
"""

source_code = r"""
public static void main(String[] args) {
   double b = Double.parseDouble(args[0]);
   double c = Double.parseDouble(args[1]);
\[
   double disc = (b*b-4*c);

   if (Math.abs(disc) < 1E-6) {
      // avoid square roots: sqrt(disc) could cause "not a number" if disc < 0
      System.out.println(-b/2);
   }
   else if (disc < 0) {
      System.out.println("There are no roots");
   }
   else {
      double root1 = (-b-Math.sqrt(disc))/2;
      double root2 = (-b+Math.sqrt(disc))/2;
      System.out.println(root1);
      System.out.println(root2);
   }
]\
}
"""

tests = """
testMain(-1, -1);
testMain(0, -2);
testMain(0, 2);
testMain(-4, 4);
testMain(-0.1, 0.0025);
testMain(randgen.nextInt(10)+10, randgen.nextInt(20));
"""
