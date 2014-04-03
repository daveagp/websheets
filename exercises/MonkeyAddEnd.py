classname = "MonkeyChain"

description = r"""
Create a method <tt>addEnd(String newName)</tt> 
that adds a new Node, containing this name, 
at the <b>end</b> of the list.
"""

source_code = r"""
// structure of items in list
class Node {
   // each node knows "next" node
   Node next;
   // and stores a value
   String name;
   // constructor for nodes
   Node(String initialName) {
      name = initialName;
   }
}

// beginning of the list, initially empty
private Node first = null;

// a demo to create a length-3 list
public void threeKongs() {
   first = new Node("DK Sr.");
   first.next = new Node("DK");
   first.next.next = new Node("DK Jr.");
}

// a working copy of this method from MonkeyTraverse will be included
// it prints all Strings in the linked list, from first to last
public void printAll() // ... method body not shown
\hide[
{
   Node current = first; // start at beginning

   // if current isn't past the last node,
   while (current != null) {
      // println current node's name; then repeat loop w/next one
      System.out.println(current.name);
      current = current.next;
   }
}
]\
// add a new node, containing this name, at the end of the list
public void addEnd(String newName) {
   Node newLast = new Node(newName);

   // loop like printAll(), but stops *just before* 
   // the end, then adds the new node
\[
   if (first == null) {
      first = newLast;
   }
   else {
      Node current = first;
      while (current.next != null) {
         current = current.next;
      }
      current.next = newLast;
   }
]\
}
   
public static void main(String[] args) {
   MonkeyChain mc = new MonkeyChain();
   mc.threeKongs();
   mc.addEnd("Bubbles");
   mc.printAll();
}
"""

tests = r"""
testMain();
saveAs = "mc";
testConstructor();
testOn("mc", "addEnd", "Curious George");
testOn("mc", "addEnd", "Bubbles");
testOn("mc", "printAll");
"""
