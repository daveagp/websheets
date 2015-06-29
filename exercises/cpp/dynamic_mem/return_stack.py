source_code = r"""
#include <iostream>
using namespace std;

int* get_pointer_to(int x) {
   return &x;
}

int main() {
   int* p5 = get_pointer_to(5);
   int* p11 = get_pointer_to(11);
   cout << *p5 << endl;   
}
"""

lang = "C++"

description = r"""
Accessing deleted stack memory.
"""

tests = [["", []]] # stdin, args

example = True

cppflags_add = ["-Wno-return-stack-address", "-Wno-unused-variable"]
# "-Wno-return-local-addr"]

remarks = """for this to work, either you need clang, or a recent enough
version of g++ that supports -Wno-return-local-addr"""
