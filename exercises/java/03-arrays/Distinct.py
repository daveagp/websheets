description = r"""
Write a program <code>Distinct</code> that takes an arbitrary
number of integer command-line arguments; it should print
<code>true</code> if they all have distinct values, and 
<code>false</code> otherwise."""

source_code = """
public class Distinct {
   public static void main(String[] args) {
 
      int N = args.length;    
         
      // convert each arg and store them in an array of integers
      int[] values =\[ new int[N] ]\;
      for (int i = 0; \[i < N]\; \[i += 1]\)
          \[ values[i] ]\ = Integer.parseInt(args[i]);    
        
      // are all of the pairs examined so far distinct?
      boolean result = true;

      // we'll examine each values[i] in the array 
      for (int i = 0; i < N; i++) {
         // we'll examine values[j] for each other j
         for (int j =\[i+1]\; \[j < N]\; \[j++]\) {
            // are they different or not?
            if (\[values[i] == values[j]]\) {
               result =\[false]\;
            }
         }
      }
         
      System.out.println(result);
   }
}
"""

tests = r"""
testMain(11, 23, -7, 0, 99, 5, 42);
testMain(2, 4, 6, 3, 6);
testMain(-3, -2, -1, -0, "+3", "+2", "+1", "+0");
testMain(2, 3, -3, -2);
testMain(126);
testMain();
"""
