source_code = r"""
#include <iostream>
#include <string>
using namespace std;

int main() {
\[
   
\show:
  // create array. which ones are valid?
  char greeting[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
  //char greeting[] = {'H', 'e', 'l', 'l', 'o', '\0'};
  //char greeting[5] = {'H', 'e', 'l', 'l', 'o', '\0'};
  //char greeting[7] = {'H', 'e', 'l', 'l', 'o', '\0'};
  //char greeting[6] = {'H', 'i', '\0', 'o', 'k', '\0'};

// ? what about this one?
// char greeting[] = {'H', 'e', 'l', 'l', 'o', ' ', 'm', 'y',
//                    ' ', 'f', 'r', 'i', 'e', 'n', 'd', 's'};

  // pass its address to cout
  cout << greeting; 

  return 0;
]\
}
"""

lang = "C++"

description = r"""
An example of a null-terminated character array.
"""


tests = [["", []]] # stdin, args

example = True
