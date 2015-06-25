source_code = r"""
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
   double approx;

   // write code that includes a for loop to compute the first 10
   // terms of Wallis' approximation to PI/2 which is:
   //  (2/1)*(2/3)*(4/3)*(4/5)*(6/5)*(6/7)*(8/7)*(8/9)*(10/9)*(10/11)
\[      
   approx = 1.0;
   for(int i=2; i <= 10; i+=2){
     approx = approx * ( static_cast<double>(i) / (i-1) );
     approx = approx * ( static_cast<double>(i) / (i+1) );
   }

]\

   cout << "The approximate value is ";
   cout << fixed << setprecision(3) << approx  << endl;
   return 0;
}
"""

lang = "C++"
attempts_until_ref = 0

description = r"""
This program should use a loop to compute the result of the first 10
terms of Wallis' approximation of PI/2.  See the comment in the code
for the exact terms.
"""

tests = [["", []],]
                    # stdin, args
