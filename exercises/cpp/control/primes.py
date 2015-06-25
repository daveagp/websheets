source_code = r"""
#include <iostream>
using namespace std;

int main() {
\[
   int n;
   cin >> n;
   
   for (int i=2; i<=n; i++) {
      bool i_is_prime = true;

      for (int j=2; j<i; j++)
         if (i%j == 0) // does j divide i? 
            i_is_prime = false;

      if (i_is_prime)
         cout << i << endl;
   }
]\
   return 0;
}
"""

lang = "C++"
attempts_until_ref = 0

description = r"""
Write a program that takes an integer input <tt>n</tt>, and prints 
out all of the prime numbers less than or equal to <tt>n</tt>. 
<p>
A number is prime if it has no divisors other than itself and one. 
The first few primes are 2, 3, 5, 7, 11, &hellip;
"""

tests = [
    ["100", []],
    ["17", []],
] # stdin, args
