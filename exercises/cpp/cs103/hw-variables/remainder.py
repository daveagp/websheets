source_code = r"""
#include <iostream>
using namespace std;

int main() {
\[
   int p, q;
   cin >> p >> q; // read two integers from input

   cout << (p % q); // remainder when p is divided by q

   return 0;
]\
}
"""

lang = "C++"

description = r"""
Write a program that takes two inputs <tt>p</tt> and <tt>q</tt>, which will be
integers, and outputs the remainder when <tt>p</tt> is divided by <tt>q</tt>.
<p>
For example if the input is <tt>20 7</tt>, then the output should be 
<tt>6</tt>. 
<p>Don't include any prompt like <tt>cout << "Please enter the input:"</tt>
&mdash; this will confuse the grader.
"""

tests = [
    ["20 7", []],
    ["14 7", []],
    ["34 3", []],
    ["17 1", []],
    ["18 1", []],
    ["123456 10", []],
] # stdin, args
