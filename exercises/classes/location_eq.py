source_code = r"""
#include <iostream>
#include <iomanip>
using namespace std;

struct Location { // define a new data type, Location
   int row;       // each Location has a row
   int col;       // each Location has a col
};

int main() {
   cout << boolalpha;
   Location home; // construct a Location
   home.row = 5; home.col = 10;

   Location north_of_home = home; // copy it
   north_of_home.row -= 1;

   Location home_again = north_of_home; // copy it
   home_again.row += 1;

   // compare them
\[
   // if you did this a lot, you might want to make a function!
   cout << (home.row == north_of_home.row &&
            north_of_home.row == north_of_home.col) << endl;
   cout << (home.row == home_again.row &&
            home.col == home_again.col) << endl;
\show:
   cout << (home == north_of_home) << endl;
   cout << (home == home_again) << endl;
]\
}

"""

lang = "C++"

description = r"""
Comparing <tt>struct</tt>s.
"""

tests = [
    ["", []],
] # stdin, args

attempts_until_ref = 0
