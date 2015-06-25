attempts_until_ref = 0

description = r"""
Create a method <tt>printAll()</tt>
that prints out all names in the list, one per line.
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

void MonkeyChain::printAll() {
   // one possible approach: use a while loop
   Node* current = first; // start at beginning

   // if current isn't past the last node,
   while (\[current != NULL]\) {
      // print current node's name; then repeat loop w/next one
\[
      cout << current->name << endl;
      current = current->next;
]\
   }
}


int main() {
   MonkeyChain mc;
   mc.threeKongs();
   mc.printAll(); cout << endl;
   // double-check
   mc.printAll(); 
}

"""

tests = [["", []]]

