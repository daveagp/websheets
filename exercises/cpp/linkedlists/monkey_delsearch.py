attempts_until_ref = 0

description = r"""
Create a member function <tt>bool delSearch(string target)</tt>
that searches for the target string in the list.
<br>If it finds this item, it should delete it and return <tt>true</tt>.
<br>If it it not found, return <tt>false</tt> and don't alter the list.
<br>You can assume the item occurs at most once in the list.
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
      string delEnd();
      bool delSearch(string target);
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


int MonkeyChain::size() {
   int count = 0;
   Node* loc = first;
   while (loc != NULL) {
      count++;
      loc = loc->next;
   }
   return count;
}
]\
bool MonkeyChain::delSearch(string target) {
\[
   if (isEmpty()) 
      return false;
   else if (first->name == target) {
      Node* oldFirst = first;
      first = first->next;
      delete oldFirst;
      return true;
   }
   else {
      // advance curr until curr->next is thing to delete
      // why? then curr is the Node that must change
      Node* curr = first;
      // stop when we find it or curr->next doesn't exist
      while (curr->next != NULL 
          && curr->next->name != target)
         curr = curr->next;

      if (curr->next == NULL)
         return false; // not found
      else {
         Node* oldNode = curr->next;
         curr->next = curr->next->next;
         delete oldNode;
         return true;
      }
   }   
]\
}

int main() {
   MonkeyChain mc;
   mc.threeKongs();
   mc.addStart("Bubbles");
   mc.addStart("King Kong");
   // list: KK, Bubbles, DK Sr, DK, DK Jr
   cout << boolalpha;

   cout << "Deleted Diddy? " << mc.delSearch("Diddy") << endl;
   mc.printAll(); cout << endl;

   cout << "Deleted DK? " << mc.delSearch("DK") << endl;
   mc.printAll(); cout << endl;

   cout << "Deleted King Kong? " << mc.delSearch("King Kong") << endl;
   mc.printAll(); cout << endl;

   cout << "Deleted DK Jr? " << mc.delSearch("DK Jr.") << endl;
   mc.printAll(); cout << endl;

   cout << "Deleted DK Sr? " << mc.delSearch("DK Sr.") << endl;
   mc.printAll(); cout << endl;

   cout << "Deleted Bubbles? " << mc.delSearch("Bubbles") << endl;
   mc.printAll(); cout << endl;

   // test your deallocation
   for (int i=0; i<500000; i++) {
      mc.addStart("A");
      mc.addStart("B");
      mc.addStart("C");
      mc.delSearch("A");
      mc.delSearch("D");
      mc.delSearch("C");
      mc.delSearch("B");
   }
}

"""

tests = [["", []]]

