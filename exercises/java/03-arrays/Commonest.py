description = r"""
<div>
Write a program <code>Commonest</code> that takes any number of command-line
arguments, which will be strings, and prints out the one that occurs most
often. For example <code>java Commonest cat dog monkey cat goose</code>
should print out <code>cat</code> and <code>java Commonest a a b b b</code> should print out <code>b</code>.
</div>
<div>
If more than one word is the commonest, print out the first one that 
occurs. Don't forget that strings have to be compared with <code>.equals</code>
instead of <code>==</code>.
</div>"""

source_code = r"""
public static void main(String[] args) {
   String commonest = "";    // just a placeholder for now
   int commonest_count = -1; // same
   int n = args.length;
   for (int i=0; i<n; i++) {
      // count how many times args[i] occurred
\[
      int count=0;
      for (int j=0; j<n; j++) {       // look everywhere
         if (args[i].equals(args[j])) // when you find it
            count++;                  // count it
      }
]\
      // we found a new commonest word
      if (count > commonest_count) {
         commonest = args[i];
         commonest_count = count;
      }
   }
   System.out.println(commonest);
}
"""


tests = """
testMain("dog", "cat", "fish", "bird", "cat");
testMain("a", "a", "a", "b", "b", "a", "b", "b", "b");
testMain("the", "commonest", "word", "in", "the", "English", "language");
testMain("first", "second", "third");
"""
