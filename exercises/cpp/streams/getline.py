source_code = r"""
#include <iostream>
#include <cstring>
using namespace std;

int main() {
   int i=0;
   while (true) {
      i++;
      char text[20];
      cin.getline(text, 20); // buffer, size
      cout << i << "th line (length " 
           << strlen(text) << "): "
           << text << endl;
      if (strlen(text)==0)
         return 0;
   }
}
"""

example = True

lang = "C++"

description = r"""
Using <tt>cin.getline()</tt>.
"""

tests = [
    ["first line\n2nd       line\n  extra  spaces  \n", []]
]


