source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int n;
   cin >> n;
\[
   if (n % 100 >= 11 && n % 100 <= 13)
      cout << n << "th";
   else if (n % 10 == 1)
      cout << n << "st";
   else if (n % 10 == 2)
      cout << n << "nd";
   else if (n % 10 == 3)
      cout << n << "rd";
   else
      cout << n << "th";
]\
   return 0;
}
"""

lang = "C++"
attempts_until_ref = 0

description = r"""
This program should take a non-negative integer input <tt>n</tt>. 
It should print out the 
English <i>ordinal number</i> corresponding to <tt>n</tt>.
For example,
<ul><li>for input <tt>1</tt> it should output <tt>1st</tt>
<li>for input <tt>2</tt> it should output <tt>2nd</tt>
<li>for input <tt>3</tt> it should output <tt>3rd</tt>
<li>for input <tt>4</tt> it should output <tt>4th</tt>
</ul>
et cetera. 
<p>Hint: the last digit is important, and you can compute the last
digit using <tt>n % 10</tt>, which is the remainder when you divide <tt>n</tt>
by 10. You also need a special case when the last two digits are 11, 12, or 13.
"""

tests = [
["1", []],
["2", []],
["3", []],
["4", []],
["5", []],
["6", []],
["7", []],
["8", []],
["9", []],
["10", []],
["21", []],
["132", []],
["4323", []],
["12984", []],
["11", []],
["212", []],
["90013", []],
] # stdin, args
