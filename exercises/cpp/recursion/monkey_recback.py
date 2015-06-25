attempts_until_ref = 0

description = r"""
Using recursion,
create a method <tt>printBackwards()</tt>
that prints out all names in the list, one per line, <b>in reverse order</b>.
You will need to declare and define a helper function.
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
      void printBackwards();
      void addStart(string newName); // implementation not shown
   private: 
\[
      void helpPrintBackwards(Node* n);
]\
      Node* first;
};
\hide[
// add a new node, containing this name, at the start of the list
void MonkeyChain::addStart(string newName) {
   Node* newFirst = new Node(newName);
   Node* oldFirst = first;
   first = newFirst;
   first->next = oldFirst;
   // there's also a slightly trickier 2-line solution
}
]\

MonkeyChain::MonkeyChain() {first = NULL;}

// a demo to create a length-3 list
void MonkeyChain::threeKongs() {
   first = new Node("DK Sr.");
   first->next = new Node("DK");
   first->next->next = new Node("DK Jr.");
}

// private helper
void MonkeyChain::helpPrintBackwards(Node* n) {
\[
   if (n != NULL) {
      helpPrintBackwards(n->next);
      cout << n->name << endl;
   }
]\
}

void MonkeyChain::printBackwards() {
\[
   helpPrintBackwards(first);
]\
}


int main() {
   MonkeyChain mc;
   mc.threeKongs();
   mc.printBackwards(); cout << endl;

   // test on 5 monkeys
   mc.addStart("King Kong");
   mc.addStart("Bubbles");
   mc.printBackwards(); 
}

"""

tests = [["", []]]


verboten = ["for", "while", "do"]
