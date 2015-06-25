attempts_until_ref = 0

description = r"""
Create a method <tt>addStart(string newName)</tt>
that adds a new Node, containing this name,
at the start of the list.
"""

lang = "C++"

source_code = r"""
#include <iostream>
#include <string>
using namespace std;

// structure of items in list
struct Node {
   Node* next;  // each node knows "next" node
   string name; // and stores a value
   Node(string initialName);  // constructor for nodes
};

Node::Node(string initialName) {name = initialName; next = NULL;}

class MonkeyChain {
   public:
      MonkeyChain();
      void threeKongs();
      void printAll();
      void addStart(string newName); // NEW!
   private: 
      Node* first;
};

MonkeyChain::MonkeyChain() {first = NULL;}

// a demo to create a length-3 list
void MonkeyChain::threeKongs() {
   first = new Node("DK Sr.");
   first->next = new Node("DK");
   first->next->next = new Node("DK Jr.");
}

// we'll provide a working copy of printAll for you 
void MonkeyChain::printAll() // ... { method body not shown }
\hide[
{
   // one possible approach: use a while loop
   Node* current = first; // start at beginning

   // if current isn't past the last node,
   while (current != NULL) {
      // print current node's name; then repeat loop w/next one
      cout << current->name << endl;
      current = current->next;
   }
}
]\

// add a new node, containing this name, at the start of the list
void MonkeyChain::addStart(string newName) {
   Node* newFirst = new Node(newName);
\[
   Node* oldFirst = first;
   first = newFirst;
   first->next = oldFirst;
   // there's also a slightly trickier 2-line solution
]\
}


int main() {
   MonkeyChain mc;
   mc.threeKongs();
   mc.addStart("King Kong");
   mc.printAll(); cout << endl;
   mc.addStart("Bubbles");
   mc.printAll(); cout << endl;

   mc = MonkeyChain(); // test 2: insert into empty list
   mc.addStart("Test 2 Monkey");
   mc.printAll(); 
   // TO-DO: clean up memory
}

"""

tests = [["", []]]

