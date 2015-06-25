source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int nums[4]; // declare array of ints called "nums"
   cin >> nums[0] >> nums[1] >> nums[2] >> nums[3];
   cout << "In reverse order, the numbers were: ";
\[
   cout << nums[3] << " " << nums[2] << " " << nums[1] << " " << nums[0];
]\
   return 0;
}
"""

lang = "C++"

description = r"""
Write a program that takes 4 numbers as input, and prints them out in reverse 
order. For example, if the input is
<pre>
4 42 15 13
</pre>
then the output should be
<pre>
In reverse order, the numbers were: 13 15 42 4
</pre>
Using a loop is not required.
"""

tests = [
    ["4 42 15 13", []],
    ["23 34 1 7", []],
    ["5 5 5 -5", []],
] # stdin, args
