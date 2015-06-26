source_code = r"""
#include <iostream>
#include <string>
using namespace std;

class TwoInts {
private:
   int* data;

public:
   TwoInts(int first, int second) {
      data = new int[2];
      data[0] = first;
      data[1] = second;
   }

   ~TwoInts() {
      delete[] data;
   }

\[
   TwoInts(const TwoInts& c) {
      data = new int[2];
      data[0] = c.data[0]; data[1] = c.data[1];
   } 
\show:
   ;// todo?
]\

   int get_first() { return data[0]; }
   int get_second() { return data[1]; }
};

int biggest_of(TwoInts pair) {
   return max(pair.get_first(), pair.get_second());
}

int main() {
   TwoInts nums(10, 33);
   cout << nums.get_first() << " " << nums.get_second() << endl;
   cout << biggest_of(nums) << endl;
   cout << nums.get_first() << " " << nums.get_second() << endl;
}

"""

lang = "C++"

description = r"""
A memory bug.
"""

tests = [["", []]] # stdin, args

attempts_until_ref = 0
