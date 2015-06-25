source_code = r"""
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
   srand(time(0)); 
   cout << rand() << endl;
   cout << rand() << endl;
   cout << rand() << endl;
   cout << rand() << endl;
}
"""

lang = "C++"

description = r"""
Using <tt>srand()</tt>.
"""

tests = [["", []]]

example = True
