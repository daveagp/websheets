attempts_until_ref = 0

source_code = r"""
#include <vector>
#include <iostream>
using namespace std;

template <typename T>
T vecsum(T init, vector<T> v) {
   \[T]\ result = init;

   // add all entries of v into result
\[
   for (int i=0; i<v.size(); i++)
      result += v[i];
]\
   return result;
}

int main() {
   // primes is 2 3 5
   vector<int> primes;
   primes.push_back(2); primes.push_back(3); primes.push_back(5);
   cout << vecsum(0, primes) << endl;
   // should give 0 + 2 + 3 + 5 which is 10

   vector<string> words;
   words.push_back("Ice"); words.push_back("Cream");
   cout << vecsum(string(""), words) << endl; 
   // should give "" + "Ice" + "Cream" which is "IceCream"
}
"""

lang = "C++"

tests = [["", []]]

description = """Define a function <tt>vecsum</tt> 
to "add" all of the entries in a vector.
The function will also need to give the initializing value 
<tt>init</tt> for
the sum (for example, if adding numbers, you want to start the sum at
zero).
"""
