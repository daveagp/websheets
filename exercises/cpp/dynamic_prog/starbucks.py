attempts_until_ref = 0

description = r"""
This program should read from cin a data file of the format
<pre>
cardvalue
N
price1 price2 ... priceN
</pre>
where all values are integers. You have a gift card worth <tt>cardvalue</tt>,
and the store sells items costing <tt>price1</tt>, <tt>price2</tt>, ... <tt>priceN</tt>.
Print out the maximum amount that you can spend without exceeding <tt>cardvalue</tt>.
<p>
For example, if the input is
<pre>
100
5
40 23 88 32 20
</pre>
then the output should be <tt>95</tt>, which you can attain by buying the items worth 40, 23 and 32.
"""

lang = "C++"

source_code = r"""
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char* argv[]) {
   // read the input
   int cardvalue, N;
   cin >> cardvalue >> N;
   int price[N]; // bad style, VLA
   for (int i=0; i<N; i++) cin >> price[i];   

   // declare the dynamic programming table
   // first index: remaining cash
   // second index: items left to consider
   int best_spend[cardvalue+1][N+1]; // bad style, VLA
   
   for (int limit=0; limit<=cardvalue; limit++) {
      for (int items_left=0; items_left<=N; items_left++) {
         // compute best_spend[limit][items_left]
         int result = 0;
         // try not buying this item
\[
         if (items_left > 0)
            result = max(result, best_spend[limit][items_left-1]);
]\
         // try buying this item
\[
         if (items_left > 0 && limit >= price[N-items_left]) {
            int p = price[N-items_left];
            result = max(result, p + best_spend[limit - p][items_left-1]);
         }
]\
         best_spend[limit][items_left] = result;
      }
   }
   // print out entry for full card value and all items
   cout << \[best_spend[cardvalue][N]]\ << endl;
}
"""

tests = [
    ["100\n5\n40 23 88 32 20", []],
    ["200\n5\n40 23 88 32 20", []],
    ["90\n5\n40 23 88 32 20", []],
    ["10\n5\n40 23 88 32 20", []],
    ["1000\n5\n40 23 88 32 20", []],
    ["10000\n10\n1826 2048 1141 1386 455 1729 619 1287 1273 1569", []],
    ["80000\n20\n12271 13721 22971 14621 35441 19951 27871 12441 33161 29551 13711 11711 13601 38691 12321 15351 26011 34292 16051 14190", []]
]

