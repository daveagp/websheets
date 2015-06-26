attempts_until_ref = 0


source_code = r"""
#include <vector>
#include <iostream>
using namespace std;

\[
vector<int> parity_counts(vector<int> nums) {
   int evens = 0;
   int odds = 0;
   for (int i=0; i<nums.size(); i++) {
      if (nums[i]%2==0)
         evens++;
      else
         odds++;
   }
   vector<int> result;
   result.push_back(evens);
   result.push_back(odds);
   return result;
}
]\

// print out contents of vector, with a space after each one
\hide[
void print_vec(vector<int> V) {
   for (int i=0; i<V.size(); i++) 
      cout << V[i] << " ";
   cout << endl;
}
]\
\fake[
void print_vec(vector<int> V); // see concat exercise
]\

int main() {
   // primes is 2 3 5
   vector<int> primes;
   primes.push_back(2); primes.push_back(3); primes.push_back(5);
   print_vec(parity_counts(primes));

   // squares is 0 1 4 9 16
   vector<int> squares;
   squares.resize(5);
   for (int i=0; i<5; i++) squares[i] = i*i;
   print_vec(parity_counts(squares));

   vector<int> empty_vector;
   print_vec(parity_counts(empty_vector));
}
"""

lang = "C++"

tests = [["", []]]

description = """Define a function <tt>parity_counts</tt> that takes
one <tt>vector&lt;int&gt;</tt> objects as input.
It should return a vector containing two ints: the first counting
how many inputs were even, the second counting how many were odd.
"""
