source_code = r"""
public static void main(String[] args) {
\[
   System.out.print("Next year, ");
   System.out.print(args[0]); // name
   System.out.print(" will be ");
   int inputAge = Integer.parseInt(args[1]);
   System.out.print(inputAge + 1);
   System.out.println(" years old.");
]\
}
"""

tests = r"""
   //test("main", (Object) new String[] {"Jim", "29"});
   testMain("Jim", "29");
   testMain("Jane", "9");
   testMain("Whiskers", "0");
"""

description = r"""
<p><i>This is a more complex version of the <b>NameAge</b> exercise.</i></p>
Using <code>Integer.parseInt()</code>, 
complete the code so that <code>java NextYear Trey 3</code> prints out 
<pre>Next year, Trey will be 4 years old.</pre>
Your code should similarly compute the age next year for any arguments <code>«name» «age»</code>.
"""

