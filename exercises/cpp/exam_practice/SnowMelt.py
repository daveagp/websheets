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

/****************************************************************************
* Solution for Exam Part 2: SnowMelt
*
* Description: Simulates how fast the snow will melt 
*              based on how much salt is used and temp
* ***************************************************************************/

#include <cmath>
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

// using current snow, temperature and salt solution
// how much snow will melt?
double meltage(double currSnow, int temp, int salt) {
   double result = pow(1 + currSnow, (temp - 32 + 2*salt)/18.0);
   result = min(currSnow, result);
   return result;
}
    
// formatted printing of a double[] array
void printArray(double arr[], double length) {
   for (int i = 0; i < length; i++)
      cout << setw(8) << setprecision(3) << arr[i];

   // new line after all entries printed
   cout << endl;
}
    
// Part 2B: input data file from standard input
// input salt solution ints from command-line
// output remaining snow for each day for each salt solution
int main(int argc, char* argv[]) {
   // store salt for scenarios
   int N = argc-1;
   int salt[100];
   for (int i = 0; i < N; i++)
      salt[i] = atoi(argv[i+1]);
            
   // array of snow left on ground for each scenario
   double snowLeft[100];
        
   // input snow in inches and temp in degrees F for each day
   while (true) {
      // read data from standard input
      double newSnow;
      cin >> newSnow;
      int temp;
      cin >> temp;
      if (cin.fail())
         return 0; // input is done
            
      // compute meltage for one day with each salt value
      for (int i = 0; i < N; i++) {
         snowLeft[i] = snowLeft[i] + newSnow;
         double melt = meltage(snowLeft[i], temp, salt[i]);
         // how much snow left after the melting?
         snowLeft[i] = snowLeft[i] - melt;
      }
      printArray(snowLeft, N);
   }
}
]\
"""

tests = [
["8.0 21\n2.0 24\n0.0 45\n2.4 30\n1.9 19\n4.4 26", ["5"]],
["8.0 21\n2.0 24\n0.0 45\n2.4 30\n1.9 19\n4.4 26", ["10"]],
["8.0 21\n2.0 24\n0.0 45\n2.4 30\n1.9 19\n4.4 26", ["2"]],
["8.0 21\n2.0 24\n0.0 45\n2.4 30\n1.9 19\n4.4 26", ["5", "10"]],
["8.0 12\n12.0 -5\n0.0 -2\n2.4 6\n0.9 23\n0.1 23\n1.3 39", ["0", "3", "6"]],
["0.0 13", ["5", "10", "20"]],
["108.0 200\n102.7 200\n10000 200", ["0", "7", "14"]],
["102.0 -199\n100.0 -145\n102.4 -200\n101.9 -119\n104.4 -126", ["3", "9", "20"]],
["1.6 27\n0.1 -4\n1.5 26\n3.4 77\n7.7 -13\n3.6 75\n6.0 -10\n7.5 49\n6.2 -6\n4.7 -36\n8.1 49\n7.6 -18\n0.8 -25\n2.0 31\n1.1 69\n6.6 27\n9.6 -26\n4.4 -7\n8.6 -11\n3.1 51\n8.0 -26\n3.1 71\n2.3 -4\n6.6 50\n3.0 36\n4.0 62\n1.4 30\n2.8 -4\n5.3 53\n4.5 12\n6.9 -34\n9.5 25\n9.6 31\n6.8 -20\n6.6 36\n9.3 59\n1.8 32\n7.4 8\n0.2 -35\n5.8 14\n3.3 7\n1.4 33\n0.0 0\n2.3 42\n2.1 15\n8.7 40\n3.9 -30\n0.5 76\n3.7 -11\n10.0 74\n9.3 18\n2.3 21\n8.1 23\n3.0 77\n3.0 60\n9.8 3\n7.3 12\n2.8 -11\n0.8 35\n1.6 24\n9.2 -27\n6.2 -16\n0.5 51\n8.4 77\n9.5 -40\n7.0 -2\n6.6 -16\n8.2 -30\n1.5 65\n5.6 52\n1.1 -40\n7.0 71\n8.7 -15\n7.8 -10\n8.2 14\n4.3 -7\n8.6 61\n8.1 -39\n5.7 4\n3.1 53\n1.0 74\n8.0 20\n8.8 -14\n3.3 60\n1.7 16\n2.6 -9\n1.6 1\n7.0 51\n7.2 -21\n6.1 33\n3.5 20\n6.5 9\n5.5 -15\n2.0 39\n0.5 7\n1.2 39\n", ["2", "12", "30"]]]

