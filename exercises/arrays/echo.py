source_code = r"""
#include <iostream>
#include <string>
using namespace std;

int main() {
\[
   int n;
   cin >> n;

   string words[100];

   // fill out the array
   for (int i=0; i<n; i++)
      cin >> words[i];

   // output twice
   for (int i=0; i<n; i++)
      cout << words[i] << endl;
   for (int i=0; i<n; i++)
      cout << words[i] << endl;
]\
}
"""

lang = "C++"

description = r"""
Write a program that takes an input <tt>n</tt>, 
then <tt>n</tt> more <tt>string</tt> inputs.
You may assume <tt>n</tt> is less than 100.
Print out all of the strings, one per line, and then print them 
all out again. For example if the input is
<pre>
3
repeat
me
plz
</pre>
then the output should be
<pre>
repeat
me
plz
repeat
me
plz
</pre>
"""

tests = [
    ["3\nrepeat\nme\nplz", []],
    ["6\nwe\nwill\nwe\nwill\nrock\nyou", []],
    ["1\nabracadabra", []],
] # stdin, args

attempts_until_ref = 0
