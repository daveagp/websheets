attempts_until_ref = 0

source_code = r"""
#include <iostream>
using namespace std;

void reset(\[int* x\show:int x]\)
{
\[
   *x = 0;
\show:
   x = 0;
]\
}

int main() {
   int num = 103;
   reset(\[&num\show:num]\);
   cout << num;
}
"""

lang = "C++"

description = r"""
In a previous exercise we tried to write a function that would
reset a variable, but it failed to work because of C++'s pass-by-value 
semantics.
<p>We can fix it now! Use pointers to do so.
"""

tests = [
    ["", []]
]


