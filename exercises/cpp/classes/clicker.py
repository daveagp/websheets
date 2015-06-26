attempts_until_ref = 0

lang = "C++"

description = r"""
When you go in to a bar or place with a seating capacity, often
the person at the front has a "clicker" to keep track of how many 
people go in or out. Build a <tt>Clicker</tt> class to do this; it should 
have the following API.
<ul>
<li><tt>Clicker()&nbsp; // constructor, make new clicker with value 0</tt>
<li><tt>void inc() // add one to the current value</tt>
<li><tt>void dec() // subtract one from the current value</tt>
<li><tt>int curr() // return the current value</tt>
</ul>
Negative clicker values should be permitted.
"""

source_code = r"""
#include <iostream>
using namespace std;

// normally this would go in clicker.h
class Clicker {
public:
   Clicker();  // constructor
   void inc(); // 3 member functions
   void dec();
   int curr();
private:
// private instance variable(s) you will use are declared here:
\[
      int value;
]\
};

// constructor, make new clicker with value 0
Clicker::Clicker() {
\[
   value = 0;
]\
}
// add one to the current value
void Clicker::inc() {
\[
   value++;
]\
}

// subtract one from the current value
\[
void Clicker::dec() {
   value--;
}
]\

// return the current value
\[
int Clicker::curr() {
   return value;
}
]\

// testing suite
int main() {
   Clicker myClick;
   cout << myClick.curr() << endl; // should be 0
   myClick.inc();
   myClick.inc();
   cout << myClick.curr() << endl; // should be 2
   myClick.dec();
   myClick.dec();
   myClick.dec();
   cout << myClick.curr() << endl; // should be -1

   Clicker clickMore;
   cout << clickMore.curr() << endl; // should be 0
   clickMore.inc();
   clickMore.inc();
   clickMore.inc();
   cout << clickMore.curr() << endl; // should be 3

   // check that both clickers have separate variables
   cout << myClick.curr(); // should still be -1
}
"""

tests = [["", []]]
