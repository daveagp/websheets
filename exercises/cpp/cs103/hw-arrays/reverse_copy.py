source_code = r"""
#include <iostream>
#include <cmath>
using namespace std;

int main() {
   // read the input
   int n;
   cin >> n;
   int src[100]; // declare an array, max size 100
   for (int i = 0; i < n; i++) 
      cin >> src[i]; // read elements of src from input

   // declare dest array
   \[int dest[100];]\

   // copy from src to dest, but in reverse order
\[
   for (int i = 0; i < n; i++) {
      dest[i] = src[n-i-1];
   }
]\

   // output dest to check it
   for (int i = 0; i < n; i++)
      cout << dest[i] << " ";

   return 0;
}
"""

lang = "C++"

description = r"""
Write a code fragment to copy the values from one array 
<tt>src</tt> into another array <tt>dest</tt>,
but in reverse order. For example, if <tt>src</tt> contains the four numbers
<style>
table.t * {font-family: 'Source Code Pro', monospace !important;}
table.t * {border: 1px solid black !important;}
table.t {border-collapse: collapse; width: auto !important;}
span.spoiler {color: white; border: 1px solid black;}
</style>
<table class='t'><tr><td>4<td>3<td>17<td>1</table>
then your code should fill <tt>dest</tt> with
<table class='t'><tr><td>1<td>17<td>3<td>4</table>
<b>Note:</b> the program will read the array size <tt>n</tt> and <tt>src</tt>
from input. But the input and output are done already for you.
<p><b>Hint</b> (hover to reveal): <span class='spoiler'>To get started, note that the element at position <tt>0</tt> 
should correspond to position <tt>n-1</tt> in the new array.</span>
"""

tests = [
    ["4\n1 17 3 4", []],
    ["5\n90210 2014 103 11 6", []],
    ["6\n4 8 15 16 23 42", []],
    ["10\n4 1 6 9 6 7 1 1 1 1", []],
] # stdin, args
