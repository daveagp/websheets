/*
 
Write a program SquareCensus that takes a single command-line argument <code>n</code>,
which is an integer. First, print out all of the positive square numbers less
than or equal to <code>n</code> (in increasing order). Then, print out their 
sum. Use the format shown in this example: <code>java SquareCensus 11</code> should output
<pre>
1
4
9
The sum is 14
</pre>
<i>Try solving it once with a <code>for</code> loop, and once with a
<code>while</code> loop.</i>
 */

public class SquareCensus {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int i = 1;
        int sum = 0;
        while (i*i <= n) {
            System.out.println(i*i);
            sum += i*i;
            i += 1;
        }
        System.out.println("The sum is " + sum);
        // alternate solution:
        // for (int i = 1; i*i <= n; i++) {sum += i*i; System.out.println(i*i);}
    }
}