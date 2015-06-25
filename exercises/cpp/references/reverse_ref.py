attempts_until_ref = 0

source_code = r"""
#include <iostream>
#include <vector>
using namespace std;

// assume this is defined for you
void swap(int& a, int& b)\fake[;]\ 
\hide[
{
   int tmp = a;
   a = b;
   b = tmp;
}
]\
// for testing: print contents of vector
void print_vec(vector<int> V)\fake[;]\ 
\hide[
{
   for (int i=0; i<V.size(); i++)
      cout << V[i] << " ";
   cout << endl;
}
]\

// complete this function to reverse a vector
void reverse(\[vector<int>& v]\) {
\[
   for (int i=0; i<v.size()/2; i++)
      swap(v[i], v[v.size()-i-1]);
]\
}

int main() {
   vector<int> test;
   int x;
   while (cin >> x) test.push_back(x);
   cout << "Before reverse: "; print_vec(test);
   reverse(test);
   cout << "After reverse: "; print_vec(test);
}
"""

lang = "C++"

description = r"""
Write a function that reverses a vector that is passed in by reference.
E.g., if <tt>vec</tt> contains 2, 0, 1, 5 in that order, after calling
<tt>reverse(vec)</tt>, it should contain 5, 1, 0, 2 in that order. 
<br>
Call the <tt>swap</tt> function defined previously to help you.
"""

tests = [
    ["1 0 3", []],
    ["4 8 15 16 23 42", []],
    ["9 6 7 1 1 1 1", []],
]

