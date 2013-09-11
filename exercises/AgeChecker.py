description = r"""
Write a program <code>AgeChecker</code>
 that reads an integer from input, representing
someone's age. If the age is 18 or larger, print out <pre>You can vote</pre>
If the age is 
between 0 and 17 inclusive, print out <pre>Too young to vote</pre>
If the age is less than 0, print out <pre>You are a time traveller</pre>
"""

tests = r"""
testMain("-1");
testMain("0");
testMain("17");
testMain("18");
testMain(20+randgen.nextInt(100)+"");
testMain(-1-randgen.nextInt(100)+"");
testMain(10+randgen.nextInt(6)+"");
"""
 
source_code = r"""
public static void main(String[] args) {
   int age = Integer.parseInt(args[0]);        
\[
      if (age < 0)
         System.out.println("You are a time traveller");
      else if (age < 18)
         System.out.println("Too young to vote");
      else
         System.out.println("You can vote");
]\
}
"""
