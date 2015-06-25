attempts_until_ref = 0
lang = "C++"
tests = [["", []]]

description = r"""
Create a 'combination lock' which has a <tt>string</tt> password that you can change,
which you can lock and unlock. It should have this API:
<ul>
<style>li {margin-bottom: 9pt;} </style>
<li><tt>
// construct new lock with this initial password, initially unlocked<br>
CombinationLock(string initpass) 
</tt>
<li><tt>// is this lock currently locked?<br>bool isLocked()</tt>
<li><tt>// if current password equals attempt, unlock (no effect if already unlocked)<br>
void tryUnlock(string attempt)</tt>
<li><tt>// make this lock become locked (no effect if already locked)<br>void lock()</tt>
<li><tt>// if locked, print "ERROR: LOCKED" else change password to newpass<br>
void changePassword(string newpass)</tt>
</ul>

<i>Note: in practice, passwords are not stored directly, but only as <a href="http://en.wikipedia.org/wiki/Cryptographic_hash_function#Password_verification">hashes</a>."""

source_code = r"""
#include <iostream>
#include <string>
using namespace std;
\[
class CombinationLock {
public:
   CombinationLock(string initpass);
   void tryUnlock(string attempt);
   bool isLocked();
   void lock();
   void changePassword(string newpass);
private:
   bool locked; // is it locked right now?
   string password; // current password
};

// construct new lock with this initial password, initially unlocked
CombinationLock::CombinationLock(string initpass) {
   password = initpass; // save password
   locked = false; // initially unlocked
}

// is this lock currently locked? 
bool CombinationLock::isLocked() {
   return locked;
}

// if current password equals attempt, unlock (no effect if already unlocked)
void CombinationLock::tryUnlock(string attempt) {
   if (attempt == password)
      locked = false;
}

// make this lock become locked (no effect if already locked)
void CombinationLock::lock() {
   locked = true;
}

// if locked, print "ERROR: LOCKED" else change password to newpass
void CombinationLock::changePassword(string newpass) {
   if (locked) 
      cout << "ERROR: LOCKED" << endl;
   else
      password = newpass;
}
]\

int main() {
   cout << boolalpha;
   CombinationLock myLock("0000");
   cout << myLock.isLocked() << endl; // false
   myLock.lock();
   cout << myLock.isLocked() << endl; // true
   myLock.changePassword("new-pass"); // -- ERROR: LOCKED
   cout << myLock.isLocked() << endl; // true
   myLock.tryUnlock("2014"); // -- shouldn't unlock, password is 0000
   cout << myLock.isLocked() << endl; // true
   myLock.tryUnlock("0000"); // -- unlocks!
   cout << myLock.isLocked() << endl; // false
   myLock.changePassword("hello123"); // -- password change OK
   cout << myLock.isLocked() << endl; // false
   myLock.lock();
   cout << myLock.isLocked() << endl; // true
   myLock.tryUnlock("0000"); // -- shouldn't unlock, wrong password now
   cout << myLock.isLocked() << endl; // true
   myLock.tryUnlock("hello123"); // -- unlocks!
   cout << myLock.isLocked() << endl; // false
   myLock.lock();
   cout << myLock.isLocked() << endl; // true
   return 0;
}
"""

