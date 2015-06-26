attempts_until_ref = 0
source_code = r"""
#include <iostream>
using namespace std;

\[
int rangesize(int start, int end) {
   return end-start+1;
}

double rangesize(double start, double end) {
   return end-start;
}
]\

int main() {
   cout << showpoint;
   cout << rangesize(10, 20) << endl; // 11
   cout << rangesize(3.4, 6.2) << endl; // 2.8
   cout << rangesize(8, 30) << endl; // 23
   cout << rangesize(8.0, 30.0) << endl; // 22.0
   return 0;
}
"""

lang = "C++"

description = r"""
Define two functions named <tt>rangesize</tt>.
<ol>
<li>
<tt>int rangesize(int start, int end)</tt> <br> This function should return the number of integers in the set 
$\{\textrm{start}, \textrm{start}+1, \dotsc, \textrm{end}\}$, which is <tt>end - start + 1</tt>.
<li>
<tt>double rangesize(double start, double end)</tt> <br> This function should return the length of the 
interval $[\textrm{start},\textrm{end}]$ of real numbers, which is <tt>end - start</tt>.
</ol>
"""

tests = [["", []]] # stdin, args
