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

// prototype any helper functions here if you wish...
//  As a challenge try to make the return type void
\[
void llsum_helper(Item* head, int& curr_sum);
]\

// llsum implementation
int llsum(Item* head)
{
\[
  int sum = 0;
  llsum_helper(head, sum);
  return sum;
]\
}

// implement any helper function here
\[
void llsum_helper(Item* head, int& curr_sum)
{
  if(head == NULL) return;
  else {
    curr_sum += head->val;
    llsum_helper(head->next, curr_sum);
  }
}
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
Write a recursive function to sum up the integers in a  linked list. In this approach, try to use tail recursion where you sum values on the way down the list (i.e. sum the current value and then pass that down the chain via a recursive call).
"""

tests = [["", []]] # stdin, args
