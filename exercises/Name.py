source_code = r"""
// instance variables
char firstInitial;
String lastName;

// constructor, takes two parameters
public Name(char firstInit, String lastName) {
   // instance variable firstInitial copies constructor parameter firstInit
   firstInitial = firstInit;

   // instance variable lastName copies constructor parameter lastName
   \[this.lastName]\ = \[lastName]\;

   // Hints:

   // "lastName = lastName;" won't work;
   // it copies the parameter into itself.

   // "String lastName = lastName;" won't work; it creates a local 
   // variable in the constructor but doesn't affect the instance.

   // You will need to use the Java keyword "this".
}

// print name of person corresponding to this instance
public void display() {
   StdOut.println(firstInitial + ". " + lastName);
}

// test client
public static void main(String[] args) {
   Name n = new Name('R', "Sedgewick");
   n.display();
}
"""

description = r"""
The <tt>Name</tt> class stores someone's first initial and last name.
Complete the missing line in the constructor.
"""

tests = r"""
testMain();
"""
