source_code = r"""
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
using namespace std;

int main() {
   // CONSTRUCTOR
   ostringstream buf;
   
   // INSERT, part 1
   buf << "Eating text and numbers: ";
      
   // INSERT, part 2
   for (int i=0; i<10; i++)
      buf << i;

   // get CONTENTS: str() member function
   cout << "Length " << buf.str().length() << endl;
   cout << buf.str();

}
"""

lang = "C++"

example = True

description = "An example of ostringstreams."

tests = [["", []]]
