#based on this Creative Commons Att-SA 3.0 exercise:
#https://cloudcoder.org/repo/exercise/b9c7c88bd10dc887d8221a3e3554d053f6d3a30b

source_code = r"""
#include <iostream>
#include <cstdlib>
using namespace std; 
\[
int main(int argc, char* argv[]) {
   int N = atoi(argv[1]);

   if (N % 15 == 0) { 
      cout << "FizzBuzz" << endl;
   }
   else if (N % 5 == 0) {
      cout << "Buzz" << endl;
   }
   else if (N % 3 == 0) {
      cout << "Fizz" << endl;
   }
   else {
      cout << N << endl;
   }

   return 0; 
}
]\
"""

lang = "C++"

attempts_until_ref = 0

description = r"""
<p>Write a program <code>fizzbuzz</code> that takes an integer command-line 
argument <code>n</code> and prints an output. 
Depending on the value of <code>n</code>, print a different output
based on the following conditions:</p>
<ul>
<li>If the value is a multiple of 3: print the string <code>Fizz</code> instead</li>
<li>If the value is a multiple of 5: print the string <code>Buzz</code> instead</li>
<li>If the value is a multiple of 3 &amp; 5: print the string <code>FizzBuzz</code> instead</li>
</ul>
For instance,
<ul>
<li><code>fizzbuzz 3</code>  should print <code>Fizz</code></li>
<li><code>fizzbuzz 5</code>  should print <code>Buzz</code></li>
<li><code>fizzbuzz 17</code> should print <code>17</code></li>
<li><code>fuzzbuzz 30</code> should print <code>FizzBuzz</code></li>
"""

tests = [["", ["1"]],
         ["", ["3"]],
         ["", ["5"]],
         ["", ["6"]],
         ["", ["7"]],
        ["", ["12"]],
        ["", ["15"]],
        ["", ["20"]],
          ["", ["60"]],
         ["", ["61"]],
         ["", ["119"]],
         ["", ["120"]]]
