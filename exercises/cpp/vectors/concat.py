attempts_until_ref = 0

source_code = r"""
#include <vector>
#include <iostream>
using namespace std;

// print out contents of vector, with a space after each one
void print_vec(vector<int> V) {
   for (int i=0; i<\[V.size()]\; i++) 
      cout << V[i] << " ";
   cout << endl;
}

\[
vector<int> concat(vector<int> A, vector<int> B) {
   vector<int> result;
   for (int i=0; i<A.size(); i++)
      result.push_back(A[i]);
   for (int i=0; i<B.size(); i++)
      result.push_back(B[i]);
   return result;
}
]\

int main() {
   // primes is 2 3 5
   vector<int> primes;
   primes.push_back(2); primes.push_back(3); primes.push_back(5);

   // squares is 0 1 4 9 16
   vector<int> squares;
   squares.resize(5);
   for (int i=0; i<5; i++) squares[i] = i*i;

   print_vec(concat(primes, squares)); // 2 3 5 0 1 4 9 16
   print_vec(concat(squares, primes)); // 0 1 4 9 16 2 3 5
   vector<int> primes_twice = concat(primes, primes);
   print_vec(concat(primes_twice, primes_twice)); // primes 4 times
}
"""

lang = "C++"

tests = [["", []]]

description = """Define a function <tt>concat</tt> that takes
two <tt>vector&lt;int&gt;</tt> objects; it should 
return the concatenation of them
into a single vector. See <tt>main</tt> for an example.
"""
