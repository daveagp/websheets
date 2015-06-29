source_code = r"""
#include <iostream>
#include <string>
using namespace std;

int main() {
\[
   cout << boolalpha;
\show:
   ;
]\
   int age = 9; // years
   double mass = 5.6; // kilograms
   char initial = 'B';
   string hair = "Longhair";
   bool male = false;
   cout << age << " " << mass << " " 
        << initial << " " << hair << " " << male;
   // something's funny! we can fix it: see page 444 of the textbook
}
"""

lang = "C++"

description = r"""
An example of variables, using my cat.
"""

tests = [["", []]] # stdin, args

