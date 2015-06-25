source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int* p = new int; 
   *p = 103;         
   delete p;      // too soon!
   cout << *p;    // too late!
}
"""

lang = "C++"

description = r"""
Accessing deleted memory.
"""

tests = [["", []]] # stdin, args

example = True
