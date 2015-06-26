description = r"""
Write a static method <tt>complementWC(String dna)</tt>
that takes a String containing only the capital letters <tt>A</tt>, <tt>C</tt>,
 <tt>T</tt>, <tt>G</tt>,
(representing DNA), and returns its <i>Watson-Crick complement</i>:
replace <tt>A</tt> with <tt>T</tt>, <tt>C</tt> with <tt>G</tt>, and vice-versa.

<p>For example, <tt>complementWC("GATTACA")</tt> should return 
<tt>"CTAATGT"</tt>. (You may assume the input is valid, there is no need
to check for non-DNA characters.)

<p>
We encourage you to 
review the <a href="http://introcs.cs.princeton.edu/java/11cheatsheet/#String">
abbreviated String API</a> on the introcs cheatsheet. If you do this,
you can solve this problem without using any loops.

"""

source_code = r"""
public static String complementWC(String dna) {
   // replace all 'C's with 'G's and vice-versa
\[
   String tmp = dna.replaceAll("C", "X");
   tmp = tmp.replaceAll("G", "C");
   tmp = tmp.replaceAll("X", "G");
]\
   // replace all 'A's with 'T's and vice-versa
\[
   tmp = tmp.replaceAll("A", "X");
   tmp = tmp.replaceAll("T", "A");
   tmp = tmp.replaceAll("X", "T");
]\
   return \[tmp;]\ 
}"""

tests = r"""
test("complementWC", "GATTACA");
test("complementWC", "CAT");
test("complementWC", "TAGACAT");
test("complementWC", "GCGAGTGAGC");
test("complementWC", "");
"""
