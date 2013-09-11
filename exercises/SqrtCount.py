/*

This program builds on <b>ModularSqrt</b>, by adding two iterative
levels of complexity. You will take one command-line integer <code>n</code>.
Print out a table with <code>n<code> rows: the first corresponds to a modulus of 1,
the second corresponds to a modulus of 2, and so on with the last row corresponding
to a modulus of <code>n</code>. Within each row, consider all values of 
<code>remainder</code> from <code>0</code> to <code>modulus - 1</code>,
and print out how many square roots <code>remainder</code> has modulo 
<code>modulus</code>. For example, <code>SqrtCount 5</code> should print out
<pre>
1
11
120
2200
12002
</pre>
where the last row indicates that modulo 5, 0 has one square root,
1 has two square roots, 2 has no square roots, 3 has no square roots, and 
4 has two square roots.

*/

public class SqrtCount {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        for (int modulus=1; modulus<=n; modulus++) {
            for (int remainder=0; remainder<modulus; remainder++) {
                int count = 0;
                for (int i=0; i<modulus; i++) {
                    if ((i*i) % modulus == remainder) {
                        count += 1;
                    }
                }
                System.out.print(count);
            }
            System.out.println();
        }
    }
}