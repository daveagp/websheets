description="""
Write a program <code>ModularSqrt</code> that takes two command-line
arguments, <code>remainder</code> and <code>modulus</code>. 
It should print 
out all of the integers <code>i</code> between <code>0</code> and
<code>modulus-1</code>
with the property that <code>(i*i) % modulus</code> equals 
<code>remainder</code>, and a count of how many integers were found. 
Use the format shown in this example:
<code>java ModularSqrt 9 10</code> should print out
<pre>
3
7
2 square roots were found
</pre>
(There's no need to have correct English grammar: print <tt>1 square roots were found</tt> if
exactly 1 is found.)
"""

source_code = r"""
public class ModularSqrt {
   public static void main(String[] args) {
      int remainder = Integer.parseInt(args[0]);
      int modulus = Integer.parseInt(args[1]);
\[
        int count = 0;
        for (int i=0; i<modulus; i++) {
            if ((i*i) % modulus == remainder) {
                System.out.println(i);
                count += 1;
            }
        }
        System.out.println(count + " square roots were found");
]\
   }
}
"""

tests = """
testMain("9", "10");
testMain("3", "8");
testMain("5", "10");
testMain("1", "8");
testMain(randgen.nextInt(100)+"", "100");
testMain(randgen.nextInt(100)+"", "100");
"""
