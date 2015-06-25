source_code = r"""
#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
   double approx;

   // write code that includes a for loop to compute the first 10
   // terms of Liebniz's approximation to PI/4 which is:
   //  (1/1) - (1/3) + (1/5) - (1/7) + ... - (1/19)
\[      
   approx = 0.0;
   for(int i=0; i < 10; i++){
     approx += pow(-1,i)/(2*i+1);
   }

]\

   cout << "The approximate value is ";
   cout << fixed << setprecision(3) << approx  << endl;
   return 0;
}
"""

lang = "C++"

description = r"""
This program should use a loop to compute the result of the first 10
terms of Leibniz's approximation of $\pi/4$.  See the comment in the code
for the exact terms.
"""

tests = [["", []],]
                    # stdin, args

attempts_until_ref = 0
