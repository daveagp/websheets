description = r"""
Write a static method <tt>invert</tt> that takes
a <tt>ST&lt;Integer, String&gt;</tt>, and returns a
<tt>ST&lt;String, Integer&gt;</tt> where the keys and the values
are swapped. If the <tt>ST</tt> passed to <tt>invert</tt> has repeated
values, since it is not invertible, throw a <tt>RuntimeExeption</tt>.
"""

source_code = r"""
\[
public static ST<String, Integer> invert(ST<Integer, String> st) {
   ST<String, Integer> result = new ST<String, Integer>();
   for (int i : st) {
      String S = st.get(i);
      if (result.get(S) != null)
         throw new RuntimeException("Not invertible!");
      result.put(S, i);
   }
   return result;
}
]\
// test client. Reads alternating strings and ints from stdin, loads them
// into an ST<Integer, String>, inverts it and prints the result
public static void main(String[] args) {
   ST<Integer, String> orig = new ST<Integer, String>();
   while (!StdIn.isEmpty()) {
      orig.put(StdIn.readInt(), StdIn.readString());
   }
   ST<String, Integer> inverted = invert(orig);
   for (String s : inverted) {
      StdOut.println(s+" "+inverted.get(s));
   }
}
"""

tests = r"""
stdin = "1 one\n2 two\n3 three";
testMain();
stdin = "115 Time\n538 Magnetism\n577 Ecology\n664 Food_technology";
testMain();
expectException = true;
stdin = "1 Uninvertible\n2 Uninvertible";
testMain();
"""
