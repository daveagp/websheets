source_code = r"""
#include <iostream>
using namespace std;

void bincombos(string prefix, int len) {
   // base case: we don't have to add any more 0s and 1s
   // the prefix is a complete string, so print it and quit
\[
   if (prefix.length() == len) {
      cout << prefix << endl;
      return;
   }
]\

   // recursive case: try adding 0 or 1 as the next digit,
   // then continue trying all possibilities after that
\[
   bincombos(prefix + "0", len);
   bincombos(prefix + "1", len);
]\
}

int main() {
   // what size combos do we want?
   int numBits;
   cin >> numBits;

   // start the recursion
\[
   bincombos("", numBits);
]\

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
where the bold/italics is added just to show the relation to the previous case (don't try to add it).
With input 3 it should likewise print out
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
 <tt>void bincombos(string prefix, int len)</tt>.
It should try appending a '0' or '1' to the prefix in turn, 
using recursion to go through
all the options of the remaining bits. For instance when n=2,
you want the recursive call tree to look like this:
<pre>
                  ("", 2)
                  /    \
          ("0", 2)      ("1", 2)
         /    \            /    \  
("00", 2)  ("01", 2)  ("10", 2)  ("11", 2)
</pre>
so it will print out
<pre>
00
01
10
11
</pre>
"""

tests = [
    ["0", []],
    ["1", []],
    ["2", []],
    ["3", []],
] # stdin, args

attempts_until_ref = 0
