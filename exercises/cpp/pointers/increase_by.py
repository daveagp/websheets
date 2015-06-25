source_code = r"""
#include <iostream>
#include <cstdlib>
using namespace std;

int main(int argc, char* argv[]) {

   // parse command-line argument, save as variable n
\[
   int n = atoi(argv[1]);
]\
   // put each number from standard input as "read", one at a time
   int read;
   while (cin >> read) {
      cout << \[read + n]\ << endl;
   }
   return 0;
}
"""

lang = "C++"

description = r"""
Write a program <tt>increase_by</tt> 
that takes a command-line argument <tt>n</tt> and then adds <tt>n</tt>
to every number on input, and prints them out one per line.
For example
<pre>
./increase_by 5
</pre>
with input
<pre>
1
2
100
</pre>
should print
<pre>
6
7
105
</pre>
"""

tests = [
    ["1\n2\n100", ["5"]],
    ["1\n0\n3", ["1"]],
    ["11\n22", ["-10"]],
]

attempts_until_ref = 0

