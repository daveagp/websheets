source_code = r"""
#include <iostream>
using namespace std;

int main() {
\[

\show:
   int n = 103;
   int* p = &n;
   delete p;
]\
}
"""

lang = "C++"

description = r"""
Trying to delete something invalid.
"""

tests = [["", []]] # stdin, args

example = True
