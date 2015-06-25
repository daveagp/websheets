source_code = r"""
#include <iostream>
using namespace std;

void basen_combos(int base, char* array, int current, int len) {
   // Code for base case (i.e. end of array)
   //   When do we know there are no more digits to show
   //   and what should we do if that is the case
\[
   if(current == len){
      array[len] = '\0';
      cout << array << endl;
   }
]\
   // Code for recursive case
   //   If we're not at the last digit, then set that
   //   digit location to each of its possible values and
   //   each time you change the value use recursion to 
   //   generate all the combinations of digits after it
   //   
   // Remember to make the char version of digit x, use '0'+x
\[
   else {
      for(int i=0; i < base; i++){
        array[current] = '0'+i;
        basen_combos(base, array, current+1, len);
      }
   } 
]\
}

int main() {
   // read target, n, then n sorted inputs
   int base, numDigits;
   cin >> base >> numDigits;

   // allocate an array to hold the current combo + null char
   char* arr = new char[numDigits+1];
   
   // Call the function to generate all binary combos
   basen_combos(base, arr, 0, numDigits);

   delete [] arr;
   return 0;
}
"""

lang = "C++"

description = r"""
Complete the following program to print out all possible combinations
of a given base and number of digits. E.g. <tt>./bincombos</tt> with input <tt>4 2</tt>
should print out
<pre>
00
01
02
03
10
11
12
13
20
21
22
23
30
31
32
33
</pre>
With input <tt>2 3</tt> it should print out
<pre>
000
001
010
011
100
101
110
111
</pre>
With input <tt>10 1</tt> it should print out
<pre>
0
1
2
3
4
5
6
7
8
9
</pre>
To do this,
fill out the recursive function
 <tt>basen_combos(int base, char arr[], int current, int len)</tt>.
It should try setting <tt>current</tt> to each possible value,
 in turn and using recursion to go through all the options of the remaining digits.
<p>
Use the base case to check that a particular combination is ready for printing.
<p>
Use the recursive case to set the current digit place and recurse to the next
digit.
"""

tests = [
    ["2 3", []],
    ["4 2", []],
    ["10 1", []],
    ["8 2", []],
] # stdin, args

attempts_until_ref = 0
