source_code = r"""
#include <iostream>
using namespace std;

void bincombos(char* array, int current, int len) {
   // Code for base case (i.e. end of array)
   //   When do we know there are no more bits to show
   //   and what should we do if that is the case
\[
   if(current == len){
      array[len] = '\0';
      cout << array << endl;
   }
]\
   // Code for recursive case
   //   If we're not at the last bit, then set that
   //   bit location to each of its possible values and
   //   each time you change the value use recursion to 
   //   generate all the combinations of bits after it
\[
   else {
      array[current] = '0';
      bincombos(array, current+1, len);
      array[current] = '1';
      bincombos(array, current+1, len);
   } 
]\
}

int main() {
   // read target, n, then n sorted inputs
   int numBits;
   cin >> numBits;

   // allocate an array to hold the current combo + null char
   char* arr = new char[numBits+1];
   
   // Call the function to generate all binary combos
   bincombos(arr, 0, numBits);

   delete [] arr;
   return 0;
}
"""

lang = "C++"

description = r"""
Complete the following program to print out all possible binary combinations
of a given number of digits. E.g. <tt>./bincombos</tt> with input <tt>1</tt>
should print out
<pre>
0
1
</pre>
With input 2 it should print out
<pre>
0<b>0</b>
0<b>1</b>
1<i>0</i>
1<i>1</i>
</pre>
where the bold/italics emphasize the relation to the previous case.
<i>You shouldn't try to add bold/italics.</i> With input 3 it should likewise print out
<pre>
0<b>00</b>
0<b>01</b>
0<b>10</b>
0<b>11</b>
1<i>00</i>
1<i>01</i>
1<i>10</i>
1<i>11</i>
</pre>
To do this,
fill out the recursive function
 <tt>bincombos(char arr[], int current, int len)</tt>.
It should try setting <tt>current</tt> to each possible value,
setting that bit to '0' and '1' in turn and using recursion to go through
all the options of the remaining bits.
<p>
Use the base case to check that a particular combination is ready for printing.
<p>
Use the recursive case to set the current bit place and recurse to the next
bit.
"""

tests = [
    ["0", []],
    ["1", []],
    ["2", []],
    ["3", []],
] # stdin, args

attempts_until_ref = 0
