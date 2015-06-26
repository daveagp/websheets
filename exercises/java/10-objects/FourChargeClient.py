source_code = r"""
public class FourChargeClient {
    public static void main(String[] args) {
        double r = Double.parseDouble(args[0]);

        double cx = 0.5;
        double cy = 0.5;

        // construct four charges
        Charge c1 = new Charge(cx + r, cy,     1.0);    // east
        Charge c2 = \[new Charge(cx,     cy - r, 1.0)]\;    // south
        Charge c3 = \[new Charge(cx - r, cy,     1.0)]\;    // west
        Charge c4 = \[new Charge(cx,     cy + r, 1.0)]\;    // north

        // Compute potentials at (.25, .5)
        double px = 0.25;
        double py = 0.5;
        double v1 = c1.potentialAt(\[px, py]\);
        double v2 = \[c2.potentialAt(px, py)]\;
        double v3 = \[c3.potentialAt(px, py)]\;
        double v4 = \[c4.potentialAt(px, py)]\;

        // compute and output total potential
        double sum = \[v1 + v2 + v3 + v4]\;
        System.out.println("total potential:");
        System.out.println(sum);
    }
}
"""

description = r"""
Here is an API (Application Programming Interface) for charged particles.
<pre>
public class Charge
------------------------------------------------------------------------
Charge(double x0, double y0, double q0)  // location and charge
double potentialAt(double x, double y)   // potential at (x,y) due to charge
String toString()                        // string representation
</pre>

Write a program that takes a double value 
<tt>r</tt> from the command line, creates four
<tt>Charge</tt> objects that are each distance 
<tt>r</tt> from the center of the unit square (.5, .5), and
prints the potential at location (.25, .5) due 
to the combined four charges. All four
charges should have unit positive charge. See the illustration below.

<div style='text-align:center'><img src='exercises/FourChargeClient.ipe.png'></div>

<p>For example, <tt>java FourChargeClient 0.1</tt>
should print out
<pre>total potential:
1.5239509122751547E11
</pre>
"""

tests = r"""
testMain("0.1");
testMain("0.2");
testMain("1");
testMain("126");
testMain("0.25");
"""
