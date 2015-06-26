attempts_until_ref = 0

source_code = r"""
#include <vector>
#include <iostream>
using namespace std;

string middle(\[vector<string>]\ v) {
\[
   return v[v.size()/2]; // rounds down
]\
}

int main() {
   vector<string> words;
   words.push_back("Doc");
   cout << middle(words) << endl; // Doc
   words.push_back("Grumpy");
   words.push_back("Happy");
   cout << middle(words) << endl; // Grumpy
   words.push_back("Sleepy");
   words.push_back("Bashful");
   cout << middle(words) << endl; // Happy
   words.push_back("Sneezy");
   words.push_back("Dopey");
   cout << middle(words) << endl; // Sleepy
}
"""

lang = "C++"

tests = [["", []]]

description = """Define a function <tt>middle</tt> that takes
a <tt>vector&lt;string&gt;</tt>; it should 
return the middle string. (You can assume the length is odd.)
<p>See the test <tt>main</tt> for an example of calling it.
"""
