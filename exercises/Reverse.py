description = r"""
Write a program <code>Reverse</code> that takes any number
of command-line arguments and prints them out on a single
line in reverse order. For example, <code>java Reverse these words will be reversed</code> should output
<pre>reversed be will words these</pre>
For simplicity, add spaces after each word, including the last one.
"""

tests = r"""
testMain("reversed", "be", "will", "words", "these");
testMain("arrays", "are", "awesome");
testMain("The", "structure", "of", "a", "sentence", "is", "not", "symmetric");
testMain("one-word");
testMain();
"""

source_code = r"""
public static void main(String[] args) {
\[
   for (int i=args.length-1; i>=0; i--)
      System.out.print(args[i]+" ");
]\
}
"""
