source_code = r"""
// helper class
private class Node {
   private String value; // value in this item
   private Node next;    // reference to next item
   private Node(String v, Node n) { // constructor
      value = v;
      next = n;
   }
}

private Node first;    // reference to first item

// construct a new empty list
public LinkIt() {
   first = null;
}

// insert new string at start
public void insertFirst(String s) {
   first = new Node(s, first);
}

// convert to string, separated by spaces
public String toString() {
   StringBuilder sb = new StringBuilder();
   Node curr = first;
   while (curr != null) {
      sb.append(curr.value + " ");
      curr = curr.next;
   }
   return sb.toString();
}

// reverse the items in the list
public void reverse() {
\[
   Node prev = null;
   Node curr = first;
   while (curr != null) {
      Node newcurr = curr.next;
      curr.next = prev;
      prev = curr;
      curr = newcurr;            
   }
   first = prev;
]\
}

// delete the kth item from the list, where the first is k=1
// throw RuntimeException if list is empty or index is invalid (k < 1)
public void deleteKth(int k) {
   // deleting from an empty list or from index less than 1 never makes sense
   if (\[first == null || k < 1]\)
      throw new RuntimeException("Invalid index!");
   
   // now delete the item, and throw an exception if the item doesn't exist
\[
   if (k == 1) {
      // this is the only case where first changes
      first = first.next;
   }
   else {
      Node curr = first;
      // access the (k-1)st node
      for (int i=1; i<k-1; i++) {
         if (curr == null)
            throw new RuntimeException("Invalid index!");
         curr = curr.next;
      }
      // link (k-1)st to (k+1)st
      if (curr == null || curr.next == null)
         throw new RuntimeException("Invalid index!");
      curr.next = curr.next.next;
   }
]\
}

// helper method for testing
// values[0] in first node, then values[1], etc
public static LinkIt fromStrings(String[] values) {
   LinkIt result = new LinkIt();
   for (int i=values.length-1; i>=0; i--)
      result.insertFirst(values[i]);
   return result;
}

public static void main(String[] args) {
   String[] testWords1 = {"is", "this", "code", "working", "well?"};
   LinkIt test1 = fromStrings(testWords1);
   test1.reverse();
   StdOut.println(test1); // should be: well? working code this is
   test1.reverse();
   StdOut.println(test1); // should be: is this code working well?

   LinkIt test2 = fromStrings(new String[]{"mull", "over", "null", "well"});
   test2.deleteKth(3);
   StdOut.println(test2); // should be: mull over well
   test2.deleteKth(1);
   StdOut.println(test2); // should be: over well
   test2.deleteKth(2);
   StdOut.println(test2); // should be: over
}
"""

tests = r"""
testMain();
saveAs = "linkit";
test("fromStrings", (Object)new String[]{"sesquipedalian"});
testOn("linkit", "reverse");
testOn("linkit", "toString");
saveAs = "linkit";
testConstructor();
testOn("linkit", "reverse");
testOn("linkit", "toString");
saveAs = "linkit";
test("fromStrings", (Object)("this sentence has five words".split(" ")));
expectException = true;
testOn("linkit", "deleteKth", 0);
saveAs = "linkit";
test("fromStrings", (Object)("this sentence has five words".split(" ")));
expectException = true;
testOn("linkit", "deleteKth", 6);
saveAs = "linkit";
test("fromStrings", (Object)("this sentence has five words".split(" ")));
testOn("linkit", "deleteKth", 4);
testOn("linkit", "toString");
testOn("linkit", "deleteKth", 2);
testOn("linkit", "toString");
testOn("linkit", "deleteKth", 2);
testOn("linkit", "toString");
testOn("linkit", "deleteKth", 1);
testOn("linkit", "toString");
testOn("linkit", "deleteKth", 1);
testOn("linkit", "toString");
expectException = true;
testOn("linkit", "deleteKth", 1);
"""

description = r"""<i>(Booksite 4.3)</i>
The class <tt>LinkIt</tt> is a basic example of a linked list that contains <tt>String</tt> items,
including a <tt>toString()</tt> method that is already complete.
We have left two methods blank for you to fill in.
<ul>
<li>The method <tt>reverse()</tt> should reverse 
the items of the list. 
For example, if the list currently contains the 4 items "is", "this", "code", "working", "well?" then
<tt>reverse()</tt> should alter the list to "well?", "working", "code", "this", "is".
You should change the links (<tt>next</tt> variables) but avoid changing the <tt>value</tt> variables
(it makes coding it harder).
For maximum challenge, don't use <tt>new Node()</tt> in this method.
</li>
<li>The method <tt>deleteKth(int k)</tt> should delete
the kth item from the list, where the first is k=1. Your code should throw a <tt>RuntimeException</tt>
if k is invalid. 
For example, if the list currently contains the 4 items "link", "think", "sink", "wink", then
<tt>deleteKth(2)</tt> should alter the list to "link", "think", "wink".
</li>
</ul>
See the test main for more examples.
"""
