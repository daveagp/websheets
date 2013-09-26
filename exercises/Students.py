description = r"""
 Read an the integer N from standard input, then a list
  of N student records, where each record consists of four
  fields, separated by whitespace:
<ul>
<li>first name</li>
<li>last name</li>
<li>email address</li>
<li>which section they're in</li>
</ul>
  Then, print a list of email address of students in sections 4 and 5.
  (Booksite Web Exercise 1.5.31)

<div>
For example, if the standard input is 
<pre>
6
Bob Sedgewick rs 1
Kevin Wayne wayne 4
Donna Gabai dgabai 5
David Pritchard dp6 6
Judith Israel jlisrael 3
Alan Turing turing 4
</pre>
Then the output should be
<pre>
Section 4
---------
wayne
turing

Section 5
---------
dgabai
</pre>
"""

source_code = r"""
public static void main(String[] args) { 

   // read the number of students
   int N = \[StdIn.readInt()]\ ;

   // declare and initialize four parallel arrays
   String[] first   = new String[N];
   \[String[]]\ last    = \[new String[N]]\;
   String[] \[email]\   = \[new String[N]]\;
   int[] section    = \[new int[N]]\;

   // read in the data from standard input
   for (\[int i=0; i<N; i++]\) {
      first[\[i]\]   = \[StdIn.readString();]\ 
      last[\[i]\]    = \[StdIn.readString();]\ 
      email[\[i]\]   = \[StdIn.readString();]\ 
      section[\[i]\] = \[StdIn.readInt();]\ 
   }

   // print email addresses of all students in section 4
   StdOut.println("Section 4");
   StdOut.println("---------");
   for (int i = 0; i < N; i++) {
      if (\[section[i] == 4]\) {
         StdOut.println(\[email[i]]\);
      }
   }
   StdOut.println(); // blank line

   // print email addresses of all students in section 5
   StdOut.println("Section 5");
   StdOut.println("---------");
   for \[(int i = 0; i < N; i++)]\ {
\[
      if (section[i] == 5) {
         StdOut.println(email[i]);
      }
]\
   }
}      
"""

tests = r"""
testStdin = "6\nBob Sedgewick rs 1\nKevin Wayne wayne 4\nDonna Gabai dgabai 5\nDavid Pritchard dp6 6\nJudith Israel jlisrael 3\nAlan Turing turing 4";
testMain();
testStdin = new stdlibpack.In("http://introcs.cs.princeton.edu/java/15inout/students.txt").readAll();
testMain();
"""
