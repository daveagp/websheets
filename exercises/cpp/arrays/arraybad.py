source_code = r"""
#include <iostream>
#include <string>
using namespace std;

int main() {
\[
   
\show:
  int arr[3];        // declare an array
  int thirteen = 13; // never changes

  cout << "Badness: reading out of bounds!" << endl;
  cout << arr[3] << endl;
  cout << arr[-1] << endl;

  cout << "Worse: writing out of bounds!" << endl;
  arr[-1] = 34;
  cout << "thirteen is now: " << thirteen << endl;

  cout << "Writing out of bounds. C++ reports nothing :(" << endl;
  arr[3] = 103;
  cout << arr[3] << endl;

  cout << "Let's crash the program!" << endl;
  arr[340912983] = 78676;
  cout << "This line won't execute." << endl;

  return 0;
]\
}
"""

lang = "C++"

description = r"""
An example of unpredictable behaviour.
"""

cppflags_add = ["-Wno-array-bounds"]

tests = [["", []]] # stdin, args

example = True
