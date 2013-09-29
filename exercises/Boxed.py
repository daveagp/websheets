description = r"""
Write a program <code>Boxed</code> whose API has two public static methods:
<ul>
<li>A method <code>repeat()</code> that takes a string argument and an integer argument,
and returns the <code>String</code> obtained by repeating the string that many times.
For example <code>repeat("hots", 2)</code> should return <code>"hotshots"</code>
</li>
<li>A method <code>boxedPrint()</code> that takes a string argument, and prints
it out surrounded by a box of asterisks. 
For example, <code>boxedPrint("Hello, World!")</code> should cause the following
text to be sent to standard output:
<pre>
***************
*Hello, World!*
***************
</pre>
Use <code>repeat()</code>, and to get
the length of a String <code>stringVar</code>, use <code>stringVar.length()</code>.
</li>
</ul>
"""
source_code = r"""
public static \[String]\ repeat(\[String S, int times]\) {
\[
   String result = "";
   for (int i=0; i<times; i++)
      result += S;
   return result;
]\
}

public static \[void]\ boxedPrint(\[String S]\) {
\[
   StdOut.println(repeat("*", S.length()+2));
   StdOut.println("*"+S+"*");
   StdOut.println(repeat("*", S.length()+2));
]\
}

//basic tests
public static void main(String[] args) {
   StdOut.println(repeat("jar", 2));
   StdOut.println(repeat("he", 4));
   boxedPrint("Hello, World!");
}
"""

tests = r"""
testMain();
test("repeat", "meow", 4);
test("repeat", "nothing", 0);
test("boxedPrint", "|||stars and stripes|||");
"""
