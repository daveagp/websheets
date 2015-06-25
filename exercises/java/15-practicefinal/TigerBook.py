description = r"""
<i>COS 126 Spring 2013 Programming Midterm 2, part 2/2</i><br>
Please see the problem description in <a href="http://www.cs.princeton.edu/courses/archive/fall13/cos126/docs/mid2-s13-prog.pdf">
this PDF link</a>. 
<p>
This websheet is intended as a practice exam. However, in a real exam,
<ul>
<li>You'll upload via Dropbox
<li>You'll get limited feedback from Dropbox during the exam, and a different full set of test cases for grading
<li>Real humans will grade your real exams and also mark you on style and apply partial credit where appropriate
<li>Because of Websheet formatting, on this page you have to put your header inside the class. On the exam, put it at the top as usual
<li>We recommend coding in DrJava and/or the command-line and doing basic tests on your own, then copying here for full testing
<li>The exam grader is generally less picky about output whitespace than the Websheet grader.
</ul>
We recommend doing this practice in a timed environment; give yourself 90 minutes.
<p>
<b>You have to solve the <a href='?group=Person'>Person</a> websheet before this one will work.</b> (But in a real exam, you don't necessarily need
to complete one part to get credit for the next.)
"""

source_code = r"""
public class TigerBook { 
\[
/************************************************************************* 
 Reference solution for Spring 2013 COS 126 Programming Exam 2: TigerBook

 Author:       COS 126 Staff
 Netid:        cos126
 Precepts:     lots of them
 Dependencies: Person, ST

 Description:  Models a collection of users (Person objects) each with
               a unique id (String).

**************************************************************************/
    private ST<String, Person> users;  // map each id to a user

    // Constructor
    public TigerBook() {
        users = new ST<String, Person>();
    }

    // Add a person to the list of users.
    // We are allowed to assume this id was not registered yet.
    public void register(String id, Person p) {
        users.put(id, p);
    }

    // Return the person registered with this id.
    // Throw a RuntimeException if no such person exists.
    public Person lookup(String id) {

        // Was this id String registered?
        if (!users.contains(id))
            throw new RuntimeException("User id not found");

        // return the right Person
        return users.get(id);
    }
]\
\hide[
    public static void exampleClientMain(String[] args) {
        TigerBook tb = new TigerBook(); 

        while (!StdIn.isEmpty()) {

            String first = StdIn.readString(); // first word on line
            
            if (first.startsWith("//")) { // is this line a comment?
                StdIn.readLine();         // if so, skip the rest of the line
                continue;                 // and don't try to read an action
            }

            String name = first;                // the first word is a person 
            String action = StdIn.readString(); // now, read the action

            // now translate the action to method calls
            if (action.equals("registers")) {
                Person newUser = new Person(name);
                tb.register(name, newUser);
            }
            else if (action.equals("meets")) {
                String name2 = StdIn.readString();
                Person user1 = tb.lookup(name);
                Person user2 = tb.lookup(name2);
                user1.meet(user2);
            }
            else if (action.equals("posts")) {
                String message = StdIn.readLine(); // read rest of line
                message = message.substring(1);    // get rid of space at start
                Person user = tb.lookup(name);
                user.post(message);
            }
            else if (action.equals("queries")) {
                String name2 = StdIn.readString();
                Person user1 = tb.lookup(name);
                Person user2 = tb.lookup(name2);
                StdOut.print("Are "+name+" and "+name2+" friends? ");
                boolean isFriend = user1.knows(user2);
                StdOut.println(isFriend);
            }
            else if (action.equals("reads")) {
                Person user = tb.lookup(name);
                user.listMessages();
            }
            else {
                // this case would be triggered by a line like "person1 coughs"
                // but could also be caused by typos, or putting too many words
                // on one line, or not enough words on one line, etc
                String msg = "ExampleClient doesn't know how to perform action";
                msg += " \""+action+"\"\n Your input is misformatted, ";
                msg += "see the ExampleClient header comment for help";
                throw new RuntimeException(msg);
            }
        }
    }    
]\
}
"""

tests = r"""
saveAs = "t";
testConstructor();
saveAs = "first";
construct(null, "Person", "", "Tony");
testOn("t", "register", "tony10010", var("first"));
saveAs = "personFound";
testOn("t", "lookup", "tony10010");
testOn("personFound", "listMessages");
expectException = true;
saveAs = "nobody";
testOn("t", "lookup", "tony-the-tiger");
stdinURL = "http://www.cs.princeton.edu/courses/archive/spring13/cos126/docs/data/TigerBook/friendly.txt";
testNamedMain("exampleClientMain", "ExampleClient");
stdinURL = "http://www.cs.princeton.edu/courses/archive/spring13/cos126/docs/data/TigerBook/mutual.txt";
testNamedMain("exampleClientMain", "ExampleClient");
stdinURL = "http://www.cs.princeton.edu/courses/archive/spring13/cos126/docs/data/TigerBook/networking.txt";
testNamedMain("exampleClientMain", "ExampleClient");
stdinURL = "http://www.cs.princeton.edu/courses/archive/spring13/cos126/docs/data/TigerBook/monologue.txt";
testNamedMain("exampleClientMain", "ExampleClient");
"""

dependencies = ["Person"]
