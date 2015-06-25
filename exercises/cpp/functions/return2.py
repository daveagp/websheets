attempts_until_ref = 0

source_code = r"""
#include <iostream>
using namespace std; 

string example(int z) {
   if (z == 103) return "yay";
   return "boo";
}

int main() {
   cout << example(103);
}
"""

lang = "C++"

example = True

description = r"""
What is printed?
"""

tests = [["", []]]
