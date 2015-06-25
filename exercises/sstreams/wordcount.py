attempts_until_ref = 0

source_code = r"""
#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
using namespace std;

int main() {
   string line;
   // read each line
   while (getline(cin, line)) {
      // create istringstream from line
      istringstream \[storage(line)]\;
      // loop through storage with >>, counting words
\[
      string word;
      int count = 0;
      while (storage >> word) {
         count++;
      }
]\
      // print word count
      cout << \[count]\ << endl;
   }
}
"""

lang = "C++"

description = r"""
Write a program that takes any number of lines from input, 
and counts the number of words per line, writing each number on a line 
by itself. For example, for the input
<pre>
Measuring programming progress
by lines of code
is like measuring aircraft building progress
by weight
</pre>
the output should be
<pre>
3
4
6
2
</pre>
Use an <tt>istringstream</tt> with <tt>&gt;&gt;</tt> to skip whitespace.
"""

tests = [
    ["""Measuring programming progress
by lines of code
is like measuring aircraft building progress
by weight""", []],
["""
There are only  two  kinds of programming languages
those people always gripe about
and those nobody uses
""", []],
["Weeks of programming can save you hours of planning", []]
]


