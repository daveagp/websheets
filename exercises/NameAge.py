source_code = r"""
public static void main(String[] args) {
\[
   System.out.print(args[0]); // name
   System.out.print(" is ");
   System.out.print(args[1]); // age
   System.out.println(" years old.");
]\
}
"""

show_class_decl = True

tests = r"""
   //test("main", (Object) new String[] {"Jim", "29"});
   testMain("Jim", "29");
   testMain("Jane", "9");
   testMain("Whiskers", "0");
"""

description = r"""
Using <code>args[]</code>, <code>System.out.print()</code> and <code>System.out.println()</code>, complete the code so that <code>java NameAge Trey 3</code> prints out 
<pre>Trey is 3 years old.</pre>
Your code should print the name and age in the same format for any arguments <code>«name» «age»</code>.
"""

