attempts_until_ref = 0

source_code = r"""
#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
using namespace std;

string date(string month, int day, int year) {
// return date in format like: October 6, 1880
\[
   ostringstream buf;
   buf << month << " " << day << ", " << year;
   return buf.str();
]\
}

int main() {
   string date1 = date("December", 30, 1950);
   cout << boolalpha;
   cout << "date1 OK? " << ("December 30, 1950" == date1) << endl;
   
   cout << date("July", 4, 1776) << endl;
   cout << date("October", 6, 1880) << endl;
}
"""

lang = "C++"

description = r"""
Define a function <tt>date(string month, int day, int year)</tt>
that returns a <tt>string</tt> combining the elements in this format:
<pre>October 6, 1880</pre>
"""

tests = [
["", []]
]


