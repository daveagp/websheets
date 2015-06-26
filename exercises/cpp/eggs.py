source_code = r"""
#include <iostream>
using namespace std; 

int main() {
   // Declare a variable to store the number of eggs
   //  since we must declare a variable before storing to it
   \[ int eggs; ]\

   // Output a prompt to ask for the number of eggs
   cout << "How many eggs do you have?" << endl;
   // Read in the number of eggs
   \[ cin >> eggs; // read input  ]\

   int num_cartons, num_boxes;

   // Write code to compute the number of boxes & cartons needed
   \[
   num_cartons = eggs / 12;
   if(eggs % 12 != 0){
     num_cartons++;
   }
   num_boxes = num_cartons / 5;
   if(num_cartons % 5 != 0){
     num_boxes++;
   }
   ]\

   cout << "You need " << num_boxes << " boxes and " << num_cartons << " cartons" << endl;
   return 0;
}
"""

lang = "C++"

example = False

description = r"""
Eggs are pacakged in cartons holding 1 dozen eggs and then boxes
that store 5 cartons each.  Given a number of eggs by the user, compute
how many cartons and boxes the pacakger will need.
"""

tests = [["12", []],
         ["60", []],
         ["61", []],
         ["119", []],
         ["120", []],
         ["1", []] ] # stdin, args
