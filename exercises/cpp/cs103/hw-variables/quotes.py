source_code = r"""
#include <iostream>
using namespace std;

int main() {
   cout << \["Debug Me!";\show:Debug Me!]\
   return 0;
}
"""

lang = "C++"

description = r"""
Debug this program so that it prints out the text <tt>Debug Me!</tt>
"""

tests = [
    ["", []],
] # stdin, args
