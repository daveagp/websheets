
source_code = r"""
#include <cmath>
#include <iostream>
using namespace std;

class Color {
public:
   // data members
   int red;
   int green;
   int blue;
};

double sqr(double x) {
   return x*x;
}

double dist(Color c1, Color c2) {
   return sqrt( sqr(\[c1.red - c2.red]\)
      + sqr(\[c1.green - c2.green]\)
      + sqr(\[c1.blue - c2.blue]\));
}
      
int main() {
   // declare a color
   Color magenta;
   // access its member variables
   magenta.red = 255;
   magenta.green = 0;
   magenta.blue = 255;
   
   Color cyan;
   cyan.red = 0;
   cyan.green = 255;
   cyan.blue = 255;

   Color azure;
   azure.red = 0;
   azure.green = 127;
   azure.blue = 255;

   // pass Colors into the function
   cout << dist(magenta, cyan) << endl;
   cout << dist(magenta, azure) << endl;
   cout << dist(cyan, azure) << endl;
   return 0;
}
"""

description = r"""The following <tt>Color</tt> class represents a 
single color. Write a function <tt>dist</tt> to compute the distance between 
two colors, defined by
$$\lVert c1, c2 \rVert = \sqrt{
(c1_{\textrm {red}} - c2_{\textrm {red}})^2+
(c1_{\textrm {green}} - c2_{\textrm {green}})^2+
(c1_{\textrm {blue}} - c2_{\textrm {blue}})^2}$$"""

lang = "C++"

tests = [["", []]]
