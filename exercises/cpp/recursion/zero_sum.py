description = r"""
<div>
Is it possible to assign + and &ndash; signs to the numbers
<pre>
1434 3243 343 5 293 3408 123 487 93 12 2984 29
</pre>
so that the sum is 0? With recursion, we can try all possible combinations
of + and &ndash; for each number to find out. There are $2^n$ ways to assign
+ or &ndash; signs to $n$ numbers, and recursion can accomplish this by making
two recursive calls (one for +, one for &ndash;) at each of $n$ levels.
Each branch of the recursive call tree will keep a running sum of the numbers
it has assigned signs so far. 
<p>To implement this in C++,
write a recursive function
<pre>bool canMakeZero(int partialSum, int* nums, int numsLeft)</pre>
which tries every assignment of +/&ndash; signs
<pre>partialSum &pm; nums[0] &pm; nums[1] &pm; &hellip; &pm; nums[numsLeft-1]</pre> 
and returns <tt>true</tt> <b>when any one of the combinations' sum is zero</b>.
</ol>
<p>
Note that our original question is:
<pre>
int nums[12] = {1434, 3243, 343, 5, 293, 3408, 123, 487, 93, 12, 2984, 29};
canMakeZero(0, nums, 12); // call helper function starting with partialSum=0
</pre>
<p>
Make each recursive call pass the pointer <tt>nums+1</tt> in place of 
<tt>nums</tt>, and pass <tt>numsLeft-1</tt> in place of <tt>numsLeft</tt>.
How do the recursive calls combine? What is the base case?
"""

source_code = r"""
#include <iostream>
#include <iomanip>
#include <cstdlib>
using namespace std;

bool canMakeZero(int runningSum, int* nums, int numsLeft) {
\[
   // we've given a sign to all numbers
   if (numsLeft == 0) {
      if (runningSum == 0) 
         return true;  // hit the runningSum
      else
         return false; // missed the runningSum
   }

   // try both possibilities, propagating any hit
   if (canMakeZero(runningSum + nums[0], nums+1, numsLeft-1))
      return true;

   if (canMakeZero(runningSum - nums[0], nums+1, numsLeft-1))
      return true;

   // neither recursive call found a solution
   return false;
]\
}

int main(int argc, char* argv[]) {
   cout << boolalpha;
   if (argc < 2) { // default tests
      int testArr[] = {1434,3243,343,5,293,3408,123,487,93,12,2984,29};
      // should print true because
      // -1434+3243-343-5-293-3408-123-487-93-12+2984-29 = 0
      cout << canMakeZero(0, testArr, 12) << endl; // true
      int testArr2[] = {1, 2};
      // no way to make zero
      cout << canMakeZero(0, testArr2, 2) << endl; // false
   }
   else {
      int n = argc-1;
      int* testArr = new int[n];
      for (int i=0; i<n; i++) testArr[i] = atoi(argv[i+1]);
      cout << canMakeZero(0, testArr, n);
      delete testArr;
   }
}
"""

tests = [
    ["", []],
["", ["1"]*6, ""],
["", ["1"]*7, ""],
["", "1 2 3 4 5 6".split(" "), ""],
["", "1 2 3 4 5 6 7".split(" "), ""],
["", "1000 100000 100 111111 10 1 10000".split(" "), ""],
["", "1000 100000 100 111111 10 1 1000".split(" "), ""],
["", "9 16 25".split(" "), ""],
["", ["0"]*3, ""],
["", "1435 3243 343 5 293 3408 123 487 93 12 2984 29".split(" "), ""],
["", "1434 3253 343 5 293 3408 123 487 93 22 2984 29".split(" "), ""],
["", "129 435 843 234 456 238 587 910".split(" "), ""]
]

lang = "C++"

attempts_until_ref = 0
