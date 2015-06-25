source_code = r"""
#include <vector>
#include <iostream>
using namespace std;

vector<int> merge(vector<int>& input, int s1, int e1, int s2, int e2)
{
  vector<int> result;
\[
  while(s1 < e1 && s2 < e2){
    if(input[s1] < input[s2]){
      result.push_back(input[s1++]);
    }
    else {
      result.push_back(input[s2++]);
    }
  }
  while(s1 < e1){
    result.push_back(input[s1++]);
  }
  while(s2 < e2){
    result.push_back(input[s2++]);
  }
]\
  return result;
}

void print_vec(vector<int> input){
  for(vector<int>::iterator it = input.begin();
      it != input.end();
      ++it){
    cout << *it << " ";
  }
  cout << endl;
}
int main()
{
  int d1[] = {2,9,10,16,3,4,5,6};
  vector<int> v1(d1, d1+8);
  print_vec( merge(v1,0,4,4,8) );

  int d2[] = {1,2,3,4,7,8,5,6};
  vector<int> v2(d2, d2+8);
  print_vec( merge(v2,4,6,6,8) );

  vector<int> v3;
  print_vec( merge(v3,0,0,0,0) );

  return 0;

}
"""

lang = "C++"

description = r"""
Write a function to merge two sorted ranges of a vector.  Assum the values in teh input vector between [s1,e1) and [s2,e2) are non-overlapping, sorted sequences of integers.  Create a new vector 'retval' that has the merged, sorted values from those two ranges.  

For example, if input is { 2, 5, 3, 4 } and s1=0,e1=2, s2=2,e2=4 should yield a merged result of { 2, 3, 4, 5}
"""

tests = [["", []]] # stdin, args
