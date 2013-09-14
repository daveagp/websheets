description = r"""  
<p>Write a program to help you feed your friends at a pizza party.
There will be one command-line argument, the pizza's radius.
The area of the pizza is the square of the side length times &pi; (use
<code>Math.PI</code>). 
Assuming that each person needs to eat
100 cm<sup>2</sup> of pizza, compute the number of people you can feed,
rounded down to the nearest integer. For example, if you run 
<code>java PizzaCalculator 10</code> the area will be 314.15...
cm<sup>2</sup>, so <code>3</code> is the correct output. 
</p><p>Hint: use an explicit typecast at the end.</p>
"""

source_code = r"""
public class PizzaCalculator {
   public static void main(String[] args) {
      double PERSONAL_AREA = 100; // in square cm
\[
        double r = Double.parseDouble(args[0]); // radius
        double area = r*r*Math.PI;
        // cast to int rounds down:
        int people = (int) (area / 100); 
        System.out.println(people);
]\
   }
}
"""

tests = r"""
testMain("10.0");
testMain("100.0");
testMain("30.48");
testMain(randgen.nextInt(20000)*0.001+"");
"""
