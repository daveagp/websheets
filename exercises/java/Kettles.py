description = r"""
Write a program <code>Kettles</code> with a recursive static method
<code>sing(n)</code> which prints the famous "kettles of tea" song.
For example, when <code>n</code> is 3, calling <code>sing(3)</code>
should print out
<pre>
3 kettles of tea on the wall
3 kettles of tea
take one down, pass it around
2 kettles of tea on the wall!
2 kettles of tea on the wall
2 kettles of tea
take one down, pass it around
1 kettles of tea on the wall!
1 kettles of tea on the wall
1 kettles of tea
take one down, pass it around
no more kettles of tea on the wall!
</pre>
<div>
<i>To sing this song, first sing the first four lines, and then sing
the song for a smaller value of n (unless you are done).</i>
This is the strategy that you can turn into
a recursive method.
</div>
Note that we require your song to say <code>1 kettles</code>
instead of the grammatically correct <code>1 kettle</code>. Fixing this 
is left as a challenge for the thirsty.
"""

source_code = r"""
public static void sing(int n) {
   // print three lines
\[
   StdOut.println(n + " kettles of tea on the wall");
   StdOut.println(n + " kettles of tea");
   StdOut.println("take one down, pass it around");
]\
   if (n > 1) {
      // sing fourth line, with exclamation point!
\[
      StdOut.println(n-1 + " kettles of tea on the wall!");
]\
      // call sing recursively on remaining kettles
      sing(\[n-1]\);
   }
   else { 
      // sing the final line, with exclamation point!
\[
      StdOut.println("no more kettles of tea on the wall!");
]\
   }
}

public static void main(String[] args) {
   sing(Integer.parseInt(args[0]));
}
"""

tests = r"""
testMain(3);
test("sing", 1);
testMain(9);
"""
