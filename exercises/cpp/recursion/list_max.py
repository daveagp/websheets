attempts_until_ref = 0

description = r"""
Using recursion,
create a method <tt>maximum()</tt>
that finds the maximum element in a linked list of integers.
You will need to declare and define a helper function.
"""

lang = "C++"

source_code = r"""
#include <iostream>
#include <algorithm>
using namespace std;

// structure of items in list
struct Node {
   Node* next;  // each node knows "next" node
   int value;
   Node(int initialValue);  // constructor for nodes
};

Node::Node(int initialValue) {value = initialValue; next = NULL;}

class IntChain {
   public:
      IntChain();
      int maximum(); 
      void addStart(int newValue);
   private: 
\[
      int helpMax(Node* n); // compute max from here to end
]\
      Node* first;
};

IntChain::IntChain() {first = NULL;}
\hide[
// add a new node, containing this name, at the start of the list
void IntChain::addStart(int newValue) {
   Node* newFirst = new Node(newValue);
   Node* oldFirst = first;
   first = newFirst;
   first->next = oldFirst;
   // there's also a slightly trickier 2-line solution
}
]\

// private helper
\[
int IntChain::helpMax(Node* n) {
   if (n->next == NULL) {
      return n->value; // nothing to reverse
   }
   else {
      return max(n->value, helpMax(n->next));
   }
}
]\

int IntChain::maximum() {
\[
   return helpMax(first);
]\
}

int main() {
   IntChain c;
   int x;
   while (cin >> x) c.addStart(x);
   cout << c.maximum();
}

"""

tests = [
    ["1 0 3", []],
    ["3 0 1", []],
    ["1 3 0", []],
    ["9 4 4 0 19", []],
    ["2923 2 20 43 298", []],
]

verboten = ["for", "while", "do"]
