classname = "MonkeyChain"

description = r"""
Create a method <tt>addStart(String newName)</tt> 
that adds a new Node, containing this name, 
at the start of the list.
"""

source_code = r"""
// structure of items in list
private class Node {
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

// add a new node, containing this name, at the start of the list
public void addStart(String newName) {
   Node newFirst = new Node(newName);
\[
   Node oldFirst = first;
   first = newFirst;
   first.next = oldFirst;
   // there's also a slightly trickier 2-line solution
]\
}
"""

tests = r"""
saveAs = "mc";
testConstructor();
testOn("mc", "threeKongs");
testOn("mc", "addStart", "King Kong");
testOn("mc", "printAll");
testOn("mc", "addStart", "Koko");
testOn("mc", "printAll");
"""
