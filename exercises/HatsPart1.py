description = r"""
<i>COS 126 Fall 2012 Programming Midterm 1, part 1/2</i><br>
Please see the problem description in <a href="http://www.cs.princeton.edu/courses/archive/fall13/cos126/docs/mid1-f12-prog.pdf">
this PDF link</a>. Please use the alternate URL
<pre>
<a href="http://www.cs.princeton.edu/~cos126/docs/data/Hats/">http://www.cs.princeton.edu/~cos126/docs/data/Hats/</a>
</pre> to access
the sample input files.
<p>
This websheet is intended as a practice exam. However, in a real exam,
<ul>
<li>You'll upload via Dropbox
<li>You'll get limited feedback from Dropbox during the exam, and a different full set of test cases for grading
<li>Real humans will grade your real exams and also mark you on style and apply partial credit where appropriate
<li>Because of Websheet formatting, on this page you have to put your header inside the class. On the exam, put it at the top as usual
<li>We recommend coding in DrJava and/or the command-line and doing basic tests on your own, then copying here for full testing
<li>The exam grader is generally less picky about output whitespace than the Websheet grader.
</ul>
We recommend doing this practice in a timed environment; give yourself 90 minutes.
"""

source_code = r"""\[
/*********************************************************************** 
Christopher Moretti
cmoretti
P01A/P06

Read in list size and permutations of that size.
Determine if each is a "derangement". 
Print out the first derangement if it exists.
Print out the number of derangements.

Requires StdIn and StdOut
***********************************************************************/

    // print the first derangement with the given format
    private static void printD(int[] r) {
        StdOut.print("First derangement:");
        for (int i = 0; i < r.length; i++)
            StdOut.print(" "+r[i]);
        StdOut.println();
    }
    
    // return true if r holds a derangement, false otherwise
    public static boolean isD(int[] r) {
        for (int i = 0; i < r.length; i++) {
            if (r[i] == i+1) //i+1 to account for Java 0-based arrays
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        // the # of items in permutation
        int N = StdIn.readInt(); 

        // space to hold permutation
        int[] arr = new int[N]; 

        // how many derangements have we seen?
        int count = 0;          
        
        // Read until there are no more permutations left on StdIn.
        while (!StdIn.isEmpty()) {
            // fill array
            for (int i = 0; i < N; i++)
                arr[i] = StdIn.readInt();

            // if arr is a derangement, count i
            // and print it if it's the first.
            if (isD(arr)) { 
                if (count == 0) 
                    printD(arr); 
                count++; 
            }
        }

        // print the count with the given format
        StdOut.println("Number of derangements: " + count);
    }
]\ 
"""

tests = r"""
test("isD", (Object)new int[]{3, 4, 1, 5, 2, 6});
test("isD", (Object)new int[]{1, 3, 4, 5, 6, 2});
test("isD", (Object)new int[]{3, 1, 4, 2, 6, 5});
test("isD", (Object)new int[]{1, 2, 3, 4, 5, 6, 7, 8});
test("isD", (Object)new int[]{8, 7, 6, 5, 4, 3, 2, 1});
test("isD", (Object)new int[]{9, 8, 7, 6, 5, 4, 3, 2, 1});
test("isD", (Object)new int[]{1});
test("isD", (Object)new int[]{2, 1});
test("isD", (Object)new int[]{1, 2});
testStdin = "9\n9 8 7 6 5 4 3 2 1\n3 7 6 9 8 2 1 5 4";
testMain();
testStdin = "6\n1 2 6 4 3 5\n6 1 5 4 3 2";
testMain();
testStdinURL = "http://www.cs.princeton.edu/~cos126/docs/data/Hats/5perms9.txt";
testMain();
testStdinURL = "http://www.cs.princeton.edu/~cos126/docs/data/Hats/1000perms15.txt";
testMain();
"""
