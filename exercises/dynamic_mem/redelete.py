source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int* p = new int; 
   *p = 103;         
\[
   delete p;
\show:
   delete p;
   delete p;
]\
}
"""

lang = "C++"

description = r"""
Re-deleting memory.
"""

tests = [["", []]] # stdin, args

example = True
