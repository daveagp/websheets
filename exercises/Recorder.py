description = r"""
Make a short recorder that can store a message to be played back. It should have the following API:
<ul>
<li><tt>public Recorder(String initialMsg) // create new recorder w/this message initially
<li><tt>public String playback() // return the saved message
<li><tt>public void record(String newMsg) // save this message instead</tt>
</ul>
"""

source_code = r"""
// private instance variable representing the message
private \[String]\ savedMsg;

// constructor
public Recorder(\[String initialMsg]\) {
   // save the initial message
   \[savedMsg = initialMsg;]\
}

// accessor: get back the saved message
 \[public]\ String \[playback()]\ {
   return \[savedMsg]\;
}

// mutator: replace the saved message
\[
public void record(String newMsg) {
   // now the new message is saved (the old one is forgotten)
   savedMsg = newMsg;
}
]\

// test client
public static void main(String[] args) {
   Recorder r = new Recorder("hello");
   StdOut.println("The recorded message is: "  + r.playback());
   StdOut.println("Let's play it again:     "  + r.playback());
   r.record("bonjour");
   StdOut.println("The new message is:      "  + r.playback());       
   Recorder card = new Recorder("happy birthday!");
   StdOut.println("The new recorder says    "  + card.playback());       
   StdOut.println("The old one still says:  "  + r.playback());       
}
"""

tests = r"""
testMain();
"""
