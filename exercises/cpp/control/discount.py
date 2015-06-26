source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int cost;
   cout << "Enter the number of items you wish to buy?" << endl;
   // Receive the number of items and calculate the total cost
   //  Recall items cost $5 each with a $10 discount if the total is 
   //  at least $50
  
\[
   int items;
   cin >> items;
   cost = 5*items;
   if(cost >= 50){
     cost -= 10;
   }
]\

   cout << "Final cost is " << cost << endl;
   return 0;
}
"""

lang = "C++"
attempts_until_ref = 0

description = r"""
This program reads in an integer number of items a user wants to buy and
then computes the final cost.  Items cost <b><i>$</i>5 each</b> but customers will
receive a <b><i>$</i>10 discount (i.e. subtract <i>$</i>10 from their total)</b> if their
total bill is at least <i>$</i>50.   You should receive input from user and
compute the final cost in the variable <code>cost</code>.
"""

tests = [["9", []],
         ["10", []],
         ["1000", []],] # stdin, args
