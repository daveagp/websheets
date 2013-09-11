/*

Write a program <code>ModularSqrt</code> that takes two command-line
arguments, <code>remainder</code> and <code>modulus</code>. 
It should print 
out all of the integers <code>i</code> between <code>0</code> and
<code>modulus-1</code>
with the property that <code>(i*i) % modulus</code> equals 
<code>remainder</code>, and a count of how many integers were found. 
Use the format shown in this example:
<code>java ModularSqrt 9 10</code> should print out
<pre>
3
7
2 square roots were found
</pre>
since 3<sup>2</sup>=9 and 7<sup>2</sup>=49 are the only squares between 
0<sup>2</sup> and 
9<sup>2</sup>
whose square is 9 mod 10.

*/

public class ModularSqrt {
    public static void main(String[] args) {
        int remainder = Integer.parseInt(args[0]);
        int modulus = Integer.parseInt(args[1]);
        int count = 0;
        for (int i=0; i<modulus; i++) {
            if ((i*i) % modulus == remainder) {
                System.out.println(i);
                count += 1;
            }
        }
        System.out.println(count + " square roots were found");
    }
}