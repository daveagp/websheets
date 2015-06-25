attempts_until_ref = 0

source_code = r"""
#include <iostream>
#include <string>
#include <set>

using namespace std;

// C++ set and map want to compare keys with a 
//  '<' operation.  Comparator objects need
//  an operator() with 2 arguments of the key type
struct StrPtrComp {
\[ bool operator() ]\(string* s1, string* s2)
  {
\[
    return *s1 < *s2;
]\
  }
};

int main()
{
  const int SIZE = 8;
  string* ptrarray[SIZE];
  ptrarray[0] = new string("Hello");
  ptrarray[1] = new string("Hola");
  ptrarray[2] = new string("An-yeong");
  ptrarray[3] = new string("Ni hao");
  ptrarray[4] = new string("Bonjour");
  ptrarray[5] = new string("Head nod");
  ptrarray[6] = new string("Hello");
  ptrarray[7] = new string("Hola");
  // 0 = use default comparator, 1 = your StrPtrComp
  int choice;
  cin >> choice;
  if(choice == 0){
    set<string*> myset;
    for(int i=0; i < SIZE; i++){
      myset.insert(ptrarray[i]);
    }
    cout << "Set has " << myset.size() << " keys!" << endl;
  }
  else {
    StrPtrComp comp;
    set<string*, StrPtrComp> myset(comp);
    for(int i=0; i < SIZE; i++){
      myset.insert(ptrarray[i]);
    }
    cout << "Set has " << myset.size() << " keys!" << endl;
  }
  return 0;
}
"""

lang = "C++"
tests = [["0", []],
         ["1", []]]

description = """Fill in the blanks to create an appropriate Comparator 
object functor that can compare the strings pointed to by the two arguments.
"""
