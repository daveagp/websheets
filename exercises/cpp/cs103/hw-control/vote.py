source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int age;
   cin >> age;
   if (\[age >= 18]\) {
\[     
   cout << "You can vote";
]\
   }
   else if (\[age < 0]\) {
\[       
   cout << "Time traveller!";
]\
   }
   else {
\[      
   cout << "Too young";
]\
   }
   return 0;
}
"""

lang = "C++"

description = r"""
This program takes an input <tt>age</tt> representing someone's age. If it is 
18 or bigger, print 
<pre>You can vote</pre>
If it is less than 18 but nonnegative, print
<pre>Too young</pre>
If it is negative, print
<pre>Time traveller!</pre>
"""

tests = [
    ["0", []],
    ["17", []],
    ["-1", []],
    ["19", []],
    ["1", []],
    ["18", []],
    ["99", []],
    ["9", []],
    ["-99", []],
] # stdin, args
