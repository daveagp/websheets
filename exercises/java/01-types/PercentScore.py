description = r"""
Compute your average score on a two-part exam.
You will be given 4 command-line arguments:
<ul>
<li>The number of questions you got right on the first part</li>
<li>The total number of questions on the first part</li>
<li>The number of questions you got right on the second part</li>
<li>The total number of questions on the second part</li>
</ul>
Output your percentage score on the exam. For example, for
<pre>PercentScore 8 10 15 17</pre>
since you got a total of 23 questions correct out of 27 
and 23/27 = 0.8518&hellip; you should print
<pre>85.18518518518519</pre>
You may assume the total number of questions is positive.
"""

source_code = r"""
public class PercentScore {
    public static void main(String[] args) {
\[
        int score1 = Integer.parseInt(args[0]);
        int total1 = Integer.parseInt(args[1]);
        int score2 = Integer.parseInt(args[2]);
        int total2 = Integer.parseInt(args[3]);
        // avoid integer division:
        System.out.println(100.0 * (score1 + score2) / (total1 + total2));
]\
    }
}
"""

tests = """
testMain("8", "10", "15", "17");
testMain("10", "10", "5", "5");
testMain(randgen.nextInt(130)+"", "130", randgen.nextInt(70)+"", "70");
testMain(randgen.nextInt(10)+"", 10+randgen.nextInt(12)+"", randgen.nextInt(70)+"", 70+randgen.nextInt(5)+"");
"""

epilogue = r"""
If you used <i>integer division</i> like this,
<pre>100 * (score1 + score2) / (total1 + total2)</pre>
Java interprets this as dividing an integer by an integer,
and will give you an integer answer, which is not correct.
<p>The reference solution shows one correct approach, or you can <i>typecast</i> to a floating-point number before dividing,
like this:
<pre>(double) (score1 + score2) / (total1 + total2) * 100</pre>
"""
