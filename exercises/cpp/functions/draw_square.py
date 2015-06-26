source_code = r"""
#include <iostream>
using namespace std;

// prints an ASCII square to stdout (monitor) 
// of side length, s, using character, c
//  e.g. calling drawSquare(4, '*') should yield
//  ****
//  *  *
//  *  *
//  ****

 \[ void ]\ drawSquare (\[ int s, char c ]\) {
\[
  for(int i=0; i < s; i++){
    for(int j=0; j < s; j++){
      if(i==0 || i == s-1 || j==0 || j==s-1){
        cout << c;
      }
      else {
        cout << " ";
      }
    }
    cout << endl;
  }

]\
}
"""

lang = "C++"

attempts_until_ref = 0

mode = "func"

description = r"""
Define a function <tt>drawSquare</tt> that takes an integer and char parameter
and prints a square:
the integer indicates the side length of the square to draw, and
the character indicates what character to use to draw the square.
See the example below.
"""

tests = [
    ["check-function", "drawSquare", "void", ["int","char"]],
    ["call-function", "drawSquare", ["3","'*'"]],
    ["call-function", "drawSquare", ["10","'+'"]],
    ["call-function", "drawSquare", ["30","'-'"]],
]


