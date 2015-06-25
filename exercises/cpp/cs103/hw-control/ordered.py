source_code = r"""
#include <iostream>
using namespace std;

int main() {
   int x, y, z;
   cin >> x >> y >> z;

   bool isDecreasing = (x > y) && \[(y > z)]\;
   bool isIncreasing = \[(x < y) && (y < z)]\;

   bool isOrdered = isIncreasing \[||]\ isDecreasing;

   // print out result, true or false   
   cout << boolalpha << isOrdered;
   return 0;
}
"""

lang = "C++"

description = r"""
This program takes three integers as input. Write a program that prints <tt>true</tt>
if they are ordered (either in strictly increasing or strictly decreasing 
order), and
<tt>false</tt> otherwise. For example, <tt>1 2 3</tt> are ordered, but
<tt>6 8 2</tt> are not ordered.
"""

tests = [
    ["1 2 3", []],
    ["6 8 2", []],
    ["10 9 2", []],
    ["6 9 9", []],
    ["10 2 8", []],
    ["9 0 9", []],
    ["888 88 8", []],
    ["2 2 1", []],
    ["4 3 5", []],
] # stdin, args
