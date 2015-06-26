attempts_until_ref = 0

description = r"""
Using recursion,
create a method <tt>reverse()</tt>
that reverses the elements in a linked list.
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
      void printAll(); // not shown
      void reverse();
   private: 
      Node* helpReverse(Node* n); // reverse and return pointer to new start
      Node* first;
};
\hide[
void MonkeyChain::printAll() {
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

MonkeyChain::MonkeyChain() {first = NULL;}

// a demo to create a length-3 list
void MonkeyChain::threeKongs() {
   first = new Node("DK Sr.");
   first->next = new Node("DK");
   first->next->next = new Node("DK Jr.");
}

// private helper: reverse list trailing from n (n moves to end), 
// return new front
Node* MonkeyChain::helpReverse(Node* n) {
\[
   if (n == NULL) {
      return NULL;
   }
   else if (n->next == NULL) {
      return n; // nothing to reverse
   }
   else {
      Node* tmp = helpReverse(n->next); // now n->next is at end
      n->next->next = n; // move n past that end
      n->next = NULL; // n is the end, fix its link
      return tmp; // same new front
   }
]\
}

void MonkeyChain::reverse() {
\[
   first = helpReverse(first);
]\
}


int main() {
   MonkeyChain mc;
   mc.threeKongs();
   mc.printAll(); cout << endl;
   mc.reverse();
   mc.printAll();   
}

"""

tests = [["", []]]


verboten = ["for", "while", "do"]
