source_code = r"""
#include <iostream>
#include <cstdlib>
using namespace std;

// main should accept command-line arguments
int main(\[int argc, char* argv[]]\) {

   int sum = 0;
   int i;

   // convert and add up each argument
   for (\[i=1]\; \[i < argc]\; i++) {
      sum += \[atoi(argv[i])]\;
   }

   cout << "Sum is " << sum << endl;
   return 0;
}
"""

lang = "C++"

description = r"""
Write a program <tt>cmdargs_sum</tt> 
that adds up all of its command-line arguments.
<!--We want to write a program that adds a series of integers provided
by the user as command line arguments.  We have declared a <tt>sum</tt>
variable for you.  You need to figure out the loop counter initialization
and condition as well as how to convert each command line argument
to an integer before it is added.  Also, if there are no arguments
your program should not crash but just output th sum of 0.-->

For example, if you run
  <pre>./cmdargs_sum 2 5 19 3</pre>
The output should be:
  <pre>29</pre>
Assume the inputs are all integers.

<!--If some one runs the program as:
  <tt>./cmdargs1</tt>
The output should be:
  <tt>0</tt>-->
"""

tests = [
    ["", ["2","5","19","3"]],
    ["", []],
    ["", ["-2"]],
]


attempts_until_ref = 0
