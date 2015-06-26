source_code = r"""
#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
using namespace std;

int main() {
   // CONSTRUCT from a string
   istringstream storage("Sample    text   2parse");

   string word1, word2, word3;
   int num;

   // EXTRACT from the stringstream
   storage >> word1 >> word2 >> num >> word3;

   cout << "Word 1: " << word1 << endl;
   cout << "Word 2: " << word2 << endl;
   cout << "Number: " << num << endl;
   cout << "Word 3: " << word3 << endl;

   // has a fail() member function like other istreams
   cout << "Fail? " << boolalpha << storage.fail() << endl;
   storage >> num; // try to read more
   cout << "Fail now? " << storage.fail() << endl;
}
"""

example = True

lang = "C++"

description = r"""
Using an <tt>istringstream</ii>.
"""

tests = [
    ["", []]
]


