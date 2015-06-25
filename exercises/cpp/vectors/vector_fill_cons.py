attempts_until_ref = 0

source_code = r"""
#include <vector>
#include <iostream>
using namespace std;

void print_vector(vector<int> v) {
   for (int i=0; i<\[v.size()]\; i++) {
      cout << v[i] << " ";
   }
   cout << endl;
}

int main() {
   // create the phone number 8 8 8 8 8 8 8 8 8 8
   vector<int> phone_number(10, 8);
   // create the zip code 9 9 9 9 9
   vector<int> zip_code(\[5, 9]\);

   print_vector(phone_number);
   print_vector(zip_code);
}
"""

lang = "C++"

tests = [["", []]]

description = r"""
Using the vector fill constructor.
"""

