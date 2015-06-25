source_code = r"""
#include <iostream>
#include <cmath>
using namespace std;

\[ bool ]\ isPrime( \[ int n ]\ )
{
\[
   for(int i=2; i < sqrt(n); i++){
      if (n%i == 0) // does i divide n? 
        return false;
   }
   return true;
]\
}
int main() {
   int n;
   cin >> n;
   
   if ( isPrime(n) ) {
     cout << n << " is prime!" << endl;
   }
   else {
     cout << n << " is NOT prime!" << endl;
   }
   return 0;
}
"""

lang = "C++"
attempts_until_ref = 0

description = r"""
Write a program that takes an integer input <tt>n</tt>, and prints 
whether that number is prime or not.<p>
A number is prime if it has no divisors other than itself and one. 
The first few primes are 2, 3, 5, 7, 11, &hellip;
"""

tests = [
    ["100", []],
    ["17", []],
    ["3", []],
    ["4", []],
    ["37", []],
    ["39", []],
] # stdin, args
