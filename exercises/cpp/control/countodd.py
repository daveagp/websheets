source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int num_odds = 0;
   int value = 0;
 
   // You may declare any additional variables below or add any additional
   //  code before the loop starts.
\[      

]\

   // Then enter a condition in the while loop parentheses to continue
   //   receiving input until the user enters a negative number (i.e. -1).
   // For each number input, check if it is odd and if so, increase
   //  'num_odds' by 1. 
 
   while(  \[ value >= 0   ]\ )  {
     cout << "Enter a positive integer or -1 to quit:" << endl;
     cin >> value;
\[
     if( value >= 0 ){
       if( (value%2) == 1){
        num_odds++;
       }
     }
]\
   }

   cout << "You entered " << num_odds << " odd numbers" << endl;
   return 0;
}
"""

lang = "C++"
attempts_until_ref = 0

description = r"""
This program reads in integers until the user enters a negative number. 
For each positive number that is input, the program should check whether that
number is odd and, if so, increment a count of how many odd numbers 
have been input.  That total is output at the end of the program.
"""

tests = [["0 100 48 47 55 3 -1", []],
         ["-1", []],
         ["1 3 5 7 -1", []],] # stdin, args
