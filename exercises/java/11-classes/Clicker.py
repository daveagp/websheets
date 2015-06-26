description = r"""
When you go in to a bar or place with a seating capacity, often
the person at the front has a "clicker" to keep track of how many 
people go in or out. Build a <tt>Clicker</tt> class to do this; it should 
have the following API.
<ul>
<li><tt>public Clicker()&nbsp; // constructor, make new clicker with value 0</tt>
<li><tt>public void inc() // add one to the current value</tt>
<li><tt>public void dec() // subtract one from the current value</tt>
<li><tt>public int curr() // return the current value</tt>
</ul>
Negative clicker values should be permitted.
"""

source_code = r"""
// private instance variable(s) you will use are declared here:
\[
private int value; // currently held value
]\

// constructor, make new clicker with value 0
public Clicker() {
\[
   value = 0;
]\
}
// add one to the current value
public void inc() {
\[
   value++;
]\
}

// subtract one from the current value
\[
public void dec() {
   value--;
}
]\

// return the current value
\[
public int curr() {
   return value;
}
]\

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
"""
tests = r"""
saveAs = "attendance";
testConstructor();
testOn("attendance", "curr");
testOn("attendance", "inc");
testOn("attendance", "inc");
testOn("attendance", "curr");
testOn("attendance", "dec");
testOn("attendance", "curr");
testOn("attendance", "curr");
testMain();
"""
