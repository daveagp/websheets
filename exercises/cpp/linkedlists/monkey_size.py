attempts_until_ref = 0

description = r"""
Create a member function <tt>int size()</tt>
that tells the user how many items are in the list.
<p>Of course, you could do this by adding and maintaining a data member, 
but for this exercise, you're not allowed to do this.
"""

lang = "C++"

source_code = r"""
\hide[
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
      void addStart(string newName);
      bool isEmpty();
      int size();
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

// add a new node, containing this name, at the start of the list
void MonkeyChain::addStart(string newName) {
   Node* newFirst = new Node(newName);
   Node* oldFirst = first;
   first = newFirst;
   first->next = oldFirst;
   // there's also a slightly trickier 2-line solution
}

// add a new node, containing this name, at the start of the list
bool MonkeyChain::isEmpty() {
   return first == NULL;
}

]\
int MonkeyChain::size() {
\[
   int count = 0;
   Node* loc = first;
   while (loc != NULL) {
      count++;
      loc = loc->next;
   }
   return count;
]\
}

int main() {
   MonkeyChain mc;
   cout << mc.size() << endl;
   mc.addStart("King Kong");
   cout << mc.size() << endl;
   mc.addStart("Bubbles");
   cout << mc.size() << endl;
   for (int i=0; i<10; i++)  // add 10 monkeys
     mc.addStart("Another Monkey");
   cout << mc.size() << endl;
}

"""

tests = [["", []]]

