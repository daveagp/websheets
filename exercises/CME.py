imports = ["java.util.Set;", "java.util.TreeSet;"]
description = r"""
Define a method <tt>addReverses(Set&lt;String&gt; ss)</tt> that takes 
a set of strings, and adds to that set the reverse of every string in the set.
For example, if you call it on a set containing <tt>"HI"</tt> and <tt>"MOM"</tt>
then after your method executes, it should contain <tt>"HI"</tt>, <tt>"IH"</tt> and <tt>"MOM"</tt>
(only once, since that's all a <tt>Set</tt> can contain).
<p>
A partial solution is given below, but it throws a <tt>ConcurrentModificationException</tt>. You have to fix it.
"""

source_code = r"""
public class CME {
   public static void addReverses(Set<String> ss) {
\[
      // we will put the reverses in a new place for now
      // while we iterate through the main set
      TreeSet<String> tmp = new TreeSet<String>();
      for (String s:ss) 
         tmp.add(new StringBuffer(s).reverse().toString());
     
      // now that we're done iterating through ss, add to it
      for (String s:tmp) 
         ss.add(s);
]\\default[
      for (String s : ss) { // for each string in the set 

         // a simple way to compute the reverse of a string
         String reverseOfS = new StringBuffer(s).reverse().toString();

         // add it to our set
         ss.add(reverseOfS);
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
