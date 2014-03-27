description = r"""
<i>COS 126 Spring 2010 Programming Midterm 2</i><br>
Please see the problem description in <a href="http://www.cs.princeton.edu/courses/archive/fall13/cos126/docs/mid2b-s10.pdf">
this PDF link</a>. 
<p>
This websheet is intended as a practice exam. However, in a real exam,
<ul>
<li>You'll upload via Dropbox
<li>You'll get limited feedback from Dropbox during the exam, and a different full set of test cases for grading
<li>Real humans will grade your real exams and also mark you on style and apply partial credit where appropriate
<li>We recommend coding in DrJava and/or the command-line and doing basic tests on your own, then copying here for full testing
</ul>
We recommend doing this practice in a timed environment; give yourself 90 minutes.
"""

source_code = r"""
public class BinaryInteger {
\[
   private final int N;      // number of bits
   private final String s;   // bit string

   // create a binary integer from a string of 0s and 1s
   public BinaryInteger(String s) {
      if (!s.matches("[01]*")) {
         throw new RuntimeException("Illegal argument to BinaryInteger()");
      }
      this.s = s;
      this.N = s.length();
   }

   // length of this binary integer
   public int length() {
      return N;
   }

   // number of leading zeros in this binary integer
   public int leadingZeros() {
      int count = 0;
      for (int i = N-1; i >= 0; i--) {
         if (!ith(i)) count++;
         else break;
      }
      return count;
   }

   // is this binary integer strictly greater than that binary integer?
   public boolean isGreaterThan(BinaryInteger that) {
      int n1 = this.length() - this.leadingZeros();
      int n2 = that.length() - that.leadingZeros();
      if (n1 > n2) return true;
      if (n1 < n2) return false;
      for (int i = n1 - 1; i >= 0; i--) {
         if (this.ith(i) && !that.ith(i)) return true;
         if (that.ith(i) && !this.ith(i)) return false;
      }
      return false;   // equal
   }

   // return the ith least significant bit as a boolean
   private boolean ith(int i) {
      if      (s.charAt(N - i - 1) == '0') return false;
      else if (s.charAt(N - i - 1) == '1') return true;
      else throw new RuntimeException("Inconsisent state");
   }

   // return the bitwise xor of this binary integer and that binary integer
   public BinaryInteger xor(BinaryInteger that) {
      if (this.N != that.N) throw new RuntimeException("Size mismatch");
      String answer = "";
      for (int i = 0; i < N; i++) {
         if (this.ith(i) ^ that.ith(i)) answer = "1" + answer;
         else                           answer = "0" + answer;
      }
      return new BinaryInteger(answer);
   }

   // return the bitwise not of this binary integer
   public BinaryInteger not() {
      String answer = "";
      for (int i = 0; i < N; i++) {
         if (this.ith(i)) answer = "0" + answer;
         else             answer = "1" + answer;
      }
      return new BinaryInteger(answer);
   }

   // return string representation of this binary integer
   public String toString() {
       return s;
   }
]\
}
"""
tests = r"""
saveAs = "a";
testConstructor("00011110");
saveAs = "b";
testConstructor("01010000");
testOn("a", "toString");
testOn("b", "toString");
testOn("a", "length");
testOn("b", "length");
saveAs = "notA";
testOn("a", "not");
testOn("notA", "toString");
saveAs = "x";
testOn("a", "xor", var("b"));
testOn("x", "toString");
testOn("a", "leadingZeros");
testOn("a", "isGreaterThan", var("b"));

saveAs = "sextillion";
testConstructor("1101100011010111001001101011011100010111011110101000000000000000000000");
testOn("sextillion", "toString");
testOn("sextillion", "length");
testOn("sextillion", "leadingZeros");
saveAs = "lengthyZero";
testOn("sextillion", "xor", var("sextillion"));
testOn("lengthyZero", "toString");
testOn("lengthyZero", "leadingZeros");

saveAs = "one";
testConstructor("00000001");
testOn("one", "leadingZeros");
expectException = true;
testOn("one", "xor", var("sextillion"));

saveAs = "zero";
testConstructor("00000000");
testOn("zero", "leadingZeros");
testOn("one", "isGreaterThan", var("zero"));
testOn("zero", "isGreaterThan", var("zero"));
testOn("zero", "isGreaterThan", var("one"));
testOn("one", "isGreaterThan", var("one"));

saveAs = "ten";
testConstructor("00001010");
testOn("one", "isGreaterThan", var("ten"));
testOn("ten", "isGreaterThan", var("one"));

expectException = true; testConstructor("1111A");
expectException = true; testConstructor("21111");
expectException = true; testConstructor(" 11111");
expectException = true; testConstructor("0000 ");

saveAs = "emptyStringIsLegal";
testConstructor("");
testOn("emptyStringIsLegal", "toString");
testOn("emptyStringIsLegal", "leadingZeros");

saveAs = "three";
testConstructor("011");
saveAs = "paddedFour";
testConstructor("00000100");
testOn("three", "isGreaterThan", var("paddedFour"));
testOn("paddedFour", "isGreaterThan", var("three"));
testOn("lengthyZero", "isGreaterThan", var("zero"));
testOn("zero", "isGreaterThan", var("lengthyZero"));
"""
