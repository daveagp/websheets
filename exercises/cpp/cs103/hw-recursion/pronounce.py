source_code = r"""
#include <iostream>
using namespace std;

// this function prints out the English pronunciation of n
void pronounce(int n) {
   // base cases
   if (n<20) {
      const char* units[] = {"zero", "one", "two", "three", "four",
                             "five", "six", "seven", "eight", "nine",
                             "ten", "eleven", "twelve", "thirteen",
                             "fourteen", "fifteen", "sixteen", "seventeen",
                             "eighteen", "nineteen"};
      cout << units[n];
   }
   // more base cases
   else if (n%10==0 && n<100) {
      const char* tenfolds[] = {"", "ten", "twenty", "thirty", "forty",
                               "fifty", "sixty", "seventy", "eighty", "ninety"};
      cout << tenfolds[n/10];
   }
   else if (n<100) {
      // pronounce the tens place
      pronounce(\[n - (n%10)]\);
      // pronounce the ones place
      cout << "-";
      pronounce(\[n%10]\);
   }
   // exact multiple of 100
   else if (n%100==0 && n<1000) {
      \[pronounce(n/100);]\
      cout << " hundred";
   }
   else if (n<1000) {
      pronounce(n - (n%100));
      cout << " ";
      pronounce(n%100);
   }
   else if (n<1E6) {
      // how many thousands?
      \[pronounce(n/1000)]\;
      cout << " thousand";
      
      // what else?
      if (n%1000 != 0) {
         cout << " ";
         pronounce(\[n%1000]\);
      }
   }
   else if (n<1E9) {
      pronounce(n/(int)1E6);
      cout << " million";
      if (n%(int)1E6 != 0) {
         cout << " ";
         pronounce(n%(int)1E6);
      }
   }
   else { // INT_MAX is less than a trillion
      pronounce(n/(int)1E9);
      cout << " billion";
      if (n%(int)1E9 != 0) {
         cout << " ";
         pronounce(n%(int)1E9);
      }
   }
}

int main() {
   int n;
   cin >> n;
   pronounce(n); 
}
"""

lang = "C++"

description = r"""
Define a function <tt>void pronounce(int n)</tt> that prints out 
(to <tt>cout</tt>) the English spelling of <tt>n</tt>. For example,
<ul>
<li>
<tt>pronounce(25);</tt> prints <tt>twenty-five</tt>
<li>
<tt>pronounce(103);</tt> prints <tt>one hundred three</tt>
<li>
<tt>pronounce(2014);</tt> prints <tt>two thousand fourteen</tt>
<li>
<tt>pronounce(999999);</tt> prints <tt>nine hundred ninety-nine thousand nine hundred ninety-nine</tt>
</ul>
"""

tests = [
    ["5", []],
    ["20", []],
    ["25", []],
    ["100", []],
    ["103", []],
    ["218", []],
    ["620", []],
    ["2014", []],
    ["999999", []],
    ["1021509", []],
    ["1234567890", []],
]



