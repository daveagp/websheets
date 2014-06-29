source_code = r"""
\[
/******************************************************************* 
 Reference solution for Spring 2013 COS 126 Programming Exam 1
 Foodlympics Part Two: Gourmet Glory

 Author:       COS 126 Staff
 Netid:        cos126
 Precepts:     lots of them
 Dependencies: StdIn, StdOut
 Usage:        java FoodPart2 N
 
 Description:  Reads in names and scores for C countries. Prints out the N
               top-score countries in order. 
   
**************************************************************************/

    // find the highest value in scores. set this value to 0, and 
    // return the corresponding element of countries.
    public static String best(String[] countries, int[] scores) {
        // number of countries
        int C = countries.length;

        // bestIndex is the index of the (earliest) max-score country
        int bestIndex = -1; 
        
        // max is the maximum score seen so far
        int max = Integer.MIN_VALUE;
        
        // find index of max-score country
        for (int i = 0; i < C; i++) {
            if (scores[i] > max) {
                max = scores[i];
                bestIndex = i;
            }
        }
        
        // do required update and return the winner
        scores[bestIndex] = 0;
        return countries[bestIndex];
    }

    // read in a file of scores, and take N from the command-line.
    // then print out the top N ranking countries from best to worst.
    public static void main(String[] args) {

        int C = StdIn.readInt();           // number of countries
        int N = Integer.parseInt(args[0]); // how many to rank

        String[] countries = new String[C];
        int[] scores = new int[C];

        // read the rest of the input
        for (int i = 0; i < C; i++) {
            countries[i] = StdIn.readString();
            scores[i] = StdIn.readInt();
        }
        
        // now print the results
        for (int i = 0; i < N; i++) {
            String nextRanked = best(countries, scores);
            StdOut.println("Rank " + (i+1) + ": " + nextRanked);
        }
    }
]\
"""

description = r"""
<i>COS 126 Spring 2013 Programming Midterm 1, part 1/2</i><br>
Please see the problem description in <a href="http://www.cs.princeton.edu/courses/archive/fall13/cos126/docs/mid1-s13-prog.pdf">
this PDF link</a>.
<p>
This websheet is intended as a practice exam. However, in a real exam,
<ul>
<li>You'll upload via Dropbox
<li>You'll get limited feedback from Dropbox during the exam, and a different full set of test cases for grading
<li>Real humans will grade your real exams and also mark you on style and apply partial credit where appropriate
<li>Because of Websheet formatting, on this page you have to put your header inside the class. On the exam, put it at the top as usual
<li>We recommend coding in DrJava and/or the command-line and doing basic tests on your own, then copying here for full testing
</ul>
We recommend doing this practice in a timed environment; give yourself 90 minutes.
"""

tests = r"""
test("best", new String[]{"SAA", "BOH"}, new int[]{5, 10});
test("best", new String[]{"SAA", "BOH"}, new int[]{5, 0});
test("best", new String[]{"Japan", "USA", "Mali", "Cuba", "Togo"}, new int[]{13, 15, 17, 19, 14});
test("best", new String[]{"Japan", "USA", "Mali", "Cuba", "Togo"}, new int[]{13, 15, 17, 0, 14});
stdinURL = "http://www.cs.princeton.edu/~cos126/docs/data/Food/naScores.txt";
testMain("3");
stdinURL = "http://www.cs.princeton.edu/~cos126/docs/data/Food/germanScores.txt";
testMain("2");
test("best", new String[]{"Pangaea"}, new int[]{10});
test("best", new String[]{"LO", "HI"}, new int[]{5, 10});
test("best", new String[]{"HI", "LO"}, new int[]{10, 5});
test("best", new String[]{"EQ", "EQUAL"}, new int[]{8, 8});
test("best", new String[]{"big", "small", "bigagain", "smallagain"}, new int[]{20, 1, 20, 1});
test("best", new String[]{"big", "small", "bigagain", "smallagain"}, new int[]{0, 1, 20, 1});
test("best", new String[]{"big", "small", "bigagain", "smallagain"}, new int[]{0, 1, 0, 1});
test("best", new String[]{"big", "small", "bigagain", "smallagain"}, new int[]{0, 0, 0, 1});
stdin = "1\nPangaea 10"; testMain("1");
stdin = "2\nA 5\nB 5"; testMain("2");
stdin = "2\nA 5\nB 8"; testMain("2");
stdin = "2\nA 8\nB 5"; testMain("2");
stdin = "3\nA 8\nB 8\nC 1"; testMain("3");
stdin = "4\nA 8\nB 5\nC 8\nD 5"; testMain("1");
stdin = "4\nA 8\nB 5\nC 8\nD 5"; testMain("4");
stdin = "7\nA 8\nB 6\nC 7\nD 5\nE 3\nF 10\nG 9"; testMain("3");
stdin = "7\nA 8\nB 6\nC 7\nD 5\nE 3\nF 10\nG 9"; testMain("7");
stdin = "9\nA 3\nB 14\nC 15\nD 9\nE 2\nF 6\nG 5\nH 3\nI 5"; testMain("1");
stdin = "9\nA 3\nB 14\nC 15\nD 9\nE 2\nF 6\nG 5\nH 3\nI 5"; testMain("3");
stdin = "9\nA 3\nB 14\nC 15\nD 9\nE 2\nF 6\nG 5\nH 3\nI 5"; testMain("9");
"""
