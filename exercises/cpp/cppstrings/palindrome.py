lang = "C++func"

attempts_until_ref = 0

description = r"""
A <i>palindrome</i> is a string that reads the same forwards or backwards,
like <tt>"RADAR"</tt> or <tt>"STOOTS"</tt>.
Define a function <tt>palindrome</tt> 
that takes as input a string and returns true if the 
string is a palindrome, and false otherwise. You will need to use
the <tt>[i]</tt> operator and <tt>length()</tt> method.
"""

source_code = r"""
#include <iostream>
#include <string>
using namespace std;

bool palindrome(string s) {
\[
// it's only necessary to do half the length many checks
for (int i=0; i<s.length()/2; i++) {
   // look at ith character from start and end
   if (s[i] != s[s.length()-i-1])
      return false;
}

return true; // everything matched
]\
}
"""

tests = [
    ["check-function", "palindrome", "bool", ["string"]],
    ["call-function", "palindrome", ['"racecar"']],
    ["call-function", "palindrome", ['"ferrari"']],
    ["call-function", "palindrome", ['"foolproof"']],
    ["call-function", "palindrome", ['"cool"']],
    ["call-function", "palindrome", ['"rester"']],
    ["call-function", "palindrome", ['"redder"']],
    ["call-function", "palindrome", ['"pinker"']],
    ["call-function", "palindrome", ['"radar"']],
    ["call-function", "palindrome", ['"rider"']],
    ["call-function", "palindrome", ['"o"']],
    ["call-function", "palindrome", ['"ok"']],
    ["call-function", "palindrome", ['"kk"']],
    ["call-function", "palindrome", ['""']],
]

