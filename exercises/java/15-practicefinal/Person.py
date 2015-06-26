description = r"""
<i>COS 126 Spring 2013 Programming Midterm 2, part 1/2</i><br>
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
"""

source_code = r"""
public class Person { 
\[
/*************************************************************************
 Reference solution for Spring 2013 COS 126 Programming Exam 2: Person

 Author:       COS 126 Staff
 Netid:        cos126
 Precepts:     lots of them
 Dependencies: Stack, Queue, StdOut

 Description:  Models a person, a list of messages that they can
               read, and a list of their friends, so that when you
               post a message, all your friends can read it too.

**************************************************************************/
    private String name;
    private Queue<Person> friends; // Stack or Queue, doesn't matter
    private Stack<String> wall;    // Stack, so newest is iterated first

    // Create a new Person with this name.
    public Person(String name) {
        this.name = name;
        this.friends = new Queue<Person>();
        this.wall = new Stack<String>();
    }

    // Make these two people become friends with each other.
    // Throw an exception if you try to meet yourself.
    // We are allowed to assume we didn't meet this person yet.
    public void meet(Person otherPerson) {
        if (otherPerson == this)
            throw new RuntimeException("You can't meet yourself");

        friends.enqueue(otherPerson);      // remember this friend
        otherPerson.friends.enqueue(this); // reciprocate
    }

    // Are these two people friends?
    // Throw an exception if you ask about knowing yourself.
    public boolean knows(Person otherPerson) {
        if (otherPerson == this)
            throw new RuntimeException("You can't call knows() on yourself");

        // Search through all my friends
        for (Person p : friends) {
            if (p == otherPerson)
                return true;
        }

        // If otherPerson was not found, I don't know them
        return false;
    }

    // Post a message to my list and the lists of all my friends
    public void post(String message) {
        wall.push(message);       // add to my own list

        for (Person p : friends)
            p.wall.push(message); // and to each friend's
    }

    // Print a header, then all messages this Person can read, newest first
    public void listMessages() {
        // header
        StdOut.println("== The wall of " + name + " ==");

        // Iterate through all messages and print them
        for (String s : wall)
            StdOut.println(s);
    }
]\ 
}
"""

tests = r"""
saveAs = "first";
testConstructor("Kim");
saveAs = "second";
testConstructor("Pat");
testOn("first", "knows", var("second"));
testOn("first", "meet", var("second"));
testOn("first", "knows", var("second"));
testOn("second", "knows", var("first"));
expectException = true;
testOn("first", "knows", var("first"));

saveAs = "first";
testConstructor("Kim");
saveAs = "second";
testConstructor("Pat");
testOn("first", "post", "Only Kim can read this");
testOn("first", "meet", var("second"));
testOn("second", "post", "Friends are awesome");
testOn("first", "post", "I agree");
testOn("first", "listMessages");
testOn("second", "listMessages");

saveAs = "testPerson";
testConstructor("Jack");
expectException = true;
testOn("testPerson", "meet", var("testPerson"));

String samename = "Different people with the same name";
saveAs = "a"; testConstructor(samename); 
saveAs = "b"; testConstructor(samename); 
saveAs = "c"; testConstructor(samename); 
saveAs = "d"; testConstructor(samename); 
testOn("a", "meet", var("b"));
testOn("b", "meet", var("c"));
testOn("a", "post", "a posts this");
testOn("b", "post", "b posts this");
testOn("c", "post", "c posts this");
testOn("d", "post", "d posts this");
testOn("a", "listMessages");
testOn("b", "listMessages");
testOn("c", "listMessages");
testOn("d", "listMessages");
"""
