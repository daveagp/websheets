source_code = r"""
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
   // get the input
   int n;
   cin >> n;

   // to print out fixed-width columns, print out each item with
   // cout << setw(4) << "item"; // see page 49
\[
   for (int j=1; j<=n; j++) {

      // print items in a row
      for (int i=1; i<=n; i++)   
         cout << setw(4) << i*j;

      // end the row
      cout << endl;
   }
]\
   return 0;
}
"""

lang = "C++"

description = r"""
Write a program that prints out a multiplication table. It should
take an input <tt>n</tt>. The output
should have <tt>n</tt> rows and <tt>n</tt> columns, and be 
formatted in 4-space wide 
columns, like this example output when the input <tt>n</tt> is 5:
<pre>
   1   2   3   4   5
   2   4   6   8  10
   3   6   9  12  15
   4   8  12  16  20
   5  10  15  20  25
</pre>
Use <tt>cout << setw(4) << [thing you want to print]</tt> with each item printed, in order to get the column-based layout.
"""

tests = [
    ["5", []],
    ["10", []],
    ["15", []],
] # stdin, args

attempts_until_ref = 0
