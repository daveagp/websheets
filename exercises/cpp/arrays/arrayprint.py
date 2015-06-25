source_code = r"""
#include <iostream>
#include <string>
using namespace std;

int main() {
   int arr[3];
   arr[0] = 5;
   arr[1] = 10;
   arr[2] = 15;
\[
   for (int i=0; i<3; i++)
      cout << arr[i] << " ";
\show:
  cout << arr;
  return 0;
]\
}
"""

lang = "C++"

description = r"""
Why doesn't this print out the contents of an array?
"""

cppflags_add = ["-Wno-array-bounds"]

tests = [["", []]] # stdin, args

attempts_until_ref = 0
