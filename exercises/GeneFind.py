description = r"""
Solve the following simplified version of
the <i>gene finding problem</i>. You will be given a <tt>String dna</tt>
consisiting of the capital letters <tt>A</tt>, <tt>C</tt>,
 <tt>T</tt>, <tt>G</tt>. You need to determine if there is any subsequence
of the form
<pre>ATG...TAG</pre>
where the region <tt>...</tt> has a length that is a 
<i>positive multiple
of three</i>. If such a region exists, print out the <tt>...</tt> part (the gene).

For example, if <tt>dna</tt> is <tt>"CATTATGGTTCACTAGCC"</tt> then the
gene you should return is <tt>"GTTCAC"</tt>. Here are some additional rules
your code must follow.
<ul>
<li>
The gene part may contain <tt>ATG</tt>.
<li>
The gene part must not contain <tt>TAG</tt> at any index that is a multiple
of three. But it can contain it at other positions. For example, <tt>"TATTAG"</tt> is not a possible gene, but <tt>"ATAGAC"</tt> is.
<li>
If one or more multiple possible genes exist, return the one with
the leftmost start position.
<li>
If no possible genes exist, return the string <tt>"no gene"</tt>
</ul>

We recommend you use <a href="http://docs.oracle.com/javase/7/docs/api/java/lang/String.html#indexOf(java.lang.String, int)"><tt>String.indexOf(String, int)</tt></a> to
search for substrings. This will simplify one of the tricky/repetitive parts of the
code.
"""

source_code = r"""
public static String findGene(String dna) {
   String START_CODON = "ATG";
   String END_CODON = "TAG";
\[
   // what's the rightmost position so far where we found a start codon?
   int latestStartIndex = -1;
   while (true) {
      // find the next start codon
      latestStartIndex = dna.indexOf(START_CODON, latestStartIndex+1);

      // -1 is used to indicate no match by String.indexOf()
      if (latestStartIndex == -1)
         return "no gene"; // we didn't find a match

      // where is the next matching end?
      int endIndex = dna.indexOf(END_CODON, latestStartIndex+6);
      // keep going if length is not a multiple of 3
      while ((endIndex != -1) && ((endIndex - latestStartIndex) % 3 != 0)) {
         endIndex = dna.indexOf(END_CODON, endIndex+1);
      }
      
      // we're done if length is a multiple of 3
      if ((endIndex != -1) && ((endIndex - latestStartIndex) % 3 == 0))
         return dna.substring(latestStartIndex+3, endIndex);
   }
]\
}
"""

tests = r"""
test("findGene", "CATTATGGTTCACTAGCC");
test("findGene", "ATGGTTCACTAG");
test("findGene", "AATGGTTCACTAGG");
test("findGene", "ATGATGGTTCACTAG");
test("findGene", "ATGGTTCACTAGTAG");
test("findGene", "CACACATGTTTTTAGTTTTTTAGCCCC");
test("findGene", "CACACATGTTTTTAGTTTTTAGCCCC");
test("findGene", "ATGTAG");
test("findGene", "ATGTAGATGTAG");
test("findGene", "GAGAATGCTAGCTAGCTAGGAGA");
test("findGene", "GAGAATGCATGCATGCATGCATGCTAGGAGA");
test("findGene", "ATGCATTACTAGCCCATGTACCATTAG");
test("findGene", "TACGTAGCTACGATCGTACGATGCTAGCTAGCTGCGTCAGCGTGTATAGTAGGCGCAGT");
test("findGene", "TACGTATGCTACGATCGTACGATGCTAGCTAGCTGCGTCAGCGTGTATAGTAGGCGCAGT");
"""
