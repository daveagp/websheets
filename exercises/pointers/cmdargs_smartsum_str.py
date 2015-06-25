source_code = r"""
#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;



int main( int argc, char* argv[] ) {

   int i;

   if( argc < \[ 2 ]\ ){
     cout << "No input" << endl;
   }
   else {
     // check whether the first argument is "integer"
     if( \[ strncmp(argv[1],"integer",7) == 0 ]\ ){
       int sum = 0;
       for(  \[ i=2  ]\ ; \[ i <= argc-1 ]\ ; i++ ){
          sum += \[ atoi(argv[i]);  ]\
       }
       cout << "Sum = " << sum << endl;
     }
     // check whether the first argument is "double"
     else if( \[ strncmp(argv[1],"double",6) == 0  ]\  ){
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
Now we want to write a program whose first command line argument is the word 
'integer' or 'double' to indicate the type of data that follows. If the
first argument is 'integer' then the program should exepect any additional
command line arguments (if any) to be integers and sum them up displaying
the sum.  if the first argument is 'double' then the program should exepct
any additional command line arguments (if any) to be doubles and sum
them up.  Again, your program should not crash if the user forgets
to provide the 'integer' or 'double' keyword, but instead just print 
'No input'.  Also, if no numbers follow the 'double' or 'integer' then
the program should just output the sum of 0.

<p>
So for example, if someone ran the program as:
  <tt>./cmdargs1 integer 2 5 19 3</tt>
<p>
The output should be:
  <tt>29</tt>
<p>
If someone runs the program as:
  <tt>./cmdargs1 double 2.25 -1.0 </tt>
<p>
The output should be:
  <tt>1.25</tt>

<p>
If someone runs the program as:
  <tt>./cmdargs1</tt>
<p>
The output should be:
  <tt>No input</tt>
"""

tests = [
    ["", ["integer", "2","5","19","3"]],
    ["", ["double", "2.25", "-1.0"]],
    ["", []],
    ["", ["integer", "-2"]],
]


