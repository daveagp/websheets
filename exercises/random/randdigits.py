source_code = r"""
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
\[
   srand(time(0));   
   int total = 0;
   for (int i=0; i<1000; i++) {
      int random_digit = rand() % 10;
      total += random_digit;
   }
   cout << total;
\show:
   srand(time(0));   
   int total = 0;
   int random_digit = rand() % 10;
   for (int i=0; i<1000; i++) {
      total += random_digit;
   }
   cout << total;
]\
   return 0;
}
"""

lang = "C++"

description = r"""
Write a program that prints out the sum of 1000 random digits.
<p>
A correct program should usually output totals between 4400 and 4600.
"""

tests = [["", []]]

example = True
