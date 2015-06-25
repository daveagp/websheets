source_code = r"""
#include <iostream>
using namespace std; // access cout and endl

int main() {
   cout << boolalpha;
   int grid[][] = {{11, 12, 13},
                   {21, 22, 23},
                   {31, 32, 33}};
\[

\show:
   // how can we determine the order in memory?
]\
}
"""

lang = "C++"

example = True

description = r"""
What order will the data be stored in? 
"""

tests = [["", []]] # stdin, args
