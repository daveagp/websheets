source_code = r"""
#include <string>
#include <vector>
#include <iostream>
using namespace std;

int main() {
   vector<string> words;     // CONSTRUCT
   words.push_back("Hello"); // ADD to back end
   words.push_back("World"); 
   cout << words.size() << endl; // get SIZE
   cout << words[0] << " " << words.at(1) << endl; // [i], at(): ACCESS
   
   vector<int> nums(10); // CONSTRUCT with initial size 10
   // or use: vector<int> nums; nums.resize(10);
   for (int i=0; i<10; i++)
      nums[i] = i*i; // assign
   cout << nums.back() << endl; // ACCESS from back end
   nums.pop_back(); // DELETE (pop) from back end
   
   // FYI: iterator-type iteration (stay tuned in CS 104) 
   // but... it is more straightforward to use a normal for loop with size()
   for (vector<int>::iterator it=nums.begin(); it != nums.end(); it++)
      cout << *it << " ";

}
"""

lang = "C++"

example = True

description = "An example of vectors."

tests = [["", []]]
