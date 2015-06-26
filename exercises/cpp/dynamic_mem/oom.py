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
Running out of memory.
"""

tests = [["", []]] # stdin, args

example = True

cppflags_remove = ["-Wall"]
cppflags_add = ["-Wall",  "-Wno-unused-variable"]
