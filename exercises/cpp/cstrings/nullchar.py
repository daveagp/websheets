attempts_until_ref = 0

source_code = r"""
#include <iostream>
using namespace std; // access cout and endl

int main() {
   cout << boolalpha;
   char word[3] = "Hi";
   // check the characters
   cout << (word[0] == 'H') << endl;
   cout << (word[1] == 'i') << endl;
   cout << (word[2] == '\0') << endl;
   return 0;
}
"""

lang = "C++"

example = True

description = r"""
The null character is <tt>'\0'</tt>.
"""

tests = [["", []]] # stdin, args
