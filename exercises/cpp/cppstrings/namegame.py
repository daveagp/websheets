attempts_until_ref = 0

source_code = r"""
#include <iostream>
#include <string>
using namespace std;

// avoid copying the long name
string namegame(const string& name) {
\[
   return "Z" + name.substr(1);
\show:
   name[0] = 'Z'; // whoops
   return name;
]\
} 

int main() {
   string name;
   cin >> name;
   cout << "My name is: " << name << endl;
   cout << "Ziggity Zap " << namegame(name) << endl;
   cout << "My name is: " << name << endl; // should be unchanged
}
"""

lang = "C++"

description = r"""
The function <tt>namegame(string s)</tt> should return
a string which is the same as its input, except
starting with <tt>Z</tt>.
<p>
For example <tt>namegame("David")</tt> returns <tt>"Zavid"</tt>.
"""

tests = [
    ["Rumpelstiltskin", []],
    ["Wolfeschlegelsteinhausenbergerdorff", []],
]

