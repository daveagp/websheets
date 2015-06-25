description = r"""
Using a <tt>while</tt> loop, create a method <tt>printAll()</tt> that prints all names in the linked list, 
starting with the first one. It should print each name on a separate line.
"""

source_code = r"""
public class MonkeyChain {
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

    public void printAll() {
        // one possible approach: use a while loop
        Node current = first; // start at beginning

        // if current isn't past the last node,
        while (\[current != null]\) {
            // println current node's name; then repeat loop w/next one
\[
            System.out.println(current.name);
            current = current.next;
]\
        }
    }

    public static void main(String[] args) {
       MonkeyChain mc = new MonkeyChain();
       mc.threeKongs();
       mc.printAll();
    }
}
"""

tests = r"""
//testMain();

saveAs = "mc";
testConstructor();

testOn("mc", "threeKongs");
testOn("mc", "printAll");

quietOnPass = true;
title = "Calling <tt>mc.printAll()</tt> <b>again</b> to see if list was destroyed.";
testOn("mc", "printAll");
"""

classname = "MonkeyChain"
