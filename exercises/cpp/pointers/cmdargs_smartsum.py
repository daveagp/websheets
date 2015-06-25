source_code = r"""
#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;

int main(int argc, char* argv[]) {

   int i;

   if (argc < \[2]\) {
     cout << "No input" << endl;
   }
   else {
     // if first argument is character i, add doubles
     if (\[argv[1][0]]\ == 'i') {
       int sum = 0;
       for (\[i=2]\; \[i < argc]\; i++) {
          sum += \[atoi(argv[i])]\;
       }
       cout << "Sum = " << sum << endl;
     }
     // check whether the first argument is the character d
     else if( \[ argv[1][0]  ]\ == 'd' ){
       double sum = 0;
       for(  \[ i=2  ]\ ; \[ i <= argc-1 ]\ ; i++ ){
          sum += \[  atof(argv[i]); ]\
       }
       cout << "Sum = " << sum << endl;
     }
     else {
       cout << "Invalid data type to sum" << endl;
     }

   }
   return 0;
}
"""

lang = "C++"

description = r"""
Now we want to write a program whose first command line argument is a 
'i' or 'd' to indicate 'integers' or 'doubles', respectively. If the
first argument is 'i' then the program should exepect any additional
command line arguments (if any) to be integers and sum them up displaying
the sum.  if the first argument is 'd' then the program should exepct
any additional command line arguments (if any) to be doubles and sum
them up.  Again, your program should not crash if the user forgets
to provide the 'd' or 'i', but instead just print 'No input'.
Also, if no numbers follow the 'd' or 'i' then
the program should just output the sum of 0.

So for example, if someone ran the program as:
  <tt>./cmdargs1 i 2 5 19 3</tt>
The output should be:
  <tt>29</tt>

If someone runs the program as:
  <tt>./cmdargs1 d 2.25 -1.0 </tt>
The output should be:
  <tt>1.25</tt>

If someone runs the program as:
  <tt>./cmdargs1</tt>
The output should be:
  <tt>No input</tt>
"""

tests = [
    ["", ["i", "2","5","19","3"]],
    ["", ["d", "2.25", "-1.0"]],
    ["", []],
    ["", ["i", "-2"]],
]


