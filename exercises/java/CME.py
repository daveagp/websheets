imports = ["java.util.Set", "java.util.TreeSet"]

description = r"""
Define a method <tt>addReverses(Set&lt;String&gt; words)</tt> that takes 
a set of strings, and adds to that set the reverse of every string in the set.
For example, if you call it on a set containing <tt>"HI"</tt> and <tt>"MOM"</tt>
then after your method executes, it should contain <tt>"HI"</tt>, <tt>"IH"</tt> and <tt>"MOM"</tt>
(only once, since that's all a <tt>Set</tt> can contain).
<p>
A partial solution is given below, but it throws a <tt>ConcurrentModificationException</tt>. You have to fix it.
"""

source_code = r"""
public class CME {
   public static void addReverses(Set<String> words) {
\[
      // we will put the reverses in a new place for now
      // while we iterate through the main set
      java.util.HashSet<String> tmp = new java.util.HashSet<String>();
      for (String s : words) 
         tmp.add(new StringBuffer(s).reverse().toString());
     
      // now that we're done iterating through 'words', add to it
      for (String s : tmp) 
         words.add(s);
\show:
      for (String s : words) { // for each string in the set 

         // a one-liner to compute the reverse of a string
         String sReverse = new StringBuffer(s).reverse().toString();

         // add it to our set
         words.add(sReverse);
      }
]\
   }

   // test client: e.g. "java CME HI MOM" should print out on 3 lines HI IH MOM
   public static void main(String[] args) {
      Set<String> testSet = new TreeSet<String>();
      for (int i=0; i < args.length; i++)
         testSet.add(args[i]); 

      addReverses(testSet);

      for (String s : testSet)
         System.out.println(s);
   }
}
"""

tests = r"""
testMain("HI", "MOM");
testMain("MADAM", "IM", "ADAM");
testMain("NOW", "SIR", "A", "WAR", "IS", "WON");
"""
