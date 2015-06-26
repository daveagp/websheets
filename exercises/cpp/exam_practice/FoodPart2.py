lang = "C++"

attempts_until_ref = 0

description = r"""
Please see <a href="http://bits.usc.edu/cs103/programming-exam/">the programming exam page</a>.
<br>
We recommend doing this practice in a timed environment; give yourself 90 minutes.
"""

source_code = r"""
// NOTE: The actual exam will not use Websheets (instead, the PA submit system).
// It's recommended to practice and test on your own machine and copy here to check.
\[
/******************************************************************* 
 Reference solution for Foodlympics Part Two: Gourmet Glory

 Description:  Reads in names and scores for C countries. Prints out the N
               top-score countries in order.    
**************************************************************************/

#include <iostream>
#include <cstdlib>
using namespace std;

// find the highest value in scores. set this value to 0, and 
// return the corresponding element of countries.
// C is the number of countries
string best(string countries[], int C, int scores[]) {

   // max is the maximum score seen so far
   int max = scores[0];

   // bestIndex is the index of the (earliest) max-score country
   int bestIndex = 0; 
        
   // find index of max-score country
   for (int i = 0; i < C; i++) {
      if (scores[i] > max) {
         max = scores[i];
         bestIndex = i;
      }
   }
        
   // do required update and return the winner
   scores[bestIndex] = 0;
   return countries[bestIndex];
}

// read in a file of scores, and take N from the command-line.
// then print out the top N ranking countries from best to worst.
int main(int argc, char* argv[]) {

   int C; // number of countries
   cin >> C;

   int N = atoi(argv[1]); // how many to rank

   string countries[100];
   int scores[100];

   // read the rest of the input
   for (int i = 0; i < C; i++) {
      cin >> countries[i];
      cin >> scores[i];
   }
        
   // now print the results
   for (int i = 0; i < N; i++) {
      string nextRanked = best(countries, C, scores);
      cout << "Rank " << i+1 << ": " << nextRanked << endl;
   }
}
]\
"""

tests = [
["""3
Canada 13
Mexico 14
USA 14""", ["3"]],
["""6
GER 13
BEL 15
AUT 17
CHF 19
LUX 14
LIE 8""", ["2"]],
["1\nPangaea 10", ["1"]],
["2\nA 5\nB 5", ["2"]],
["2\nA 5\nB 8", ["2"]],
["2\nA 8\nB 5", ["2"]],
["3\nA 8\nB 8\nC 1", ["3"]],
["4\nA 8\nB 5\nC 8\nD 5", ["1"]],
["4\nA 8\nB 5\nC 8\nD 5", ["4"]],
["7\nA 8\nB 6\nC 7\nD 5\nE 3\nF 10\nG 9", ["3"]],
["7\nA 8\nB 6\nC 7\nD 5\nE 3\nF 10\nG 9", ["7"]],
["9\nA 3\nB 14\nC 15\nD 9\nE 2\nF 6\nG 5\nH 3\nI 5", ["1"]],
["9\nA 3\nB 14\nC 15\nD 9\nE 2\nF 6\nG 5\nH 3\nI 5", ["3"]],
["9\nA 3\nB 14\nC 15\nD 9\nE 2\nF 6\nG 5\nH 3\nI 5", ["9"]]]
