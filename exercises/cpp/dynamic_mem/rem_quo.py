source_code = r"""
#include <iostream>
using namespace std;

int* rem_quo(int x, int y) {
   int* result = new int[2];
   result[0] = x % y;
   result[1] = x / y;
   return result;
}

int main() {
   int* rq = rem_quo(103, 5);
   cout << rq[0] << " " << rq[1];
   delete[] rq;
}
"""

lang = "C++"

description = r"""
Creating and destroying in different functions.
"""

tests = [["", []]] # stdin, args

example = True
