source_code = r"""
#include <iostream>
using namespace std;

/* prints out the number of seconds in a week */

int main() {
\[
   int seconds_per_minute = 60;
   int seconds_per_hour = seconds_per_minute * 60; // that's better!
   int seconds_per_day = seconds_per_hour * 24;

   int days_per_week = 5;
   days_per_week = days_per_week + 2; // weekends enabled

   cout << seconds_per_day * days_per_week;

   return 0;
\show:
   int seconds_per_minute = 60;
   int seconds_per_hour = seconds_per_minute * 50; // TODO: check this!
   int seconds_per_day = seconds_per_hour * 24;

   int days_per_week = 5;
   // days_per_week = days_per_week + 2; // weekends are disabled!?

   cout << seconds_per_day * days_per_week;

   return 0;
]\
}
"""

lang = "C++"

description = r"""
Debug this program so that it prints out the number of seconds in a week.
"""

tests = [
    ["", []],
] # stdin, args
