attempts_until_ref = 0

description = r"""
Define a recursive function to compute <i>maxprod(N)</i>.
"""

lang = "C++"

source_code = r"""
#include <algorithm>
#include <iostream>
using namespace std;

long maxprod(int n) {
   if (\[n <= 3]\)
      return \[n]\;
   else
      return \[max(2*maxprod(n-2), 3*maxprod(n-3))]\;
}

int main(int argc, char* argv[]) {
   cout << maxprod(atoi(argv[1])) << endl;
}
"""

tests = [
    ["", ["6"]],
    ["", ["7"]],
    ["", ["8"]],
    ["", ["20"]],
    ["", ["60"]],
]

