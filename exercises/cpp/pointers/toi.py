source_code = r"""
#include <iostream>

int ctoi(char ch) {
   int ch_as_int = (int)ch;
\[
   int zero_as_int = '0';
   return ch_as_int - zero_as_int;
]\
}

int atoi(char* str) {
\[
   int value = 0;
   int i = 0;
]\
   while (\[str[i] != '\0']\) { // iterate through C string
      // multiply by 10 and add next ctoi each time
\[
      value *= 10;
      value += ctoi(str[i]);
      i++;
]\      
   }
\[
   return value;
]\
}
"""

lang = "C++func"


description = r"""
Write a function <tt>ctoi</tt> that converts a character to an integer,
e.g. <tt>ctoi('7')</tt> gives the integer 7. Then write <tt>atoi</tt>,
that converts a C string to an integer.
<p>
You don't need to worry about negative numbers, overflow,
or input validation for this exercise.
"""

tests = [
    ["check-function", "ctoi", "int", ["char"]],
    ["call-function", "ctoi", ["'7'"]],
    ["call-function", "ctoi", ["'0'"]],
    ["call-function", "ctoi", ["'1'"]],
    ["check-function", "atoi", "int", ["char*"]],
    ["call-function", "atoi", ['"48"']],
    ["call-function", "atoi", ['"103"']],
    ["call-function", "atoi", ['"2014"']],
    ["call-function", "atoi", ['"2"']],
]


attempts_until_ref = 0
