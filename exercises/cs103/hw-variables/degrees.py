source_code = r"""
#include <iostream>
using namespace std;

int main() {
   double F;
   cin >> F; // read input, degrees Fahrenheit

   double C = \[5 * (F - 32) / 9\show:5 * F - 32 / 9]\;
   cout << C; // print the output, degrees Celsius

   return 0;
}
"""

lang = "C++"

description = r"""
This program is supposed to read a temperature in degrees Fahrenheit,
and output the corresponding temperature in degrees Celsius, using the formula
$$C = 5 \times \frac{F-32}{9}.$$
For example, when the input $F$ is 41, the output $C$ should be 5.
There's something missing, which is causing the program to give an incorrect 
answer. Debug it.
"""

tests = [
    ["41", []],
    ["50", []],
    ["77", []],
    ["-10", []],
    ["100", []],
    ["-32", []],
    ["-40", []],
] # stdin, args
