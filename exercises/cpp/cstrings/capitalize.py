attempts_until_ref = 0

source_code = r"""
#include <iostream>
using namespace std;

void capitalize(char text[]) {
\[
   int i=0;
   while (text[i] != '\0') {
      if (text[i] >= 'a' &&  text[i] <= 'z') {
         text[i] += 'A'-'a';
      }
      i++;
   }
]\
}

int main() {
   char word[81]; // allow a word up to 80 characters
   cin >> word;
   cout << "Before calling your function, word is: " << word << endl;

   // call YOUR function
   capitalize(word);

   cout << "After calling your function, word is: " << word << endl;
   return 0;
}
"""

lang = "C++"

description = r"""
Define a function <tt>capitalize</tt>
that takes a C string and capitalizes every letter in it.
Non-letters should be left alone. 
<p>You may need to refer to an ASCII table:<br> <img src="http://macao.communications.museum/images/exhibits/2_18_8_1_eng.png">.
<p>You should <b>not</b> use cin or cout, that part is done for you
in order to facilitate testing.
"""

tests = [
    ["thisISaTEsT", []],
    ["don't_4get_ONLY_letters_CHANGE", []],
    ["abcsdmZklAdz][`'@{}", []],
] # stdin, args
