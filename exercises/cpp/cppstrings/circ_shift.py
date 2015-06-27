lang = "C++func"

attempts_until_ref = 0

description = r"""
A string <tt>S</tt> is a <i>circular shift</i> of a string <tt>T</tt>
if they are of the same length, and when written in clockwise circles,
they are the same except for a rotation. For example, <tt>STOP</tt> and
<tt>TOPS</tt> are circular shifts of each other,
as are <tt>STRING</tt> and <TT>RINGST</tt>. But <tt>STOP</tt> and
<tt>POTS</tt> are not circular shifts of one another, nor are 
<tt>CAT</tt> and <tt>ACT</tt>.

<p>
Write a static boolean method
<tt>is_circular_shift(string S, string T)</tt>
that determines whether two strings are circular shifts of one another.

<p>
One approach is to use <tt>length()</tt>, <tt>+</tt> and <tt>find()</tt>.
"""

source_code = r"""
#include <string>
using namespace std;

bool is_circular_shift(string s, string t) {
\[
   return s.length() == t.length() && (s+s).find(t)!=string::npos;
]\
}
"""

tests = [
    ["check-function", "is_circular_shift", "bool", ["string"]*2],
    ["call-function", "is_circular_shift", ['"POTS"', '"SPOT"']],
    ["call-function", "is_circular_shift", ['"TOPS"', '"STOP"']],
    ["call-function", "is_circular_shift", ['"TOPS"', '"SPOT"']],
    ["call-function", "is_circular_shift", ['"ABBA"', '"AABB"']],
    ["call-function", "is_circular_shift", ['"BYEBYE"', '"BYE"']],
    ["call-function", "is_circular_shift", ['"HI"', '"HIHI"']],
    ["call-function", "is_circular_shift", ['"TESTCASE"', '"TESTCASE"']],
    ["call-function", "is_circular_shift", ['"find()"', '"()find"']],
    ["call-function", "is_circular_shift", ['"find()"', '"(find)"']],
]
