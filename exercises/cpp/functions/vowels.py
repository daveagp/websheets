attempts_until_ref = 0

source_code = r"""
#include <iostream>
#include <string>
using namespace std;

// return the number of times that needle occurs in haystack
int frequency(string haystack, char needle) {
   int n = haystack.length(); // this is how you get length of C++ string
   int result = 0;

   // loop to count the occurrences 
   for (int i=0; i<n; i++) {
      if (haystack[i] \[== needle]\) // look at ith character
         \[result++;]\
   }

   return result;
} 

// return the number of vowels in the given string
\[
int vowel_count(string text) {
   return frequency(text, 'a') + frequency(text, 'e') + 
       frequency(text, 'i') + frequency(text, 'o') + frequency(text, 'u');
}
]\
"""

lang = "C++func"

description = r"""
<b>Note:</b> For this exercise, we'll use C++ <tt>string</tt> objects. 
To get the <i>k</i>th <tt>char</tt> from a <tt>string s</tt>, 
write <tt>s[k]</tt>, like an array.
<p>
Complete the method
<tt>int frequency(string haystack, char needle)</tt>
so that it returns the number of times that the character <tt>needle</tt>
occurred in <tt>haystack</tt>. For example <tt>frequency("hello", 'l')</tt>
should return 2.
<p>
Then, define a function <tt>vowel_count</tt> that takes a <tt>string</tt>
argument and returns the number of vowels it contains. Assume the vowels are:
a, e, i, o, and u. For example <tt>vowel_count("hello")</tt> should be 2. 
Hint: use <tt>frequency</tt>. 
"""

tests = [
    ["check-function", "frequency", "int", ["string", "char"]],
    ["check-function", "vowel_count", "int", ["string"]],
    ["call-function", "frequency", ['"hello"', "'l'"]],
    ["call-function", "frequency", ['"goodbye"', "'l'"]],
    ["call-function", "vowel_count", ['"supercalifragilisticexpialidocious"']],
    ["call-function", "vowel_count", ['"facetious"']],
    ["call-function", "vowel_count", ['"phhhht"']],
]


