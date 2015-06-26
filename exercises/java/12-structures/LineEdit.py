description = r"""
Create a class <tt>LineEdit</tt> to implement a text editor &mdash; a very primitive text editor that can only hold one line of text, 
and supports the following functions.
<pre>
// create a new LineEdit with given initial text
 public LineEdit(String text)
// get the current state of the editor
 public String toString()
// add the given text at the end of the line
 public void append(String text) 
// replace all occurrences of "from" with "to"
 public void replaceEach(String from, String to)
// undo the latest append/replaceEach operation that hasn't already been undone
 public void undo()
</pre>
For example,
<pre>
LineEdit line = new LineEdit("datatype"); // line.toString() is now "datatype"
line.replaceEach("t", "");                // line.toString() is now "daaype"
line.append("st");                        // line.toString() is now "daaypest"
line.undo();                              // line.toString() is now "daaype"
</pre>
The main purpose of this exercise is to gain familiarity with stacks &mdash;
use <tt>Stack&lt;String&gt;</tt> to implement the history of changes and to
implement the <tt>undo()</tt> functionality. If the client
 calls <tt>undo()</tt> and everything has already been undone, then 
<tt>undo()</tt> should just return without changing the state.
Use <tt><a href="http://docs.oracle.com/javase/7/docs/api/java/lang/String.html#replace(java.lang.CharSequence, java.lang.CharSequence)">String.replace</a></tt> to perform the changes required by the <tt>replaceEach</tt> instance method.
"""

source_code = r"""
// instance variables
\[
String state;                                   // current state
Stack<String> oldStates = new Stack<String>();  // previous states for undo
]\

// create a new LineEdit with given initial text
public LineEdit(String text) {
\[
   state = text;
]\
}

// get the current state of the editor
public String toString() {
\[
   return state;
]\
}

// add the given text at the end of the line
public void append(String text) {
\[
   oldStates.push(state);
   state = state + text;
]\
}

// replace all occurrences of "from" with "to"
public void replaceEach(String from, String to) {
\[
   oldStates.push(state);
   state = state.replace(from, to);
]\
}

// undo the latest append/replaceEach operation that hasn't already been undone
public void undo() {
\[
   if (!oldStates.isEmpty())  // avoid crashing when there's nothing to undo
      state = oldStates.pop();
]\
}

// test client
public static void main(String[] args) {
   LineEdit line = new LineEdit("datatype");
   System.out.println(line.toString());
   line.replaceEach("t", "");
   System.out.println(line.toString());
   line.append("st");
   System.out.println(line.toString());
   line.undo();
   System.out.println(line.toString());
}
"""

tests = r"""
testMain();
saveAs = "word";
testConstructor("COS 226");
testOn("word", "toString");
testOn("word", "replaceEach", "22", "12");
testOn("word", "toString");
testOn("word", "replaceEach", "wierd", "weird");
testOn("word", "toString");
testOn("word", "append", " is the best");
testOn("word", "toString");
testOn("word", "undo");
testOn("word", "toString");
testOn("word", "undo");
testOn("word", "toString");
saveAs = "emacs";
testConstructor("your code shouldn't crash even if there's nothing to undo");
testOn("emacs", "toString");
testOn("emacs", "undo");
testOn("emacs", "toString");
testOn("word", "replaceEach", "O", "oh");
testOn("word", "toString"); 
testOn("word", "undo");
testOn("word", "toString"); 
testOn("word", "undo");
testOn("word", "toString"); 
"""
