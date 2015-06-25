description = r"""
<div>Part 1. Write a method <code>reverse1()</code> that takes a String array
as an argument, and returns a
<i>new</i> String array which holds the reverse of the original. 
<b>This method should not alter the original array</b>. 
</div>
<div>Part 2. 
Write a function <code>reverse2()</code> to
reverse the elements in a String array passed to the method. The
method should not return anything. Hint: you can use the code from page 89 or
Booksite Ex. 1.4.4. (Web Exercise 2.1.35)"""

source_code = r"""
public \[static String[]]\ reverse1(\[String[] a]\) {
\[
   int n = a.length; // just for convenience
   String[] result = new String[n];
   for (int i=0; i<n; i++)
      result[i] = a[n-i-1]; // map 0 to n-1, 1 to n-2, ...
   return result;
]\
}

public \[static void]\ reverse2(\[String[] a]\) {
\[
   int n = a.length; // just for convenience
   // swap 0 with n-1, 1 with n-2, ...
   for (int i=0; i < n/2; i++) {
      String tmp = a[i];
      a[i] = a[n-i-1];
      a[n-i-1] = tmp;
   }
]\
}

// basic tests
public static void main(String[] args) {
   String[] test = {"this", "is", "a", "test"};
   String[] tset = reverse1(test);
   StdOut.println("after calling reverse1, test is: "
                  + java.util.Arrays.toString(test));
   StdOut.println("after calling reverse1, tset is: " 
                  + java.util.Arrays.toString(tset));
   String[] second = {"another", "test", "for", "you", "here"};
   reverse2(second);
   StdOut.println("after calling reverse2, second is: " 
                  + java.util.Arrays.toString(second));
}
"""

tests = """
   testMain();
   test("reverse1", (Object)new String[]{"calling", "reverse1", "directly"});
   test("reverse2", (Object)new String[]{"reverse2", "return", "type", "ok?"});
"""
