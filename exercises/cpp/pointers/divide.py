source_code = r"""
#include <iostream>
#include <cstdlib>
using namespace std;

int main(int argc, char* argv[]) {

   if (\[argc != 4]\) {
     cout << "wrong number of arguments" << endl;
   }
   else {
     // if first argument starts with 'i', divide integers
     if (argv[1][0] == \['i']\) {
        // parse arguments as integers
        \[int]\ x = atoi(argv[2]);
\[
        int y = atoi(argv[3]);
]\
        // divide and print
        cout << x / \[y]\;
     }
     else {
        // parse as doubles, divide and print
        double x = \[atof(argv[2])]\;
\[
        double y = atof(argv[3]);
        cout << x / y;
]\
     }
   }
   return 0;
}
"""

lang = "C++"

description = r"""
Write a program <tt>divide</tt> 
that is capable of performing integer or floating-point division.
For example
<pre>
./divide d 12.3 10.0
</pre>
asks for division of doubles and prints <tt>1.23</tt>, while
<pre>
./divide i 10 3
</pre> 
asks for integer division and should print <tt>3</tt>.

<p>
Print <tt>wrong number of arguments</tt> if the number of arguments is wrong.
You don't need to do any further error checking for this exercise.
"""

tests = [
    ["", ["d", "12.3","10.0"]],
    ["", ["i", "10", "3"]],
    ["", ["d", "7","2"]],
    ["", ["i", "7", "2"]],
    ["", ["d", "1.8","1.2"]],
    ["", ["d", "45"]],
    ["", ["i", "-2", "-3", "-4"]],
]


attempts_until_ref = 0
