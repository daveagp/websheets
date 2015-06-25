attempts_until_ref = 0

source_code = r"""
#include <iostream>
#include <vector>

using namespace std;

void print_list(vector<int> &myvec)
{
  // declare an i counter
  \[int ]\ i;
  // complete the for loop and its body
  for(\[ i=0   ]\ ; \[ i < myvec.size() ]\; i++ ){
     cout << \[ myvec[i] ]\ << " ";
  }
  cout << endl;
}


int main(int argc, char *argv[])
{
  vector<int> lst;

  cout << "Added 1, 2, 3, and 9 to list 1" << endl;
  // add code to put 1, 2, 3, and 9 into the vector in that order
  \[
    lst.push_back(1);
    lst.push_back(2);
    lst.push_back(3);
    lst.push_back(9);
  ]\

  print_list( lst );

  // print out the number of items (list size) in the list
  cout << \[ lst.size() ]\ << endl;



  // print out the front item
  cout << \[ lst.front() ]\ << endl;

  // delete the item at index 1 in the lines of code after the cout
  cout << "Removing second item (i.e. at index 1): " << endl;
  
  \[
  lst.erase(lst.begin()+1);
  ]\

  // will print the resulting list
  print_list( lst );

  // add code to put 120, 121, 122 onto the front of the list 
  // so that 120 is at location 0, 121 at location 1, etc.
  //  use the insert() method after the cout line below
  cout << "Adding 120, 121, 122" << endl;

  \[
   lst.insert(lst.begin(), 120);
   lst.insert(lst.begin()+1, 121);
   lst.insert(lst.begin()+2, 122);

  ]\



  print_list( lst );
  return 0;
}
"""
lang = "C++"
tests = [["", []]]

description = """Fill in the blanks with appropriate code to implement
the directions given in the comments.
"""
