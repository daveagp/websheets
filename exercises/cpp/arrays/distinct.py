source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int n;
   cin >> n;

   int vals[100];

   // fill out the array
   for (int i=0; i<n; i++)
      cin >> vals[i];

\[
   bool all_distinct = true;

   for (int i=0; i<n; i++) {
      for (int j=i+1; j<n; j++) {
         if (vals[i] == vals[j]) {
            all_distinct = false;
         }
      }
   }
   
   if (all_distinct)
      cout << "distinct";
   else
      cout << "not distinct";
]\
}
"""

lang = "C++"

description = r"""
Write a program that takes an input <tt>n</tt>, 
then <tt>n</tt> more <tt>int</tt> inputs.
You may assume <tt>n</tt> is less than 100.
If all the numbers are distinct, print <tt>"distinct"</tt>.
Otherwise, print out <tt>"not distinct"</tt>.
<br>For example if the input is
<pre>
3
45 67 45
</pre>
then the output should be <tt>not distinct</tt>.
"""

tests = [
    ["3\n45 67 45", []],
    ["6\n5 4 8 2 3 9", []],
    ["6\n5 4 8 2 8 9", []],
    ["1\n103", []],
    ["10\n34 65 32 87 79 43 24 43 12 21", []],
    ["10\n34 65 32 87 79 43 24 37 12 21", []],
    ["10\n1 1 1 1 1 1 1 1 1 1", []],
] # stdin, args

attempts_until_ref = 0
