source_code = r"""
#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
   srand(103); 
   cout << "First two numbers in list 103: ";
   cout << rand() << " ";
   cout << rand() << endl;

   srand(1003); 
   cout << "First two numbers in list 1003: ";
   cout << rand() << " ";
   cout << rand() << endl;

   srand(103); 
   cout << "First two numbers in list 103 again: ";
   cout << rand() << " ";
   cout << rand() << endl;
}
"""

lang = "C++"

description = r"""
Using <tt>srand()</tt>.
"""

tests = [["", []]]

example = True
