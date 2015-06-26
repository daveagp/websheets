source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int* p = new int; // get address of 4 new bytes of memory
   *p = 103;         // store 103 there
   cout << *p;       
   delete p;         // remember to recycle!
}
"""

lang = "C++"

description = r"""
An example of new and delete.
"""

tests = [["", []]] # stdin, args

example = True
