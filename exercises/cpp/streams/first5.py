source_code = r"""
#include <iostream>
#include <cstring>
using namespace std;

int main() {
   for (int i=0; i<5; i++) {
      char ch = (char) cin.get();
      cout << i << "th char: " 
           << ch << endl;
   }
}
"""

example = True

lang = "C++"

description = r"""
Using <tt>cin.get()</tt>.
"""

tests = [
    ["hi  mom", []]
]


