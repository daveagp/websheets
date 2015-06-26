lang = "C++"

source_code = r"""
#include <iostream>
#include <deque>
using namespace std;

// ASSUMING a and b are sorted in increasing order, return a new queue
// consisting of the elements of both in combined increasing order
deque<int> merge(deque<int> a, deque<int> b) {
   deque<int> result;

   // keep going as long as there are elements to merge in BOTH
   while (\[!a.empty() && !b.empty()]\) {
      // take the smaller element from either a or b, move it to result
\[
      if (b.front() < a.front()) {
         result.push_back(b.front());
         b.pop_front();
}
      else {
         result.push_back(a.front());
         a.pop_front();
}
]\
   }

   // if anything is left over once one queue is empty, move it into result
\[
   while (!a.empty()) {
      result.push_back(a.front());
      a.pop_front();
   }
   while (!b.empty()) {
      result.push_back(b.front());
      b.pop_front();
   }
]\
   return result;
}

// return a new queue consisting of the same elements in sorted order
deque<int> merge_sort(deque<int> input) {
   if (input.size() == 1) {  // base case
\[
      return input;
]\
   }
   else {
      // move half the elements into a new queue
\[
      int halfSize = input.size() / 2; 
      deque<int> firstHalf;
      for (int i=0; i<halfSize; i++) {
         firstHalf.push_back(input.front());
         input.pop_front();
      }
]\
      // sort both halves and merge
      return \[merge(merge_sort(firstHalf), merge_sort(input))]\;
   }
}

// read all integers from input, sort them, and print them
int main(int argc, char* argv[]) {
   deque<int> data;
   int value;
   while (cin >> value)
      data.push_back(value);
   deque<int> sortedData = merge_sort(data);
   while (!sortedData.empty()) {
      cout << sortedData.front() << " ";
      sortedData.pop_front();
   }
}
"""

import random as _random

tests = [
["9 1 6 2", []],
["3 7 8 2 4 5 2 4 1", []],
[" ".join(str(_random.randint(1, 100)) for _ in range(100)), []],
]

description = r"""
Write code to sort a list of integers using merge sort. You will use the <tt>deque&lt;int&gt;</tt> template type.
<ol>
<li>
Create a function <tt>deque&lt;int&gt; merge(deque&lt;int&gt; a, deque&lt;int&gt; b)</tt> which, assuming
 <tt>a</tt> and <tt>b</tt> are both deques sorted in increasing order, returns a new deque
consisting of all their elements combined, sorted in increasing order. E.g., if <tt>a</tt> is a deque into which
1 and 9 have been inserted, and <tt>b</tt> is a deque into which 2 and 6 have been inserted, then the returned
deque should contain 1 first, then 2, 6, 9. 
</li>
<li>
Then, create a function <tt>deque&lt;int&gt; merge_sort(deque&lt;int&gt; input)</tt> to implement merge sort.
It should use <tt>size()</tt> from the <tt>deque</tt> API to break the deque into two 
(non-ordered) deques each about half as big as the original. Then sort both halves recursively, and merge them.
</li>
</ol>
 You will also need to use 
<tt>bool deque::empty()</tt> as well as <tt>push_back()</tt>, <tt>front()</tt> and <tt>pop_front()</tt>.
"""

attempts_until_ref = 0
