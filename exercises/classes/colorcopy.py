
source_code = r"""
#include <cmath>
#include <iostream>
using namespace std;

\hide[
class color {
   public:
      int red;
      int green;
      int blue;
};

]\
int main() {
   color my_fav_color;
   my_fav_color.red = 1;
   my_fav_color.blue = 0;
   my_fav_color.green = 3;
   
   color your_fav_color = my_fav_color;
   your_fav_color.green = 4;

   cout << my_fav_color.green << endl; // 3 or 4?
}
"""

description = "Example of <tt>=</tt> with objects."

example = True

lang = "C++"

tests = [["", []]]
