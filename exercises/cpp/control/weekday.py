source_code = r"""
#include <iostream>
using namespace std;

int main() {

   cout << "Enter an integer between 1-7 (1=Sun. to 7=Sat.)" << endl;

   // Receive the number between 1-7 and if the corresponding day is
   //  a "weekday" or "weekend" output that single word.  Output nothing
   //  if the user outputs a number outside the range 1-7.
  
\[
   int day;
   cin >> day;
   if(day == 1 || day == 7){
     cout << "weekend";
   }
   else if( day >= 2 && day <= 6){
     cout << "weekday";
   }
]\

   return 0;
}
"""

lang = "C++"
attempts_until_ref = 0

description = r"""
Ask the user to enter a number between 1-7 where 1 corresponds to Sunday,
2 corresponds to Monday, ..., and 7 corresponds to Saturday.  
Receive the integer input from the user and output the word 
<code>weekday</code> if the day is Monday-Friday.  Output the word 
<code>weekend</code> if the day is Saturday-Sunday.  Output nothing
at all if the user enters a number that's not in the range 1-7.
"""

tests = [["-1", []],
         ["0", []],
         ["1", []],
         ["2", []],
         ["3", []],
         ["4", []],
         ["6", []],
         ["7", []],
         ["8", []],] # stdin, args
