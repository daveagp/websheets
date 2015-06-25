attempts_until_ref = 0

source_code = r"""
#include <iostream>
using namespace std;

\[
int mystery() {
   return 42;
}

int main() {
   cout << mystery();
   return 0;
}
\show:
int main() {
   cout << mystery();
   return 0;
}

int mystery() {
   return 42;
}
]\
"""

lang = "C++"

description = r"""
Why is the compiler complaining? How can we fix it?
"""

tests = [["", []]] # stdin, args

