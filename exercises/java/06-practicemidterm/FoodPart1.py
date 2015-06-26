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

source_code = r"""\[
/*******************************************************************
 Reference solution for Spring 2013 COS 126 Programming Exam 1
 Foodlympics Part One: Competitive Cuisine

 Author:       COS 126 Staff
 Netid:        cos126
 Precepts:     lots of them
 Dependencies: StdIn, StdOut
 Usage:        java FoodPart1 
 
 Description:  Reads in judge rankings for C countries by J judges.
               Prints out the rounded average score for each country,
               excluding the min and max.

**************************************************************************/

    // excluding the min and max, compute the rounded average
    // of the entries of judgeRatings
    public static int score(int[] judgeRatings) {

        int J = judgeRatings.length;              
        int sum = 0;

        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < J; i++) {
            min = Math.min(min, judgeRatings[i]);
            max = Math.max(max, judgeRatings[i]);
            sum += judgeRatings[i];
        }                                         

        // eliminate min and max
        sum = sum - min - max;
        
        // average
        double ave = sum / (double) (J - 2);
        
        // rounded average, excluding min and max
        int score = (int) Math.round(ave);
        return score;
    }

    // read the judges' ratings for several countries
    // from standard input and print their overall scores
    // to standard output
    public static void main(String[] args) {
        int C = StdIn.readInt(); // number of countries
        int J = StdIn.readInt(); // number of judges

        StdOut.println(C);       // first line of output

        // for each country, process their ratings
        for (int i = 0; i < C; i++) {

            // read the next line of input
            String name = StdIn.readString();
            int[] ratings = new int[J];
            for (int j = 0; j < J; j++)
                ratings[j] = StdIn.readInt();

            // compute the overall score
            int overall = score(ratings);

            // output for this country
            StdOut.println(name + " " + overall);
        }
    }
]\
"""

tests = r"""
test("score", (Object)new int[]{7, 14, 20, 12, 15, 16});
test("score", (Object)new int[]{10, 16, 10, 20, 14, 10});
stdinURL = "http://www.cs.princeton.edu/~cos126/docs/data/Food/german.txt";
testMain();
stdinURL = "http://www.cs.princeton.edu/~cos126/docs/data/Food/na.txt";
testMain();
test("score", (Object)new int[]{15, 5, 10});
test("score", (Object)new int[]{7, 7, 7});
test("score", (Object)new int[]{4, 8, 12, 16});
test("score", (Object)new int[]{4, 5, 10, 12});
test("score", (Object)new int[]{4, 5, 8, 12});
test("score", (Object)new int[]{20, 19, 20, 19, 20});
test("score", (Object)new int[]{1, 2, 1, 2, 1});
stdin = "1 3\nPangaea 8 8 8";
testMain();
stdin = "6 3\nLMH 1 2 3\nLHM 4 6 5\nMLH 8 7 9\nMHL 11 12 10\nHLM 15 13 14\nHML 18 17 16";
testMain();
stdin = "6 3\nLLH 1 1 9\nLHL 1 9 1\nHLL 9 1 1\nLHH 1 9 9\n HLH 9 1 9\nHHL 9 9 1";
testMain();
stdin = "2 3\noneLand 1 1 1\ntwentyStan 20 20 20";
testMain();
stdin = "4 4\nmaxRepeat 18 18 7 5\nminRepeat 6 6 12 19\nbothRepeat 4 4 12 12\nfours 4 4 4 4";
"""
