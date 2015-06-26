source_code = r"""
#include <iostream>
using namespace std;

int main() {
\[
   cout << "Hello, world!" << endl;
\show:
   cout << Hello, <<
   cout << world!
]\
   return 0;
}
"""

lang = "C++"

description = r"""
Fix this program so that it outputs <pre>Hello, world!</pre>
followed by a newline character.
"""

tests = [["", []]] # stdin, args
