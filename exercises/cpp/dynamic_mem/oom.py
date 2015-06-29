source_code = r"""
#include <iostream>
using namespace std;

int main() {
   for (int i=0; i<1000000; i++) {
      int* p = new int;
\[
      delete p;

\show:
      ;
]\
   }
}
"""

lang = "C++"

description = r"""
Running out of memory. <i>What needs to change to avoid this?</i>
"""

tests = [["", []]] # stdin, args

#example = True

cppflags_add = ["-Wno-unused-variable"]
