source_code = r"""
#include <iostream>
#include <string>
using namespace std;

int main() {
   string top, bottom, left, right;
   cin >> top >> bottom >> left >> right;
   // now do something clever to update the variables!
\[
   string t = top;
   top = left;
   left = bottom;
   bottom = right;
   right = t;
]\
   cout << top << " " << bottom << " " << left << " " << right;
   return 0;
}
"""

lang = "C++"

attempts_until_ref = 0

description = r"""
This program reads in 4 strings, representing the top, bottom, left, right 
colors of the sides
of a square. Your program should <i>rotate the square 90 degrees clockwise</i>
and output the top, bottom, left, right colors after the rotation. 
<p>
For example if the input is <tt>red green blue yellow</tt> then the rotation
looks like this:
<div><img src="http://cscircles.cemc.uwaterloo.ca/websheets/images/FourSwap.ipe.png"></div>
and the output should be <tt>blue yellow green red</tt>.
<p>
Hint: use a variant of the <i>swap idiom</i>.
"""

tests = [["red green blue yellow", []],
         ["fuschia vermilion salmon ochre", []],] # stdin, args
