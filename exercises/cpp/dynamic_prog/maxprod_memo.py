attempts_until_ref = 0

description = r"""
Define a memoized recursive function to compute <i>maxprod(N)</i>.
"""

lang = "C++"

source_code = r"""
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

double maxprod(int n, vector<double>& memory) {
   // check if answer was already computed
   if (\[memory[n] != 0]\)
      return \[memory[n]]\;

   // else save answer 
   if (\[n <= 3]\)
      memory[n] = \[n]\;
   else
      memory[n] = \[max(2*maxprod(n-2, memory), 3*maxprod(n-3, memory))]\;

   return memory[n];
}

int main(int argc, char* argv[]) {
   int N = atoi(argv[1]);
   vector<double> memory(N+1, \[0]\); // sets initial value for vector
   cout << setprecision(20) << maxprod(N, memory) << endl;
}
"""

tests = [
    ["", ["6"]],
    ["", ["7"]],
    ["", ["8"]],
    ["", ["20"]],
    ["", ["60"]],
    ["", ["100"]],
    ["", ["101"]],
    ["", ["102"]],
    ["", ["500"]],
    ["", ["1812"]],
]

