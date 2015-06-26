attempts_until_ref = 0

source_code = r"""
#include <iostream>
#include <string>
using namespace std;

// counter.h
class Counter {
public:
   Counter();
   void add_one();
   void add_one_and_print();
private:
   int value;
};

// counter.cpp
Counter::Counter() {
   value = 0;
}

void Counter::add_one() {
   value++;
}
   
void Counter::add_one_and_print() {
   // how do we call a method on the current object?
   \[add_one();\show:the_count.add_one();]\
   cout << value << endl;
}

// test code
int main() {
   Counter the_count;
   the_count.add_one_and_print();
}
"""

lang = "C++"

description = r"""
Calling a member function from inside of another member function.
"""

tests = [["", []]] # stdin, args


