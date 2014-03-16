description = r"""
Create a 'combination lock' which has a <tt>String</tt> password that you can change,
which you can lock and unlock. It should have this API:
<ul>
<style>li {margin-bottom: 9pt;} </style>
<li><tt>
// construct new lock with this initial password, initially unlocked<br>
public CombinationLock(String initpass) 
</tt>
<li><tt>// is this lock currently locked?<br>public boolean isLocked()</tt>
<li><tt>// if current password equals attempt, unlock (no effect if already unlocked)<br>
public void tryUnlock(String attempt)</tt>
<li><tt>// make this lock become locked (no effect if already locked)<br>public void lock()</tt>
<li><tt>// if locked, print "ERROR: LOCKED" else change password to newpass<br>
public void changePassword(String newpass)</tt>
</ul>
Make sure you use <tt>.equals()</tt> to compare strings in <tt>tryUnlock()</tt>, not the <tt>==</tt> operator. 
<i>Note: in practice, passwords are not stored directly, but only as <b>hashes</b>."""

source_code = r"""\[
private boolean locked; // is it locked right now?
private String password; // current password

// construct new lock with this initial password, initially unlocked
public CombinationLock(String initpass) {
   password = initpass; // save password
   locked = false; // initially unlocked
}

// is this lock currently locked? 
public boolean isLocked() {
   return locked;
}

// if current password equals attempt, unlock (no effect if already unlocked)
public void tryUnlock(String attempt) {
   if (attempt.equals(password))
      locked = false;
}

// make this lock become locked (no effect if already locked)
public void lock() {
   locked = true;
}

// if locked, print "ERROR: LOCKED" else change password to newpass
public void changePassword(String newpass) {
   if (locked) 
      StdOut.println("ERROR: LOCKED");
   else
      password = newpass;
}
]\ 

"""

tests = r"""
saveAs = "myLock";
testConstructor("0000");
testOn("myLock", "isLocked");
testOn("myLock", "lock");
testOn("myLock", "changePassword", "my-new-password");
testOn("myLock", "isLocked");
testOn("myLock", "tryUnlock", "2014");
testOn("myLock", "isLocked");
testOn("myLock", "tryUnlock", "0000");
testOn("myLock", "isLocked");
testOn("myLock", "changePassword", "hello123");
testOn("myLock", "isLocked");
testOn("myLock", "lock");
testOn("myLock", "isLocked");
testOn("myLock", "tryUnlock", "0000");
testOn("myLock", "isLocked");
testOn("myLock", "tryUnlock", "hello123");
testOn("myLock", "isLocked");
testOn("myLock", "lock");
testOn("myLock", "isLocked");
"""
