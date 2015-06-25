description = r"""
Define a recursive function <tt>int rec_len(char* str)</tt>
that computes the length of a C string without using a loop.
"""

source_code = r"""
#include <iostream>
using namespace std;

int rec_len(char* str) {
\[
   if (*str=='\0') 
      return 0;

   // go to next pointer, compute length, add 1
   return 1 + rec_len(str + 1);
]\
}

int main() {
   char buf[80];
   cin.getline(buf, 80);
   cout << rec_len(buf);
}
"""

lang = "C++"

tests = [
    ["Hi\n", []],
    ["Hello\n", []],
    ["Supercalifragilisticexpialadocious\n", []],
    ["\n(this test case should return 0, the above line is blank)", []],
]

verboten = ("#include", "for", "while", ".length", "length()")

