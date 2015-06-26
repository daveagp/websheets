source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int* arr = new int[3]; // get 12 bytes of memory
   arr[0] = 13;
   arr[1] = 7;
   arr[2] = 42;
   cout << arr[0] << " " << arr[1] << " " << arr[2];
   delete[] arr;         // remember to recycle!
}
"""

lang = "C++"

description = r"""
An example of new and delete.
"""

tests = [["", []]] # stdin, args

example = True
