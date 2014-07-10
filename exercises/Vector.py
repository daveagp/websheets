description = r"""
<i>Booksite section 3.4.</i> This class is an implementation of a vector of real numbers.
It should be immutable: once the client
   initializes a <tt>Vector</tt>, they cannot change any of its fields
   either directly or indirectly. 
For example, the instance method <tt>double cartesian(int i)</tt> will return the <tt>i</tt>th coordinate,
but we will never allow the client to directly access the array in which we store the data, because
we don't want the client to be able to change it.
"""

source_code = r"""
public class Vector {
   
   private\[int N]\;              // length of the vector
   private double[] data;       // array of vector's components

   // create the zero vector of length N
   public Vector(int N) {
      this.N = N;
      this.data = new double[N];
   }

   // create a vector from an array
   public Vector(double[] d) {
     \[N = d.length;]\ // initialize the length

      // make defensive copy so that client can't alter our copy of data[]
\[
      this.data = new double[N]; // using "this" on these lines is optional
      for (int i = 0; i < N; i++)
         this.data[i] = d[i];
\show:
      double[] data = d; //<-- this isn't it!


]\
   }

    // return this + that
    public Vector plus(Vector that) {
        if (this.N != that.N) 
           throw new RuntimeException("Dimensions don't agree");
        Vector c = new Vector(N);
        for (int i = 0; i < N; i++)
            c.data[i] = this.data[i] + that.data[i];
        return c;
    }

    // return this - that
    public Vector minus(Vector that) {
        if (this.N != that.N) 
           throw new RuntimeException("Dimensions don't agree");
        Vector c = new Vector(N);
        for (int i = 0; i < N; i++)
            c.data[i] = this.data[i] - that.data[i];
        return c;
    }

    // create and return a new object whose value is (this * factor)
    public Vector times(double factor) {
        Vector c = new Vector(N);
        for (int i = 0; i < N; i++)
            c.data[i] = factor * data[i];
        return c;
    }

    // return the corresponding unit vector
    public Vector direction() {
        if (this.magnitude() == 0.0) 
           throw new RuntimeException("Zero-vector has no direction");
        return this.times(1.0 / this.magnitude());
    }

    // return the inner product of Vectors this and that
    public double dot(Vector that) {
\[
        if (this.N != that.N) 
           throw new RuntimeException("Dimensions don't agree");
        double sum = 0.0;
        for (int i = 0; i < N; i++)
            sum = sum + (this.data[i] * that.data[i]);
        return sum;
]\
        // remark: is used with "this" in the magnitude() method
    }

    // return the Euclidean norm of this Vector
    public double magnitude() {
        // magnitude is dot product with self, square rooted
        return Math.sqrt(this.dot(this));
    }

    // return the corresponding coordinate
    public double cartesian(int i) {
        return data[i];
    }

    // return a string representation of the vector
    // e.g. (1.0, 2.0, 6.0); format specifiers not required
    public String toString() {
\[
        String s = "(";
        for (int i = 0; i < N; i++) {
            s += data[i];
            if (i < N-1) s+= ", "; 
        }
        return s + ")";
]\
    }

    // partial test client
    public static void main(String[] args) {
        System.out.println("Immutability test:");
        // is it really immutable?
        double[] c = {3.0, 4.0};
        Vector v = new Vector(c);
        System.out.println("v = " + v); // should be (3.0, 4.0)
        c[0] = 0;
        System.out.println("v = " + v); // should still be (3.0, 4.0)!!
    }
}
"""

tests = r"""

defaultOptions.cloneForStudent = false;
double[] nums = new double[]{3, -4};
saveAs = "nums";
store(nums);
saveAs = "velocity";
testConstructor(var("nums"));
defaultOptions.cloneForStudent = true;

testOn("velocity", "cartesian", 0);
testOn("velocity", "cartesian", 1);
remark("Setting <tt>nums[0] = 100</tt> to check for aliasing&hellip;");
nums[0] = 100;
testOn("velocity", "cartesian", 0);


testOn("velocity", "magnitude");
testOn("velocity", "toString");
testOn("velocity", "dot", var("velocity"));
testMain();
saveAs = "x";
testConstructor(new double[]{1, 2, 3, 4});
testOn("x", "toString");
saveAs = "y";
testConstructor(new double[]{5, 2, 4, 1});
testOn("y", "toString");
saveAs = "sum";
testOn("x", "plus", var("y"));
testOn("sum", "toString");
saveAs = "scaled";
testOn("x", "times", 10.0);
testOn("scaled", "toString");
testOn("x", "magnitude");
testOn("x", "dot", var("y"));
saveAs = "yx";
testOn("x", "minus", var("y"));
testOn("yx", "magnitude");
"""
