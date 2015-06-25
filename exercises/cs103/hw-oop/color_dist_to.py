
source_code = r"""
#include <cmath>
#include <iostream>
using namespace std;

class Color {
public:
   // constructor declaration
   Color(int r, int g, int b);
   // member function declaration
   double dist_to(Color other_color);
private:
   // data members
   int red;
   int green;
   int blue;
};

\fake[
Color::Color(int r, int g, int b){...} // assume this is still defined for you
]\
\hide[
Color::Color(int r, int g, int b) {
   red = r; 
   green = g; 
   blue = b;
}
]\

double sqr(double x) {
   return x*x;
}

// member function definition
double Color::dist_to(Color other_color) {
   return sqrt( sqr(\[red - other_color.red]\)
      + sqr(\[green - other_color.green]\)
      + sqr(\[blue - other_color.blue]\));
}

int main() {
   Color magenta(255, 0, 255);
   Color cyan(0, 255, 255);
   Color azure(0, 127, 255);

   // call member function
   cout << magenta.dist_to(cyan) << endl;
   cout << azure.dist_to(magenta) << endl;
   // you also should print out distance from cyan to azure
   cout << \[cyan.dist_to(azure)]\ << endl;

   return 0;
}
"""

description = r"""
It's generally bad practice to leave your data members as <tt>public</tt>.
So in this example, we make them <tt>private</tt>. Since a non-member 
function can't access <tt>private</tt> variables, we'll also replace
<tt>dist</tt> with a member function <tt>dist_to</tt> which can be called like
<pre>magenta.dist_to(cyan)</pre>
"""

lang = "C++"

tests = [["", []]]

