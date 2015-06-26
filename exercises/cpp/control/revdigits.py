source_code = r"""
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
   int n;
   int revn;

   // write code that allows the user to enter a non-zero integer 
   // which could be either (pos. or neg). and then 
   // outputs the number with digits reversed
   //  Example 1:    321    outputs:  123
   //  Example 2: -14539    outputs:  -93541
   // Output a newline after you output the digits in reverse.

   cout << "Enter an integer: " << endl;
   cin >> n;

\[      
   if(n == 0) { cout << 0; }
   else {
     if(n < 0){
       cout << "-";
       n = -n;
     }
     while( n > 0 ) {
       cout << n%10;
       n = n/10;
     }
   }
   cout << endl;
]\
  return 0;
}
"""

lang = "C++"

description = r"""
This program should take an integer input (which could be negative) and
outputs the string of digits of the number in reverse order.  If the number
is negative you should still output a negative sign first.
"""

tests = [["-14539", []],
         ["-321", []],
         ["321", []],
         ["0", []],]
                    # stdin, args
attempts_until_ref = 0
