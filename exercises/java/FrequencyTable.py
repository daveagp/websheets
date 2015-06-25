description = r"""
The class <tt>FrequencyTable</tt> represents a table that tracks
the number of repeated occurrences of items in a list of Strings. It has 
the API
<pre>
public FrequencyTable()           // new table
public void click(String word)    // add 1 to frequency of this word
public int count(String word)     // what is frequency of this word?
public void show()                // print out all words and frequencies
</pre>
For example,
<pre>
FrequencyTable ft = new FrequencyTable();
ft.click("duck");
ft.click("duck");
ft.click("goose");
StdOut.println(ft.count("duck"));  // should print 2
StdOut.println(ft.count("goose")); // should print 1
StdOut.println(ft.count("horse")); // should print 0
</pre>
In addition, create a <tt>main</tt> that takes no arguments, reads words
from standard input (using <tt>StdIn.readString()</tt>) until none are left,
and then prints out the frequencies of all words using <tt>show()</tt>.
<div class="noprint">
You will need to know the <a href="http://introcs.cs.princeton.edu/java/44st/"><tt>ST</tt> API</a>: look up the constructor, <tt>put</tt> and <tt>get</tt>.
</div>
<div class="printonly">
Here are the relevant components of the ST API:
<pre>public class ST&lt;Key, Value&gt;              // Note: Key must be Comparable
------------------------------------------------------------------------
ST&lt;Key, Value&gt;()           // create a symbol table
void put(Key key, Value v) // put key-value pair into the table
Value get(Key key)         // return value paired with key
                           // or null if no such value
boolean contains(key Key)  // is there a value paired with key?
// Allows iteration with enhanced for loops:
for (Key key : st) {...}   // executes body once for each key
</pre>
</div>
"""

source_code = r"""
    // Dependencies: ST.java (available on precepts page), StdIn, StdOut
    // maintain counts of all words seen so far
    // the key is the word and the value is the count
    private ST<\[String, Integer]\> st = \[new ST<String, Integer>()]\;

    // remark: we have not declared a constuctor! but Java lets every class 
    // have a no-argument constructor by default. It only runs the line of 
    // code above (instance variable initialization).

    // add 1 to the frequency of this word
    public void click(String word) {
        int count = count(word);
        st.put(word, count + 1);
    }

    // what is the frequency of this word?
    public int count(String word) {
        if (!st.\[contains]\(\[word]\)) return 0;  // if word is not in ST
        else return \[st]\.\[get]\(\[word]\);        // get word's count
    }

    // print out all words and frequencies
    public void show() {
        // foreach loop. goes through all keys in alphabetical order
        for (String word : st) {
            // print out frequency and word, separated by a space
            StdOut.println(\[count]\(\[word]\) + " " + \[word]\);
        }
    }

    // method used by client to count all words in StdIn
    public static void main(String[] args) {

        // build frequency table from words on standard input
        FrequencyTable freq = new FrequencyTable();
        while (!StdIn.isEmpty()) {
            String word = StdIn.readString();
            freq.\[click]\(word);
        }

        // print frequency table to standard output
        freq.show();
    }
"""

tests = r"""
saveAs = "ft";
testConstructor();
testOn("ft", "click", "duck");
testOn("ft", "count", "duck");
testOn("ft", "click", "duck");
testOn("ft", "click", "goose");
testOn("ft", "count", "duck");
testOn("ft", "count", "goose");
testOn("ft", "count", "horse");
stdin = "in this test the api is tested by the words in the sentence";
testMain();
maxOutputBytes = 500000;
stdinURL = "http://introcs.cs.princeton.edu/java/44st/mobydick.txt";
testMain();
"""
