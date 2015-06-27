attempts_until_ref = 0
source_code = r"""
#include <iostream>
using namespace std;

// return how many times p is a factor of x
 \[ int ]\ remove_factor(\[ int x, int p ]\) {
   // return the correct value
\[
   int num=0;
   while(x%p == 0){
     num++;
     x = x/p;
   }
   return num;
]\
}
"""

lang = "C++func"

description = r"""
Define a function <tt>remove_factor</tt> that takes two integer arguments, 
<tt>x</tt> and <tt>p</tt>.  <tt>x</tt> should be a non-zero positive integer and  
<tt>p</tt> should be a positive integer bigger than 1. The function should
return how many times p is a factor of x.  For example if x=40 and p=2, then you should
return 3 since 40 = 2<sup>3</sup> &times; 5 
 (i.e. 2 occurs as a factor of 40 three times)
<p>
<b>Note: don't use <tt>cout</tt></b> in your code. 
Just <tt>return</tt> the appropriate value. The grader will 
automatically add print statements as it sees fit.
"""

tests = [
    ["check-function", "remove_factor", "int", ["int","int"]],
    ["call-function", "remove_factor", ["40","3"]],
    ["call-function", "remove_factor", ["32","2"]],
    ["call-function", "remove_factor", ["1024","2"]],
    ["call-function", "remove_factor", ["54","3"]],
     ["call-function", "remove_factor", ["49", "7"]]
]


