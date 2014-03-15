source_code = r"""
public class RegularExercise {

    // regular expression for: all strings that start with G or R
    public static String startsWithGorR = "(G|R).*";

    // regular expression for: all strings that contain a substring "EX"
    public static String containsEX = \[".*EX.*"]\;

    // regular expression for: all strings that do not contain an E
    public static String noE = \["(R|G|X)*"]\;

    // regular expression for: all strings in which every X is followed by a G
    public static String everyXfollowedByG = \["(XG|G|R|E)*"]\;

    // regular expression for: all strings that do not end with X
    public static String doesNotEndWithX = \["(.*(G|R|E))|"]\;
    
    public static void main(String[] args) {
        StdOut.printf("%24s%12s%6s%18s%16s\n", "startsWithGorR", "containsEX",
                      "noE", "everyXfollowedByG", "doesNotEndWithX");
        for (String a : args) {
        StdOut.printf("%8s%16s%12s%6s%18s%16s\n", a, 
                      a.matches(startsWithGorR),
                      a.matches(containsEX),
                      a.matches(noE),
                      a.matches(everyXfollowedByG),
                      a.matches(doesNotEndWithX));
        }
    }
    
}
"""

description = r"""
Complete the program below by defining five strings, each containing a regular
expression to match one of the five languages indicated in the comments.
The first one is filled in for you as an example. 
You may assume that we will only test your program on strings containing
the letters <tt>E</tt>, <tt>G</tt>, <tt>R</tt> and <tt>X</tt>."""

tests = r"""
testMain("REGEX", "GREE", "XRXG", "XX");
test("main", (Object)new String[]{"", "R", "G", "E", "X"});
String[] letters = {"R","G","E","X"};
quietOnPass = true;
for (String a : letters) for (String b : letters)
test("main", (Object)new String[]{a+b});
for (String a : letters) for (String b : letters)
for (String c : letters) 
test("main", (Object)new String[]{a+b+c});
for (String a : letters) for (String b : letters)
for (String c : letters) 
for (String d : letters) 
test("main", (Object)new String[]{a+b+c+d});
for (String a : letters) for (String b : letters)
for (String c : letters) 
for (String d : letters) 
for (String e : letters) 
test("main", (Object)new String[]{a+b+c+d+e});
"""
