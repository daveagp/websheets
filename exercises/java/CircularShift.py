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
<tt>isCircularShift(String S, String T)</tt>
that determines whether two strings are circular shifts of one another.

<p>
We encourage you to 
review the <a href="http://introcs.cs.princeton.edu/java/11cheatsheet/#String">
abbreviated String API</a> on the introcs cheatsheet. If you do this,
you can solve this problem in one line
using a concatenation, calls to <tt>length()</tt>,
and one additional method call (<a href="http://docs.oracle.com/javase/7/docs/api/java/lang/String.html#indexOf(java.lang.String)">hint</a>).
"""

source_code = r"""
public static boolean isCircularShift(String S, String T) {
\[
   return S.length() == T.length() && (S+S).indexOf(T)>=0;
]\
}
"""

tests = r"""
test("isCircularShift", "POTS", "SPOT");
test("isCircularShift", "TOPS", "STOP");
test("isCircularShift", "TOPS", "SPOT");
test("isCircularShift", "ABBA", "AABB");
test("isCircularShift", "BYEBYE", "BYE");
test("isCircularShift", "HI", "HIHI");
test("isCircularShift", "TESTCASE", "TESTCASE");
test("isCircularShift", "indexOf()", "Of()index");
test("isCircularShift", "indexOf()", "Ofindex()");
"""
