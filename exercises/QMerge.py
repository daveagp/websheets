source_code = r"""
// ASSUMING a and b are sorted in increasing order, return a new queue
// consisting of the elements of both in combined increasing order
public static Queue<Integer> merge(Queue<Integer> a, Queue<Integer> b) {
   Queue<Integer> result = new Queue<Integer>();

   // keep going as long as there are elements to merge
   while (\[!a.isEmpty() && !b.isEmpty()]\) {
      // take the smaller element from either a or b, move it to result
\[
      if (b.peek() < a.peek())
         result.enqueue(b.dequeue());
      else
         result.enqueue(a.dequeue());
]\
   }

   // if anything is left over once one queue is empty, move it into result
\[
   while (!a.isEmpty())
      result.enqueue(a.dequeue());
   while (!b.isEmpty())
      result.enqueue(b.dequeue());
]\
   return result;
}

// return a new queue consisting of the same elements in sorted order
public static Queue<Integer> mergeSort(Queue<Integer> input) {
   if (input.size() == 1) {  // base case
      Queue<Integer> result = new Queue<Integer>();
\[
      result.enqueue(input.dequeue());
]\
      return result;
   }
   else {
      // move half the elements into a new queue
\[
      int halfSize = input.size() / 2; 
      Queue<Integer> firstHalf = new Queue<Integer>();
      for (int i=0; i<halfSize; i++) 
         firstHalf.enqueue(input.dequeue());
]\
      // sort both halves and merge
      return \[merge(mergeSort(firstHalf), mergeSort(input))]\;
   }
}

// read all integers from input, sort them, and print them
public static void main(String[] args) {
   Queue<Integer> data = new Queue<Integer>();
   while (!StdIn.isEmpty())
      data.enqueue(StdIn.readInt());
   Queue<Integer> sortedData = mergeSort(data);
   while (!sortedData.isEmpty())
      StdOut.println(sortedData.dequeue());
}
"""

tests = r"""
saveAs = "q1";
construct("stdlibpack", "Queue", "<Integer>");
testOn("q1", "enqueue", 1);
testOn("q1", "enqueue", 6);
saveAs = "q2";
construct("stdlibpack", "Queue", "<Integer>");
testOn("q2", "enqueue", 2);
testOn("q2", "enqueue", 9);
saveAs = "q";
test("merge", var("q1"), var("q2"));
testOn("q", "size");
testOn("q", "dequeue");
testOn("q", "dequeue");
testOn("q", "dequeue");
testOn("q", "dequeue");
testOn("q", "isEmpty");
testStdin = "3 7 8 2 4 5 2 4 1";
testMain();
testStdin = "3 7 8 2 4 5 2 4 1";
testMain();
testStdinURL = "http://www.cs.princeton.edu/~cos126/websheets/data/100rand126.txt";
testMain();
testStdinURL = "http://www.cs.princeton.edu/~cos126/websheets/data/10000rand.txt";
testMain();
"""

description = r"""
Write code to sort a list of integers using merge sort. You will use the <tt>Queue&lt;Integer&gt;</tt> parameterized generic type. 
<ol>
<li>
Create a static method <tt>Queue&lt;Integer&gt; merge(Queue&lt;Integer&gt; a, Queue&lt;Integer&gt; b)</tt> which, assuming
 <tt>a</tt> and <tt>b</tt> are both queues sorted in increasing order, returns a new queue
consisting of all their elements combined, sorted in increasing order. E.g., if <tt>a</tt> is a queue into which
1 and 6 have been enqueued, and <tt>b</tt> is a queue into which 2 and 9 have been enqueued, then the returned
queue should contain 1 first, then 2, 6, 9. 
</li>
<li>
Then, create a static method <tt>Queue&lt;Integer&gt; mergeSort(Queue&lt;Integer&gt; input)</tt> to implement merge sort.
It should use <tt>size()</tt> from the <tt>Queue</tt> API to break the queue arbitrarily into two 
(non-ordered) queues each about half as big as the original. Then sort both halves recusrively, and merge them.
</li>
</ol>
"""

