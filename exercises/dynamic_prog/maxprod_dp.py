attempts_until_ref = 0

description = r"""
Define a dynamic programming function to compute <i>maxprod(N)</i>.
"""

lang = "C++"

source_code = r"""
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

double maxprod(int n) {
   vector<double> memory(n+1); // indices from 0 to n 
\[
   for (int i=1; i<=3; i++)
      memory[i] = i;
   for (int i=4; i<=n; i++)
      memory[i] = max(memory[i-2]*2, memory[i-3]*3);
   return memory[n];
]\
}

int main(int argc, char* argv[]) {
   int N = atoi(argv[1]);
   cout << setprecision(20) << maxprod(N) << endl;
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

