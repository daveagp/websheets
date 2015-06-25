description = r"""
The official flag of CSCI 103 is a right triangle pointing up-left,
with <code>n</code> rows and <code>n</code> columns, made out of
backslashes, where <code>n</code> is a command-line argument.
Write a program to print it out for any positive integer <code>n</code>:
for example
<code>./flag 5</code> should print out
<pre>
\\\\\
\\\\
\\\
\\
\
</pre>
This tests two things: escaping in strings, and nested loops.
"""

lang = "C++"
attempts_until_ref = 0

source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int n;
   cin >> n;
   for (int i=0; \[i<n; i++]\) {
      for (int j\[=0; j<n-i; j++]\) {
         cout << \["\\"]\;
      }
      cout << \[endl]\;
   }
}
"""

tests = [["5", ""], ["10", ""], ["1", ""]]
