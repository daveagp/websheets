source_code = r"""
#include <iostream>
#include <cstring>
using namespace std;

int main() {
   // store 10 user names 
   // names type is a char**
   char* names[10];
   char temp[50];
 
   for (int i=0; i < 10; i++) {
   \[
      cin >> temp;
      char* new_region = new char[strlen(temp)+1];
      names[i] = new_region; // shallow copy (address)
      strcpy(names[i], temp); // deep copy (each character)
    \show:
      cin >> names[i]; // does this work?
      // PS: don't allocate more than needed.
   ]\
   }

  // now print the names
   for (int i=0; i < 10; i++) {
      cout << names[i] << " ";
   }  
   cout << endl;
   // now free/delete the memory you allocated
\[
   for (int i=0; i < 10; i++) {
      delete[] names[i];
   }
\show:
   ; // TODO
]\
   return 0;
}
"""

cppflags_remove = ["-Wall"]
cppflags_add = ["-Wall", "-Wno-unused-variable"]


lang = "C++"

description = r"""
Write a program that reads 10 names from input, stores them in an
array of dynamically-allocated char pointers, and prints them out.
<ul>
<li>Don't allocate more dynamic memory than absolutely necessary.
This means that you need to read strings to a temporary buffer,
then create dynamic memory of exactly the right size.
<li>Remember to recycle 
<i>all</i> dynamically-allocated memory!

"""

tests = [
    ["Timothy Christopher Jennifer Tommy John Bill Rafastafafarimalingoberry Melissa JackTwentyFourLetterName Peter", []]
]

attempts_until_ref = 0

