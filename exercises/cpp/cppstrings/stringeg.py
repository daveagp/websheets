source_code = r"""
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
\[

\show:
   cout << boolalpha;
// parallel syntax for construction, like
// int      x = 5;
   string name = "Bobby";
   cout << name << endl; // Bobby

   string place = name; // deep copy
   cout << (place == name) << endl; // deep compare: true

   place[0] = 'L';
   cout << name << " " << place << endl; // Bobby Lobby
   cout << (place == name) << endl; // deep compare: false

   // member functions (dot notation!)
   cout << place.length() << endl; // 5
   cout << place.substr(2, 2) << endl; // bb
]\
}
"""

lang = "C++"

description = r"""
An example of <tt>string</tt>.
"""

tests = [
    ["", []],
] # stdin, args

example = True
