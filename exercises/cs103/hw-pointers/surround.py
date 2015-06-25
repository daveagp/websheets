source_code = r"""
#include <iostream>
using namespace std;

void surround(string* a, char ch)
{
   // surround the string with copies of ch
   *a = ch + *a + ch;
}

int main() {
   string name = "Tommy";
   char hyphen = '-';
   // surround name with hyphens
   surround(\[&name, hyphen]\);
   cout << "After calling surround, name is " << name << endl;
   return 0;
}
"""

lang = "C++"

description = r"""
We have defined a function
<tt>surround</tt> that takes a <tt>string</tt> pointer
and a <tt>char</tt> as input, and surrounds the pointed-to string 
with that character.
Call it on the values indicated below.
"""

tests = [
    ["", []]
]


