source_code = r"""
#include <iostream>
using namespace std;

char* suffix(char* text) {
\[
   return text + 1;
]\
}

int main() {
   char* word = (char*) "lion";
   cout << word << endl;
   cout << suffix(word) << endl;
   cout << suffix(suffix(word)) << endl;
   cout << suffix(suffix(suffix(word))) << endl;
}
"""

lang = "C++"

description = r"""
Write a function <tt>suffix</tt> that takes a <tt>char*</tt>
representing a null-terminated character array (a C string), and returns
the string obtained by starting at the second letter. For example
<pre>suffix("thug")</pre>
should return a C string containing <tt>"hug"</tt>.
<p>
Hint: you shouldn't be trying to create new memory locations or change
the given string.
<p>
You're not required to check if the string is already empty.
"""

tests = [
    ["", []]
]


