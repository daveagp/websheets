source_code = r"""
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std; 

int main() {
   cout << 2.5 * 4 << endl; // what data type and output do you expect?
   cout << showpoint; // change a flag
   cout << 2.5 * 4; // try again
   return 0;
}
"""

lang = "C++"

example = True

description = r"""
Using the <tt>showpoint</tt> output manipulator.
"""

tests = [["", []]]
