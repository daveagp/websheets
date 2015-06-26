source_code = r"""
#include <iostream>
#include <string>
using namespace std;

int main() {
   int n;
   string text;
   cin >> n >> text;

   // repeat n times
   // see page 144 for an example of defining the loop control variable
   for (\[int i = 0]\; \[i < n]\; \[i = i + 1]\)
   {
      // print text
\[   
      cout << text;
]\
   }
   return 0;
}
"""

lang = "C++"

description = r"""
This program takes two inputs: an integer <tt>n</tt>
and a string <tt>text</tt>. Complete it so that it prints out
the <tt>text</tt> over and over, a total of <tt>n</tt> times.
<p>
Don't print any spaces or newlines. For example, 
<ul><li>if the input is <tt>2 hots</tt> the output should be <tt>hotshots</tt>
<li>if the input is <tt>5 /\</tt> the output should be <tt>/\/\/\/\/\</tt>
</ul>
"""

tests = [
    ["2 hots", []],
    ["5 /\\", []],
    ["8 wo", []],
    ["3 ~", []],
    ["0 nothing_should_print", []],
] # stdin, args
