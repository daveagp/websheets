source_code = r"""
#include <iostream>
#include <cstring>
using namespace std;


int main() {
  // store 10 user names 
  char* names[10];
 
  char temp_buf[50];
  for(int i=0; i < 10; i++) {
   \[
    cin >> temp_buf;
    names[i] = new char[strlen(temp_buf)+1];
    strcpy(names[i], temp_buf);
    \show:
    cin >> names[i]; // this is not correct!
   ]\
  }

  // now print the names
  for(int i=0; i < 10; i++){
    cout << names[i] << " ";
  }  
  cout << endl;

  // I want to change names[0] and names[1]
\[  
  cin >> temp_buf; // user enters "Al"
  delete[] names[0];
  names[0] = new char[strlen(temp_buf)+1];
  strcpy(names[0], temp_buf);

  cin >> temp_buf; // user enters "Grace"
  delete[] names[1];
  names[1] = new char[strlen(temp_buf)+1];
  strcpy(names[1], temp_buf);
  \show:
  cin >> temp_buf; // user enters "Al"
  names[0] = temp_buf;
  cin >> temp_buf; // user enters "Grace"
  names[1] = temp_buf;
]\

  // print the names again
  for(int i=0; i < 10; i++){
    cout << names[i] << " ";
  }  
  cout << endl;

  // now free/delete the memory you allocated
\[
  for(int i=0; i < 10; i++){
    delete[] names[i];
  }
  \show:
  ;
]\
  return 0;
}
"""

lang = "C++"

description = r"""
Write code to receive 10 names of less than 50 characters but only
use the minimum amount of memory to store those 10 names.
<p>
Today, add the following features:
<ul>
<li>Don't allocate more dynamic memory than absolutely necessary.
<li>Add code to change the first two names. Remember to recycle 
<i>all</i> unused memory!
</ul>
"""

tests = [
    ["Tim Chris Jen JackTwentyFourLetterName Phil Bill Raffi Melissa Pete Megan\nAl Grace", []]
]

attempts_until_ref = 0

