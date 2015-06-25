source_code = r"""
#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
   char buf[80];
   char ch;
   int i;
   cin >> buf; cout << buf << endl;
   cin >> i; cout << i << endl;
   cin >> ch; cout << ch << endl;
   cin >> ch; cout << ch << endl;
   cin >> i; cout << i << endl;
   cin >> buf; cout << buf << endl;
}
"""

example = True

lang = "C++"

description = r"""
What will be printed if the input is <pre>hi 5s     4    every1</pre>
"""

tests = [
    ["hi 5s    4    every1", []]
]


