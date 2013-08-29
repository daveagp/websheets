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

tests = r"""
   test("main", "Jim", "29");
   test("main", "Jane", "9");
   test("main", "Whiskers", "0");
"""

description = r"""
Complete the code so that <code>java nextYear Trey 3</code> prints out 
<br><code>Next year, Trey will be 4 years old.</code>
"""
