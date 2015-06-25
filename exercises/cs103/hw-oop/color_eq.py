
source_code = r"""
#include <cmath>
#include <iostream>
#include <iomanip>
using namespace std;

class Color {
public:
   // constructor
   Color(int r, int g, int b);
   // member function
\[
   bool same_as(Color other_color);
]\
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

\[bool]\ \[Color::]\same_as(\[Color other_color]\) { 
\[
   return red == other_color.red && blue == other_color.blue 
         && green == other_color.green;
]\
}      

int main() {
   Color my_wall(255, 127, 0);
   Color my_shoes(255, 255, 0);
   Color my_snack(255, 127, 0); // orange
   Color my_hat(0, 127, 0);
   Color my_balloon(255, 127, 255);

   cout << boolalpha;
   cout << my_wall.same_as(my_shoes) << endl;
   cout << my_wall.same_as(my_snack) << endl; // TRUE! others are false
   cout << my_wall.same_as(my_hat) << endl;
   cout << my_wall.same_as(my_balloon) << endl;
   return 0;
}
"""

description = r"""
We saw in class that <tt>==</tt> doesn't work with objects (at least, not by default).
Declare and define a method <tt>same_as</tt> which tells us whether two colors are the same.
For example, you should be able to call it as <tt>col1.same_as(col2)</tt> and get back a <tt>true</tt> or <tt>false</tt> answer
depending on whether the reds, greens, and blues are pairwise identical.
"""

lang = "C++"

tests = [["", []]]
