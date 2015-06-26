source_code = r"""
#include <iostream>
using namespace std; 

int main() {
   cout << "How many tacos do you want to buy? ";
   int tacos; // must declare before reading!
   cin >> tacos; // read input
   cout << "That will cost " << tacos * 3 << " dollars.";
   cout << endl;
   return 0;
}
"""

lang = "C++"

example = True

description = r"""
An example of taking input.
"""

tests = [["7", []],
         ["-4", []],
         ["5 this stuff is ignored", []]] # stdin, args
