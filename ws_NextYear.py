classname = "NextYear"

code = r"""
public static void main(String[] args) {
\[
   System.out.print("Next year, ");
   System.out.print(args[0]);
   System.out.print(" will be ");
   System.out.print(Integer.parseInt(args[1])+1);
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
Complete the code so that <code>java nextYear Trey 3</code> prints out 
<br><code>Next year, Trey will be 4 years old.</code>
"""
