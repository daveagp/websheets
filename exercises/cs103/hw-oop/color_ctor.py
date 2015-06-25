
source_code = r"""
#include <cmath>
#include <iostream>
using namespace std;

class Color {
public:
   // constructor declaration
   Color(int r, int g, int b);
   // data members
   int red;
   int green;
   int blue;
};

double dist(Color c1, Color c2); // assume this is still defined for you.

\hide[
double sqr(double x) {
   return x*x;
}

double dist(Color c1, Color c2) {
   return sqrt( sqr( c1.red-c2.red   )
      + sqr( c1.green-c2.green )
      + sqr( c1.blue-c2.blue     ));
}
]\
// constructor definition
Color::Color(int r, int g, int b) {
   red = r; // copy passed-in value into object 
\[ 
   green = g; 
   blue = b;
]\
}

int main() {
   // construct three objects (call constructor)
   Color magenta(255, 0, 255);
   Color cyan(0, 255, 255);
   Color azure(0, 127, 255);

   cout << dist(magenta, cyan) << endl;
   cout << dist(magenta, azure) << endl;
   cout << dist(cyan, azure) << endl;

   return 0;
}
"""

description = r"""
The previous exercise got tedious when we wanted to create a new 
color: we had to set all three values individually. For this exercise,
create a constructor.
<p>
<i>The job of any constructor is to initialize all of the data members.</i>
(The data members are the variables inside the class definition.)
"""

lang = "C++"

tests = [["", []]]

