source_code = r"""
#include <iostream>
using namespace std;

int main(int argc, char* argv[]) {
   cout << "argc is " << argc << endl;
   // each argv[i] is a char* (a C string)
   for (int i = 0; i < argc; i++) {
      cout << "argv[" << i << "] is " << argv[i] << endl;
   }
   return 0;
}
"""

lang = "C++"

example = "True"

description = r"""
An example of <tt>argc</tt> and <tt>argv</tt>.
"""

tests = [
    ["", ["-al"]],
    ["", ["funky", "pineapple"]],
    ["", []],
]


