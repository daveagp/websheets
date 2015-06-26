source_code = r"""
#include <iostream>
#include <iomanip>
using namespace std;

struct Location { // define a new data type, Location
   int row;       // each Location has a row
   int col;       // each Location has a col
};

void print_location(Location loc); // TODO

int main() {
\[

\show:
   Location home; // construct a Location
   home.row = 5;
   home.col = 10;

   Location north_of_home = home; // copy it
   north_of_home.row -= 1;

   print_location(home);
   print_location(north_of_home);
]\
}

void print_location(Location loc) {
   cout << "row " << loc.row << ", column " << loc.col << endl;
}
"""

lang = "C++"

description = r"""
An example of <tt>struct</tt>.
"""

tests = [
    ["", []],
] # stdin, args

example = True
