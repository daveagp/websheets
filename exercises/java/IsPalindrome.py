description = r"""
(Exercise 3.1.13)
A <i>palindrome</i> is a string that reads the same forwards or backwards,
like <tt>"RADAR"</tt> or <tt>"STOOTS"</tt>.
Define a method <tt>isPalindrome</tt> 
that takes as input a string and returns true if the 
string is a palindrome, and false otherwise. You will need to use
the instance methods <tt>charAt()</tt> and <tt>length()</tt>
from the <a href="http://introcs.cs.princeton.edu/java/11cheatsheet/#String">String API</a>."""

source_code = r"""
public static boolean isPalindrome(String s) {
\[
// it's only necessary to do half the length many checks
for (int i=0; i<s.length()/2; i++) {
   // look at ith character from start and end
   if (s.charAt(i) != s.charAt(s.length()-i-1))
      return false;
}

return true; // everything matched
]\
}
"""

tests = r"""
test("isPalindrome", "racecar");
test("isPalindrome", "ferrari");
test("isPalindrome", "foolproof");
test("isPalindrome", "cool");
test("isPalindrome", "rester");
test("isPalindrome", "redder");
test("isPalindrome", "pinker");
test("isPalindrome", "o");
test("isPalindrome", "ok");
test("isPalindrome", "kk");
test("isPalindrome", "joUO9G");
test("isPalindrome", "rt2$77$2tr");
test("isPalindrome", "Qay&2&yaQ");
test("isPalindrome", "");
"""



