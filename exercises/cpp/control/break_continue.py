source_code = r"""
#include <iostream>
using namespace std;

int main() {
   string line_of_text;
   int counter = 0;
   while (true) {
      getline(cin, line_of_text);
      if (cin.fail())
         \[break    ]\;
      
      if (line_of_text == "SKIP") 
         \[continue]\;

      if (line_of_text == "DONE") 
         \[break    ]\;

      counter++;
      cout << counter << " " << line_of_text << endl;
   }
   cout << "Printed " << counter << " lines." << endl;
}
"""

lang = "C++"

description = r"""
Write a program that reads any number of lines of text from the user.
It should print out each one, with its line number. However,
<ul>
<li>if the line is <tt>SKIP</tt>, skip it
<li>if the line is <tt>DONE</tt>, stop reading completely
</ul>
E.g., for the input
<pre>
Hello World
Bonjour, Monde
SKIP
Hallo, Welt
DONE
Hola, Mundo
</pre>
the output should be
<pre>
1 Hello World
2 Bonjour, Monde
3 Hallo, Welt
Printed 3 lines.
</pre>
(The summary line logic is written for you already.)
"""

tests = [
    ["""Hello World
Bonjour, Monde
SKIP
Hallo, Welt
DONE
Hola, Mundo
""", []],
    ["""SKIP
SKIP
SKIP
to my loo
SKIP
to the loo
my darling
""", []],
    ["""apple
orange
DONE
DONE
SKIP
banana
""", []],
] # stdin, args

attempts_until_ref = 0
