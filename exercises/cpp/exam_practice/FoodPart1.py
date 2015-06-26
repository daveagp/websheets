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
 Reference solution for Foodlympics Part One: Competitive Cuisine

 Description:  Reads in judge rankings for C countries by J judges.
               Prints out the rounded average score for each country,
               excluding the min and max.
**************************************************************************/

#include <iostream>
#include <cmath> // for round
using namespace std;

// excluding the min and max, compute the rounded average
// of the entries of judgeRatings
// J is the number of judges
int score(int judgeRatings[], int J) {

   int sum = 0;
   int min = judgeRatings[0];
   int max = judgeRatings[0];

   for (int i = 0; i < J; i++) {
      if (judgeRatings[i] > max)
         max = judgeRatings[i];
      if (judgeRatings[i] < min)
         min = judgeRatings[i];
      sum += judgeRatings[i];
   }                                         

   // eliminate min and max
   sum = sum - min - max;
        
   // average
   double ave = sum / (double) (J - 2);
        
   // rounded average, excluding min and max
   int score = (int) round(ave);
   return score;
}

// read the judges' ratings for several countries
// from standard input and print their overall scores
// to standard output
int main() {
   int C; // number of countries
   int J; // number of judges
   cin >> C >> J; // read the input

   cout << C << endl;       // first line of output

   // for each country, process their ratings
   for (int i = 0; i < C; i++) {

      // read the next line of input
      string name;
      cin >> name;

      int ratings[100];
      for (int j = 0; j < J; j++)
         cin >> ratings[j];

      // compute the overall score
      int overall = score(ratings, J);

      // output for this country
      cout << name << " " << overall << endl;
   }
}
 ]\ 
"""

tests = [
["""6 3
GER 1 13 20
BEL 15 15 15
AUT 17 18 3
CHF 19 7 19
LUX 14 14 15
LIE 7 8 9""", []],
["""3 6
Canada 10 16 10 20 14 10
Mexico 14 14 14 14 14 14
USA 7 14 20 12 15 16""", []],
["1 3\nPangaea 8 8 8", []],
["6 3\nLMH 1 2 3\nLHM 4 6 5\nMLH 8 7 9\nMHL 11 12 10\nHLM 15 13 14\nHML 18 17 16", []],
["6 3\nLLH 1 1 9\nLHL 1 9 1\nHLL 9 1 1\nLHH 1 9 9\n HLH 9 1 9\nHHL 9 9 1", []],
["2 3\noneLand 1 1 1\ntwentyStan 20 20 20", []],
["4 4\nmaxRepeat 18 18 7 5\nminRepeat 6 6 12 19\nbothRepeat 4 4 12 12\nfours 4 4 4 4", []]]
