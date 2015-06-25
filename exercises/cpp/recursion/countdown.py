source_code = r"""
#include <iostream>
using namespace std;

void countdown(int n) {
  // base case
  if (n == 0) {
     cout << "Blastoff!" << endl;
  }
  // recursive case
  else {
     cout << n << endl;
     // recursive call
     countdown(n-1);
  }
}

int main() {
   countdown(5);
}
"""

example = True

lang = "C++"

description = r"""
Using a recursive function.
"""

tests = [
    ["", []]
]


