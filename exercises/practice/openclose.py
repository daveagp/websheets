#based on this Creative Commons Att-SA 3.0 exercise:
#https://cloudcoder.org/repo/exercise/6cdc568f0b5fac4c019de701dd849f4396d7670b

source_code = r"""
#include <iostream>
#include <cstdlib>
using namespace std; 

bool bracket_check(string expr) {
\[
   // we'll scan through the string in a single pass
   // the strategy will be to remember how "deep" we're nested
   int depth = 0;
   // and what kinds of brackets contain us, memory[0] being the outermost
   char memory[100];

   for (int i=0; i<expr.length(); i++) {
      if (expr[i] == '(' || expr[i] == '{' || expr[i] == '[') {
         // remember entering this
         depth++;
         memory[depth-1] = expr[i];
      }
      else if (expr[i] == ')' || expr[i] == '}' || expr[i] == ']') {
         // closer not matching any previous opener
         if (depth == 0)
            return false;
 
         // see if closer and opener have same style
         char should_match = memory[depth-1];
         depth--;
         if (expr[i] == ')' && should_match != '(')
            return false;
         if (expr[i] == ']' && should_match != '[')
            return false;
         if (expr[i] == '}' && should_match != '{')
            return false;
      }
   }
   
   // done scanning the string. we'd better be at level 0...
   return (depth == 0);
]\
}
"""

lang = "C++"

mode = "func"

attempts_until_ref = 0

description = r"""
You're working with an intern that keeps coming to you with 
C++ code that won't run because the <tt>{</tt>braces<tt>}</tt>, 
<tt>(</tt>brackets<tt>)</tt>, and <tt>(</tt>parentheses<tt>)</tt> 
are off. To save you both some time, you decide 
to write a braces/brackets/parentheses validator.

<p>
Write a function <tt>bracket_check</tt> that takes a <tt>string</tt>
and returns <tt>true</tt> if the braces/brackets/parentheses are matched,
and <tt>false</tt> otherwise. You can assume all other characters have
been deleted: the string can only contain some mix of <tt>()[]{}</tt>
characters (possibly multiple times).

<p>E.g.: <tt>"{[]()}"</tt> and <tt>"[(())]"</tt> should return <tt>true</tt>,
and <tt>")("</tt> and <tt>"(]"</tt> should return <tt>false</tt>.

<p>You may assume that the string has length at most 100.
"""

tests = [
    ["check-function", "bracket_check", "bool", ["string"]],
    ["call-function", "bracket_check", ['"()()"']],
    ["call-function", "bracket_check", ['"(())"']],
    ["call-function", "bracket_check", ['"())("']],
    ["call-function", "bracket_check", ['"((())"']],
    ["call-function", "bracket_check", ['"([])"']],
    ["call-function", "bracket_check", ['"{}[]"']],
    ["call-function", "bracket_check", ['"{[}]"']],
    ["call-function", "bracket_check", ['"([]{})"']],
    ["call-function", "bracket_check", ['"([()][([[]][]){()}])"']],
    ["call-function", "bracket_check", ['"([()][([[]][]}{()}])"']],
    ["call-function", "bracket_check", ['"([(]][([[]][]){()}])"']],
    ["call-function", "bracket_check", ['"([()][([[]][]){())])"']],
    ["call-function", "bracket_check", ['"([()][([[]][]){()]])"']],
    ["call-function", "bracket_check", ['"([()][([[)][]){()}])"']],
    ["call-function", "bracket_check", ['"([()][([[]}[]){()}])"']],
    ["call-function", "bracket_check", ['"([()][([[]][]){()}]))"']],
    ["call-function", "bracket_check", ['"([()][([[]][]){()}]"']],
]


