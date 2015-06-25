source_code = r"""
#include <iostream>
#include <string>
using namespace std;

struct Item {
  Item(int v, Item* n) { val = v; next = n; }
  int val; 
  Item* next;
};

// prototype
int llsum(Item* head);

// prototype any helper functions here if you wish
\[

]\

// llsum implementation
int llsum(Item* head)
{
\[
  if(head == NULL)
    return 0;
  else
    return head->val + llsum(head->next);
]\
}

// implement any helper function here
\[

]\

int main() 
{

  cout << llsum(NULL) << endl;
  Item* head = new Item(4, new Item(7, new Item(9, new Item(6, NULL))));
  cout << llsum(head) << endl;

}
"""

lang = "C++"

description = r"""
Write a recursive function to sum up the integers in a  linked list. In this approach, try to use head recursion where you sum values on the way back up the list.
"""

tests = [["", []]] # stdin, args
