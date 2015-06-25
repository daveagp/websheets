
source_code = r"""
#include <cmath>
#include <iostream>
using namespace std;

class Color {
public:
   // constructor
   Color(int r, int g, int b);
   // member functions
   void swap_with(Color* other_color);
   double dist_to(Color other_color);
private:
   // data members
   int red;
   int green;
   int blue;
};

\fake[
Color::Color(int r, int g, int b){...} // assume this is still defined for you
Color::dist_to(Color other_color){...} // this too
]\
\hide[
double sqr(double x) {
   return x*x;
}

Color::Color(int r, int g, int b) {
   red = r; 
   green = g; 
   blue = b;
}

double Color::dist_to(Color other_color) {
   return sqrt( sqr(red - other_color.red)
      + sqr(green - other_color.green)
      + sqr(blue - other_color.blue));
}
]\

void Color::swap_with(Color* other_color) {
   int tmp = red;   
   red = (*other_color).red;
\[
   (*other_color).red = tmp;
]\

   tmp = green;
   green = other_color->green;
\[
   other_color->green = tmp;
]\

   // swap blues any way you like
\[
   tmp = blue;
   blue = other_color->blue;
   (*other_color).blue = tmp;
]\
}

int main() {
   Color black(0, 0, 0);
   Color my_shoe_color(3, 4, 0);
   Color my_sock_color(0, 0, 100);
   
   my_shoe_color.swap_with(&my_sock_color);
   cout << black.dist_to(my_shoe_color) << endl;
   cout << black.dist_to(my_sock_color) << endl;
}
"""

description = """Write a member function that swaps the contents of two <tt>Color</tt> objects.
This means that after running <tt>colA.swap(&colB)</tt>, the reds of the two colors are swapped,
as are the greens, and blues.
"""

lang = "C++"

tests = [["", []]]
