source_code = r"""
#include <iostream>
#include <iomanip>
using namespace std;

struct Location { // define a new data type, Location
   int row;       // each Location has a row
   int col;       // each Location has a col
};

\[
void reset_location(Location* loc) {
   loc->row = 0;
   loc->col = 0;
}
\show:
void reset_location(Location loc) {
   loc.row = 0;
   loc.col = 0;
}
]\

void print_location(Location loc);

int main() {
   Location home; // construct a Location
   home.row = 5;
   home.col = 10;

\[
   reset_location(&home);
\show:
   reset_location(home);
]\
   print_location(home);
}

void print_location(Location loc) {
   cout << "row " << loc.row << ", column " << loc.col << endl;
}
"""

lang = "C++"

description = r"""
An example of <tt>struct</tt> with pass-by-value.
"""

tests = [
    ["", []],
] # stdin, args

attempts_until_ref = 0
