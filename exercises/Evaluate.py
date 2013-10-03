source_code = r"""
public static int evaluate(String expression) {
   // here -1 means 'not found yet'
   int plusPos = -1; // position of last '+' outside of parentheses
   int timesPos = -1; // position of last '*' outside of parentheses

   // scan expression, looking for operators outside of parentheses
   int level = 0; // current nesting depth
   for (int i=0; i<expression.length(); i++) {
      char ch = expression.charAt(i);

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
      String exprLeft = expression.substring(0, plusPos);
      String exprRight = expression.substring(plusPos+1);
      int valueLeft = evaluate(exprLeft);
      int valueRight = evaluate(exprRight);
      return valueLeft + valueRight;
   }
   else if (timesPos != -1) {
      // break down, e.g. "(3+4)*(5+6)" => "(3+4)" and "(5+6)"
      String exprLeft = expression.substring(0, timesPos);
      String exprRight = expression.substring(timesPos+1);
\[
      int valueLeft = evaluate(exprLeft);
      int valueRight = evaluate(exprRight);
      return valueLeft * valueRight;
]\
   }
   else if (expression.charAt(0)=='(') {
      // everything was in a matched pair of parentheses
      // break down, e.g. "(3*4)" => "3*4"
      return evaluate(expression.substring(1, expression.length()-1));
   }
   else {
      // base case: just a number. convert expression to int.
      // don't make any recursive calls
      return \[Integer.parseInt(expression)]\;
   }
}

public static void main(String[] args) {
   String test = "1*2+3*(4+5)";
   StdOut.println(test + " evaluates to " + evaluate(test));
}
"""

description = r"""
Write a static method <code>evaluate()</code> that evaluates
a mathematical expression (a String) consisting of
integers, +, *, and parentheses.
By definition, it must use
 recursion to evaluate two halves of the expression and
combine them. The string manipulation and logic are filled in, but
you need to add two recursive calls and a base case.
"""

tests = r"""
testMain();
test("evaluate", "2*2+3*3");
test("evaluate", "(3+4)*(5+6)");
test("evaluate", "126");
test("evaluate", "(2*(1+6*2+2)+6*6+2*2*(1+2+6))+6*2*2");
"""
