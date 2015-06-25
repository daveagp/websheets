source_code = r"""
#include <iostream>
#include <string>
using namespace std;

class Item {
public:
  Item(int w, string y) { _w = w; _y = y; }
  int _w; 
  string _y;
};

\[
// Function to build an item
\show:
Item  buildItem()
{
  Item x(4, "hi");
  return x;

}
]\

int main() 
{
\[
   // Code to call buildItem and receive return value
\show:
   Item i = buildItem();
   cout << i._w << " " << i._y << endl;

]\
   return 0;
}
"""

lang = "C++"
example = True 

description = r"""
Use this program to test various methods of returning an object or 
pointer/reference to an object from a function.
"""

tests = [["", []]] # stdin, args
