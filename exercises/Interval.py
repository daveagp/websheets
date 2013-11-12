description = r"""
Create a class to model intervals of the real line. Each interval has a minimum and a maximum, and contains
all of the real numbers between its minimum and its maximum.
(This kind of object has applications in
geometry, scheduling, and text editing.)
For example, the interval [3, 6] from 3 to 6 contains 3, &pi;, 5, and 6, but it does not contain 6.21.
(All intervals we deal with will include both endpoints.) 
Your code must produce the following API:
<pre>
public Interval(double lo, double hi) // construct inveral from lo to hi; but 
                                      // throw a RuntimeException if lo > hi
String toString()                  // return text representation, e.g. "[3, 6]"
boolean contains(double x)         // does this interval contain x?
boolean intersects(Interval other) // do these intervals contain a common point?
boolean subsetOf(Interval other)   // is this interval a subset of the other?
boolean supersetOf(Interval other) // is this interval a superset of the other?
</pre>
For <tt>subsetOf</tt>, the containment doesn't have to be strict. For example
[3, 4] is a subset of [3, 4.5], and every interval is a subset of itself.
"""

source_code = r"""
// instance variables
\[
double lo; // minimum value in this Interval
double hi; // maximum value in this Interval
]\
// constructor
\[
public Interval(double lo, double hi) {
   if (hi < lo)
     throw new RuntimeException("Empty interval!");

   // copy data from constructor parameters to instance vars
   this.lo = lo;
   this.hi = hi;
}
]\
// text representation
public String toString() {
   // use something like String.format("%.3g", ...);
\[
   return String.format("[%.3g, %.3g]", lo, hi);
]\
}
// other instance methods
\[
// is x in this interval?
public boolean contains(double x) {
   return x >= lo && x <= hi;
}

// do these intervals intersect?
public boolean intersects(Interval other) {
   if (this.lo > other.hi) return false; // this is to the right of other
   if (other.lo > this.hi) return false; // other is to the right of this
   return true; // otherwise, they intersect
}

// is other a subset of this interval?
public boolean subsetOf(Interval other) {
   return other.lo <= lo && other.hi >= hi;
}
]\
// use "this" to just reuse previous logic
public boolean supersetOf(Interval other) {
   return other.subsetOf(this);
}

// test client
public static void main(String[] args) {
   // counting years BCE to avoid negative signs
   Interval mesozoic = new Interval(66E6, 252E6);
   Interval jurassic = new Interval(145E6, 201E6);
   StdOut.println("The Mesozoic is " + mesozoic.toString());
   StdOut.println("The Jurassic is " + jurassic); // implicit toString
   StdOut.println(mesozoic.intersects(jurassic)); // true
   StdOut.println(jurassic.subsetOf(mesozoic));   // true
}
"""

tests = r"""
testMain();
saveAs = "persianEmpire"; testConstructor(-550.0, 651.0);
testOn("persianEmpire", "toString");
testOn("persianEmpire", "contains", 126.0);
saveAs = "tangDynasty"; testConstructor(623.0, 907.0);
testOn("tangDynasty", "contains", 126.0);
testOn("persianEmpire", "intersects", var("tangDynasty"));
testOn("persianEmpire", "subsetOf", var("persianEmpire"));
testOn("persianEmpire", "intersects", var("persianEmpire"));
saveAs = "alfredTheGreat"; testConstructor(849.0, 899.0);
testOn("alfredTheGreat", "contains", 899.0);
testOn("alfredTheGreat", "supersetOf", var("tangDynasty"));
testOn("alfredTheGreat", "subsetOf", var("tangDynasty"));
testOn("alfredTheGreat", "supersetOf", var("persianEmpire"));
testOn("persianEmpire", "intersects", var("alfredTheGreat"));
expectException = true; testConstructor(2013.0, -2013.0);
"""
