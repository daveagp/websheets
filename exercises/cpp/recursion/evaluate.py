description = r"""
Define a function <code>evaluate()</code> that evaluates
a mathematical expression (a string) consisting of
integers, +, *, and parentheses.
<p>
For example,
<ul>
<li><tt>evaluate("11+23");</tt> returns 34
<li><tt>evaluate("(1+1)*5");</tt> returns 10
</ul>
By definition, it must use
 recursion to evaluate two halves of the expression and
combine them. The string manipulation and logic are filled in, but
you need to add two recursive calls and a base case.
"""


source_code = r"""
#include <iostream>
#include <cstdlib>
// cstdlib is for atoi
using namespace std;

int evaluate(string expression) {
   // here -1 means 'not found yet'
   int plusPos = -1; // position of last '+' outside of parentheses
   int timesPos = -1; // position of last '*' outside of parentheses

   // scan expression, looking for operators outside of parentheses
   int level = 0; // current nesting depth
   for (int i=0; i<expression.length(); i++) {
      char ch = expression[i];

      // look for operator
      if (ch=='+' && level==0) plusPos = i;
      if (ch=='*' && level==0) timesPos = i;
  
      // count level of parentheses
      if (ch=='(') level++;
      if (ch==')') level--;
   }
   
   // recurse on lowest-precedence operator

   if (plusPos != -1) {
      // break down, e.g. "3*4+5*6" => "3*4" and "5*6"
      string exprLeft = expression.substr(0, plusPos);
      string exprRight = expression.substr(plusPos+1);
      int valueLeft = evaluate(exprLeft);
      int valueRight = evaluate(exprRight);
      return valueLeft + valueRight;
   }
   else if (timesPos != -1) {
      // break down, e.g. "(3+4)*(5+6)" => "(3+4)" and "(5+6)"
      string exprLeft = expression.substr(0, timesPos);
      string exprRight = expression.substr(timesPos+1);
\[
      int valueLeft = evaluate(exprLeft);
      int valueRight = evaluate(exprRight);
      return valueLeft * valueRight;
]\
   }
   else if (expression[0]=='(') {
      // everything was in a matched pair of parentheses
      // break down, e.g. "(3*4)" => "3*4"
      return evaluate(expression.substr(1, expression.length()-1));
   }
   else {
      // base case: just a number like "12". convert expression to int.
      // don't make any recursive calls
      // 1. convert C++ string to C string
      const char* num_cstr = expression.c_str();
      // 2. convert C string to integer and return it
      return \[atoi]\(num_cstr);
   }
}

int main() {
   string expr;
   cin >> expr;
   cout << evaluate(expr);
}
"""

lang = "C++"

tests = [
    ["11+19", []],
    ["(1+1)*5", []],
    ["2*2+3*3", []],
    ["(2*(1+6*2+2)+6*6+2*2*(1+2+6))+6*2*2", []],
    ["103+456*789", []],
]

attempts_until_ref = 0
