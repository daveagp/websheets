attempts_until_ref = 0

source_code = r"""
#include <iostream>
using namespace std;

void exchange(\[int& a, int& b]\) {
\[
   int tmp = a;
   a = b;
   b = tmp;
]\
}

int main() {
   int x = 103;
   int y = 99;
   exchange(x, y);
   cout << "x is " << x << ", y is " << y << endl;
}
"""

lang = "C++"

description = r"""
Performing a swap using pass-by-reference.
"""

tests = [
    ["", []]
]

