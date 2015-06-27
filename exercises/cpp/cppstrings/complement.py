attempts_until_ref = 0

description = r"""
Write a function <tt>string complement(string dna)</tt>
that takes a string containing only the capital letters <tt>A</tt>, <tt>C</tt>,
 <tt>T</tt>, <tt>G</tt>,
(representing DNA), and returns its <i>Watson-Crick complement</i>:
replace <tt>A</tt> with <tt>T</tt>, <tt>C</tt> with <tt>G</tt>, and vice-versa.

<p>For example, <tt>complement("GATTACA")</tt> should return 
<tt>"CTAATGT"</tt>. (You may assume the input is valid, there is no need
to check for non-DNA characters.)

"""

lang = "C++func"

source_code = r"""
#include <iostream>
#include <string>
using namespace std;

// replace all 'C's with 'G's and vice-versa
// replace all 'A's with 'T's and vice-versa
string complement(string dna) {
\[
   string result = dna; // create string of same length
   int n = dna.length();
   for (int i=0; i<n; i++) {
      if (dna[i] == 'C')
         result[i] = 'G';
      else if (dna[i] == 'G')
         result[i] = 'C';
      else if (dna[i] == 'A')
         result[i] = 'T';
      else if (dna[i] == 'T')
         result[i] = 'A';
   }
   return result;
]\
}"""

tests = [
    ["check-function", "complement", "string", ["string"]],
    ["call-function", "complement", ['"GAATTACA"']],
    ["call-function", "complement", ['"CAT"']],
    ["call-function", "complement", ['"TAGACAT"']],
    ["call-function", "complement", ['"GCGAGTGAGC"']],
    ["call-function", "complement", ['""']],
]
