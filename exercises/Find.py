source_code = r"""
public static int find(\[int]\ needle, \[int[]]\ haystack) {
   int n = haystack.length;
   for (\[int i=0; i<n; i++]\) {
      // check if this element of haystack equals needle
      if (\[ haystack[i] == needle ]\) 
         // quit immediately with this index
         return \[i]\;
   }
   // if we get this far, the needle was not found
   return -1;
}

public static void main(String[] args) {
   int[] testArr = {1, 2, 6};
   System.out.println("index of 6: " + find(6, testArr));
   System.out.println("index of 2: " + find(2, testArr));
   System.out.println("index of 1: " + find(1, testArr));
   System.out.println("index of 4: " + find(4, testArr));
}
"""

tests = r"""
testMain();
test("find", 1, new int[]{4, 1, 6, 1});
"""

description = r"""
Write a class <code>Find</code> with a method <code>find()</code>
that takes two arguments, an integer <code>needle</code>
and an array of integers <code>haystack</code>. If <code>needle</code>
is one of the elements of <code>haystack</code>, then return the
index at which it appears<sup>*</sup>. Otherwise, if <code>needle</code>
is not one of the elements of the array, return <code>-1</code>.
<div><sup>*</sup>: if it occurs multiple times, return the least-indexed
position</div>"""


