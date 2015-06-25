attempts_until_ref = 0

source_code = r"""
#include <iostream>
using namespace std; 

void reset(int x) {
   x = 0;
}

int main() {
   int number = 33;
   reset(number);
   cout << number;
}
"""

lang = "C++"

example = True

description = r"""
What is printed?
"""

tests = [["", []]]
