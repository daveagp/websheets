description = r"""Write a program <tt>CountingSort</tt>, a client of <tt><a href="javascript:loadProblem('Clicker')">Clicker</a></tt>, 
that sorts a list of single-digit numbers.
On standard input, you will get a list of numbers like
<pre>
0 2 4 3 2 2 9 8 1 0
</pre>
Your program should use an array of ten <tt>Clicker</tt> objects to keep track of how many of each digit you saw. At the end, print out each number the number of times it was seen, in this case it would be
<pre>
0 0 1 2 2 2 3 4 8 9
</pre>
Remember that <tt>Clicker</tt> has the following API:
<ul>
<li><tt>public Clicker()&nbsp; // constructor, make new clicker with value 0</tt>
<li><tt>public void inc() // add one to the current value</tt>
<li><tt>public void dec() // subtract one from the current value</tt>
<li><tt>public int curr() // return the current value</tt>
</ul>
"""

source_code = r"""
public static void main(String[] args) {
   Clicker[] counts = \[new Clicker[10];]\ // array of Clickers

   // initialize them all
\[
   for (int i=0; i<10; i++) {
      counts[i] = new Clicker(); // initialize one
   }
]\

   // read each digit
   while (!StdIn.isEmpty()) {
      int digit = StdIn.readInt();
      // increment the right clicker
\[
      counts[digit].inc();
]\
   }

   // print out each number once for each time it was seen
   for (int i=0; i<10; i++) {
      while (counts[i].curr() > 0) {
         StdOut.print(i+" ");
         counts[i].dec();
      }
   }
   StdOut.println();
}
\hide[
public static class Clicker {
   // private instance variable(s) you will use are declared here:
   private int value; // currently held value
   
   // constructor, make new clicker with value 0
   public Clicker() {
      value = 0;
   }
   // add one to the current value
   public void inc() {
      value++;
   }
   
   // subtract one from the current value
   public void dec() {
      value--;
   }
   
   // return the current value
   public int curr() {
      return value;
   }
   
   // testing suite
   public static void main(String[] args) {
      Clicker myClick = new Clicker();
      StdOut.println(myClick.curr()); // should be 0
      myClick.inc();
      myClick.inc();
      StdOut.println(myClick.curr()); // should be 2
      myClick.dec();
      myClick.dec();
      myClick.dec();
      StdOut.println(myClick.curr()); // should be -1
   
      Clicker clickMore = new Clicker();
      StdOut.println(clickMore.curr()); // should be 0
      clickMore.inc();
      clickMore.inc();
      clickMore.inc();
      StdOut.println(clickMore.curr()); // should be 3
   
      // the next line won't work if you used static variables
      StdOut.println(myClick.curr()); // should still be -1
   }
}
]\
"""

#dependencies = ["Clicker"]

tests = r"""
testStdin = "0 2 4 3 2 2 9 8 1 0";
testMain();
testStdin = "6";
testMain();
testStdin = "3 4 5 5 5 4 3 4 4 5 3 4 3 5 4";
testMain();
testStdin = "0 1 3 6 0 0 7 4 3 5 6 7 8 7 4 3 2 2 3 4 5 6 8 9 8 5 1 1 1 1 2 2 3 6 8 7 9 0 0 5";
testMain();
"""
