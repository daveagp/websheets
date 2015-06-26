attempts_until_ref = 0

description = r"""
Make a short recorder that can store a message to be played back. It should have the following API:
<ul>
<li><tt>Recorder(string initialMsg) // create new recorder w/this message initially
<li><tt>string playback() // return the saved message
<li><tt>void record(string newMsg) // save this message instead</tt>
</ul>
"""

lang = "C++"

source_code = r"""
#include <string>
#include <iostream>
using namespace std;

// normally this would go in recorder.h
class Recorder {
public:
   Recorder(string initialMsg);
   string playback();
   void record(string newMsg);
private:
   string savedMsg;
};

// normally this would go in recorder.cpp
// constructor
Recorder::Recorder(\[string initialMsg]\) {
   // save the initial message
   \[savedMsg = initialMsg;]\
}

// accessor: get back the saved message
string Recorder::\[playback()]\ {
   return \[savedMsg]\;
}

// mutator: replace the saved message
\[
void Recorder::record(string newMsg) {
   // now the new message is saved (the old one is forgotten)
   savedMsg = newMsg;
}
]\

// test client
int main() {
   Recorder r("hello");
   cout << "The recorded message is: " << r.playback() << endl;
   cout << "Let's play it again:     " << r.playback() << endl;
   r.record("bonjour");
   cout << "The changed message is:  " << r.playback() << endl;       
   Recorder card("happy birthday!");
   cout << "The new recorder says:   " << card.playback() << endl;       
   cout << "The old one still says:  "  + r.playback() << endl;       
}
"""

tests = [["", []]]
