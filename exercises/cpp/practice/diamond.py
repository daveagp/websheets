remarks = """
based on this Creative Commons Att-SA 3.0 exercise:
https://cloudcoder.org/repo/exercise/535b0347ba7d641fd5860ddace95f258c17e2386
"""

source_code = r"""
#include <iostream>
#include <cstdlib>
using namespace std; 
\[

// print ch a total of n times
void reprint(char ch, int n) {
   for (int i=0; i<n; i++) {
      cout << ch;
   }
}

int main(int argc, char* argv[]) {
   int n;
   n = atoi(argv[1]);

   // draw the top half
   for (int i=0; i<n/2; i++) {
      // this counts the hyphens
      int hyphens = n/2-i;
      // but is off by one in the even case
      if (n%2 == 0) hyphens--;

      reprint('-', hyphens);
      reprint('X', n - 2*hyphens);
      reprint('-', hyphens);
      cout << endl;
   }

   for (int i=n/2; i<n; i++) {
      // this counts the hyphens
      int hyphens = i-n/2;

      reprint('-', hyphens);
      reprint('X', n - 2*hyphens);
      reprint('-', hyphens);
      cout << endl;
   }
}
]\
"""

lang = "C++"

attempts_until_ref = 0

description = r"""
Write a program that takes a command-line argument <tt>N</tt>
and draws a diamond of
<tt>'X'</tt> characters on a size-<tt>N</tt> grid of <tt>'-'</tt>
characters. For example <tt>diamond 5</tt> should print
<pre>
--X--
-XXX-
XXXXX
-XXX-
--X--
</pre>
and <tt>diamond 6</tt> should print
<pre>
--XX--
-XXXX-
XXXXXX
XXXXXX
-XXXX-
--XX--
</pre>
"""

tests = [
["", ["5"]],
["", ["6"]],
["", ["7"]],
["", ["8"]],
["", ["3"]],
["", ["2"]],
["", ["1"]],
["", ["0"]],
["", ["20"]],
["", ["25"]],
]


