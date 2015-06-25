attempts_until_ref = 0

source_code = r"""
#include <vector>
#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
   vector<int> memory;
   string input;
   // read each input
   while (cin >> input) {
      // if you read an operator, combine the last two elements of the stack
      if (input == "+" || input == "*") {
\[
         int v1 = memory.back();
         memory.pop_back();
         int v2 = memory.back();
         memory.pop_back();
]\
         if (input == "+")
            \[memory.push_back(v1+v2);]\
         else
            \[memory.push_back(v1*v2);]\
      }
      // if you read a number, place it at the end of the stack
      else {
         memory.push_back(atoi(input.c_str()));
      }
   }
   cout << memory.back();
}
"""

lang = "C++"

tests = [
["1 2 +", []],
["5 2 *", []],
["4 3 * 2 1 * +", []],
["4 3 2 + * 1 *", []],
["5 4 3 2 1 * * * *", []],
["5 4 3 2 1 + + + +", []],
["1 2 + 3 4 * 5 6 + 7 8 + 9 * + + *", []],
]

description = """
<i>Postfix notation</i> transforms mathematical expressions by putting 
each operator <i>after</i> its arguments. So <tt>1 + 2</tt> becomes 
<tt>1 2 +</tt> and <tt>5 * 2</tt> becomes <tt>5 2 *</tt>. 
<p>An advantage
over normal (infix) expressions is that parentheses are not needed.
For example <tt>4 3 * 2 1 * +</tt> is the prefix version of <tt>4*3+2*1</tt>
while <tt>4 3 2 + * 1 *</tt> is the prefix version of <tt>4*(3+2)*1</tt>.
<p>Write an evaluator for prefix notation (just the <tt>*</tt> and <tt>+</tt>
operators) by using a vector as a stack.
Each time you read a number, place it at the end of the stack. Each time
you read an operator, combine the last two elements of the stack.
"""
