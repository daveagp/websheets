attempts_until_ref = 0

source_code = r"""
#include <iostream>
using namespace std;

void println(\[const char*\show:char*]\ text) {
   cout << text << endl;
}

int main() {
   println("Hello!");
}
"""

lang = "C++"

cppflags_remove = ["-Wno-write-strings"]

description = r"""
Showing a usage of <tt>const</tt>.
"""

tests = [
    ["", []]
]

