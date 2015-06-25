source_code = r"""
public static void main(String[] args) {
   // read point coordinates from input
   int x = Integer.parseInt(\[args[0]]\);
\[
   int y = Integer.parseInt(args[1]);
]\
        
   // compute distance
\[
   double dist = Math.sqrt(x*x + y*y);
]\

   // print output
\[
   System.out.print("distance from ");
   System.out.print("(" + x + ", " + y + ")");
   System.out.println(" to (0, 0) = " + dist);
]\
}"""

description = r"""
(<a href="http://introcs.cs.princeton.edu/java/12types/">Web Exercise 1.2.1.</a>)
Write a program <tt>Distance.java</tt> which, 
given two integer command-line arguments, <tt>x</tt>
and <tt>y</tt>, computes the Euclidean distance from the point 
$(x, y)$ to the origin $(0, 0)$ using the formula
$$\textrm{distance} = \sqrt{x^2 + y^2}.$$

Do NOT use <tt>Math.pow(x, 2)</tt> to compute $x^2$. (It is too slow 
for many applications.) 

<p>Output your answer like the following:
<tt>java Distance 3 4</tt> should output
<pre style='text-align: center'>
distance from (3, 4) to (0, 0) = 5.0
</pre>
"""

tests = r"""
testMain("3", "4");
testMain("0", "0");
testMain("1000", "1000");
testMain("-1064", "1710");
"""
