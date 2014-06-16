description = r"""
Egg cartons each hold exactly 12 eggs. Write a program which reads an integer
number of eggs as an argument, then prints out two numbers: how many cartons
can be filled by these eggs, and how many eggs will be left over. For example,
the output corresponding to <code>java Eggsactly 27</code> is
<pre>
2 3
</pre>
since 27 eggs fill 2 cartons, leaving 3 eggs left over. <i>Hint:</i> use 
<code>%</code>.
"""

tests = """
testMain("27");
testMain(randgen.nextInt(100)+"");
testMain(randgen.nextInt(10)*12+"");
testMain(randgen.nextInt(10)*12+1+"");
testMain(randgen.nextInt(10)*12+11+"");

"""

source_code = """
public static void main(String[] args) {
   int n = Integer.parseInt(args[0]); // number of eggs
   System.out.print(\[n / 12]\); // number of filled 12-egg cartons
   System.out.print(" "); 
   System.out.println(\[n % 12]\); // number of eggs left over
}
"""
