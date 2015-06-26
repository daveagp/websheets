source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int h, w;
   cin >> h >> w;
\[
   for (int i=0; i<h; i++) {
      for (int j=0; j<w; j++) {
         cout << "=";
      }
      cout << endl;
   }
\show:
   int i;
   for (i=0; i<h; i++) {
      for (i=0; i<w; i++) {
         cout << "=";
      }
      cout << endl;
   }
]\
   return 0;
}
"""

lang = "C++"

description = r"""
Write a program that takes two inputs <tt>h</tt> and <tt>w</tt>
and draws a grid of equals signs of height <tt>h</tt> and width <tt>w</tt>.
E.g. if the input is <tt>2 3</tt> the output should be:
<pre>
===
===
</pre>
"""

tests = [
    ["2 3", []],
    ["10 4", []],
] # stdin, args

attempts_until_ref = 0
