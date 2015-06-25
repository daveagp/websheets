description = r"""
Create a class <tt>LineEdit</tt> to implement a text editor &mdash; a very primitive text editor that can only hold one line of text, 
and supports the following functions.
<pre>
// create a new LineEdit with given initial text
 LineEdit(string text)
// get the current state of the editor
 string to_string()
// add the given text at the end of the line
 void append(string text) 
// change the ith character to ch (you can assume it exists)
 void replace(int i, char ch)
// undo the latest append/replace operation that hasn't already been undone
 void undo()
</pre>
For example,
<pre>
LineEdit line("datatype");      // line.to_string() is now "datatype"
line.replace(4, 'h');           // line.to_string() is now "datahype"
line.append("st");              // line.to_string() is now "datahypest"
line.undo();                    // line.to_string() is now "datahype"
</pre>
The main purpose of this exercise is to gain familiarity with stacks &mdash;
use <tt>deque&lt;string&gt;</tt> to implement the history of changes and to
implement the <tt>undo()</tt> functionality. If the client
 calls <tt>undo()</tt> and everything has already been undone, then 
<tt>undo()</tt> should just return without changing the state.
"""

source_code = r"""
#include <deque>
#include <iostream>
using namespace std;

class LineEdit {
public:
   LineEdit(string text);
   string to_string();
   void append(string text);
   void replace(int i, char ch);
   void undo();
private:
// data members
\[
   string state;             // current state
   deque<string> oldStates;  // previous states for undo
]\
};

// create a new LineEdit with given initial text
LineEdit::LineEdit(string text) {
\[
   state = text;
]\
}

// get the current state of the editor
string LineEdit::to_string() {
\[
   return state;
]\
}

// add the given text at the end of the line
void LineEdit::append(string text) {
\[
   oldStates.push_back(state);
   state = state + text;
]\
}

// change the ith character to ch (you can assume it exists)
void LineEdit::replace(int i, char ch) {
\[
   oldStates.push_back(state);
   state[i] = ch;
]\
}

// undo the latest append/replaceEach operation that hasn't already been undone
void LineEdit::undo() {
// hint: use deque::empty()
\[
   if (!oldStates.empty()) { // avoid crashing when there's nothing to undo
      state = oldStates.back();
      oldStates.pop_back();
   }
]\
}

// test client
int main() {
   // test 1
   LineEdit line("datatype");
   cout << line.to_string() << endl;
   line.replace(4, 'h');
   cout << line.to_string() << endl;
   line.append("st");
   cout << line.to_string() << endl;
   line.undo();
   cout << line.to_string() << endl;
   cout << endl;

   // test 2
   LineEdit word("CSCI 103");
   cout << word.to_string() << endl;
   word.replace(7, '4');
   cout << word.to_string() << endl;
   word.replace(1, 'X');
   cout << word.to_string() << endl;
   word.undo();
   cout << word.to_string() << endl;
   word.append(" is the best");   
   cout << word.to_string() << endl;
   word.undo();
   cout << word.to_string() << endl;
   word.undo();
   cout << word.to_string() << endl;
   word.undo(); // nothing to undo, but shouldn't crash
   cout << word.to_string() << endl;
}
"""

tests = [["", []]]

lang = "C++"

attempts_until_ref = 0
