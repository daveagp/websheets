description = r"""
<i>COS 126 Fall 2013 Programming Midterm 2, part 1/2</i><br>
Please see the problem description in <a href="http://www.cs.princeton.edu/courses/archive/spring14/cos126/docs/mid2-f13-prog.pdf">
this PDF link</a>. 
<p>
This websheet is intended as a practice exam. However, in a real exam,
<ul>
<li>You'll upload via Dropbox
<li>You'll get limited feedback from Dropbox during the exam, and a different full set of test cases for grading
<li>Real humans will grade your real exams and also mark you on style and apply partial credit where appropriate
<li>We recommend coding in DrJava and/or the command-line and doing basic tests on your own before using automatic tests
</ul>
We recommend doing this practice in a timed environment; give yourself 90 minutes.
"""

source_code = r"""
\[
/**************************************************************************
  * MiniPro: Interpreter for a miniature programming language.
  * 
  * COS 126, Princeton University, Fall 2013, Programming Midterm 2 Part 1
  * 
  * Dependencies: ST, StdOut
  * 
  * Compilation: javac-introcs MiniPro.java
  * 
  * Execution:
  * % java-introcs MiniPro
  * false
  * 0
  * currently x is 13
  * 39
  * 13
  * true
  **************************************************************************/
    private int pc;                       // the program counter
    private String[][] program;           // the program itself
    private ST<String, Integer> varTable; // values of all defined variables
    
    // Create interpreter for this program. Don't execute it yet!
    public MiniPro(String[][] program) {
        this.program = program;
        pc = 0; // line 0 is always the first to execute
        varTable = new ST<String, Integer>();
    }

    // Return the current value of the variable named v. If no
    // such variable is currently defined, throw a RuntimeException.
    public int valueOf(String v) {
        if (!varTable.contains(v))
            throw new RuntimeException("Variable named " + v + " not defined");
        return varTable.get(v);
    }

    // Return the number of the line that will execute next.
    public int programCounter() {
        return pc;
    }

    // Execute the line whose number equals the value of the
    // program counter. Then, increment the program counter.
    public void step() {
        String[] line = program[pc]; // current line (1d piece of 2d array)
        String command = line[1]; 

        // assignment statement
        if (command.equals("=")) {
            // look at token on right-hand side, evaluate it
            String rhsToken = line[2];
            int rhsValue;
            
            if (rhsToken.matches("[a-z]+"))       // it's a variable name
                rhsValue = varTable.get(rhsToken);
            else                                  // it's an integer
                rhsValue = Integer.parseInt(rhsToken);
            
            // save value in variable
            varTable.put(line[0], rhsValue);
        }
        
        // println statement
        else if (command.equals("println")) {
            // get value of desired variable, then print it
            int value = varTable.get(line[0]);
            StdOut.println(value);
        }
        
        // increment the program counter
        pc++;
    }

    // Is the program done?
    public boolean isDone() {
        return pc == program.length;
    }
]\
\hide[
public static void MPRun_main() {

   // read all input into lines; handle Windows newlines & extra space
   String[] allLines = StdIn.readAll().trim().split("\\s*\\n");

   // two-dimensional array to hold program
   String[][] program = new String[allLines.length][];

   // break each line into tokens
   for (int i=0; i<allLines.length; i++)
      program[i] = allLines[i].split(" ");
      
   // construct intepreter
   MiniPro mp = new MiniPro(program);

   // execute the program
   int steps = 0;
   while (!mp.isDone()) {
      mp.step();
      steps++;
      if (steps > 500) throw new Error("MPRun ran this MiniPro instance for 500 step()s, halting!\nCheck for infinite looping behavior.");
   }
}                                                                                                                        
]\
"""

tests = r"""
saveAs = "mp";
testConstructor((Object)new String[][]
            {{"x", "=", "13"},     // line 0
            {"y", "=", "x"},      // line 1
            {"x", "=", "39"},     // line 2
            {"x", "println"},     // line 3
            {"y", "println"}});    // line 4
testOn("mp", "isDone");
testOn("mp", "programCounter");
testOn("mp", "step");
testOn("mp", "valueOf", "x");
testOn("mp", "step");
testOn("mp", "step");
testOn("mp", "step");
testOn("mp", "isDone");

saveAs = "mpThrow";
testConstructor((Object)new String[][]
            {{"one", "=", "1"}});     // line 0
testOn("mpThrow", "programCounter");
expectException = true;
testOn("mpThrow", "valueOf", "one");

title = "Running <tt>java-introcs MPRun </tt>";
stdinURL = "http://www.cs.princeton.edu/courses/archive/spring14/cos126/docs/data/MiniPro/sample.txt";
test("MPRun_main");

title = "Running <tt>java-introcs MPRun </tt>";
stdinURL = "http://www.cs.princeton.edu/courses/archive/spring14/cos126/docs/data/MiniPro/swap.txt";
test("MPRun_main");

String program = "a = 1\nb = 2\nc = 3\ntmp = a\na = b\nb = c\nc = tmp\na println\nb println\nc println";
String[] lines = program.split("\\n");
String[][] p1 = new String[lines.length][];
for (int i=0; i<lines.length; i++) p1[i] = lines[i].split(" ");
                                
saveAs = "mp3";
testConstructor((Object)p1);
testOn("mp3", "programCounter");
testOn("mp3", "programCounter");
testOn("mp3", "isDone");
expectException = true;
testOn("mp3", "valueOf", "a");
expectException = true;
testOn("mp3", "valueOf", "b");
expectException = true;
testOn("mp3", "valueOf", "c");
testOn("mp3", "step");
testOn("mp3", "valueOf", "a");
testOn("mp3", "step");
testOn("mp3", "step");
testOn("mp3", "programCounter");
testOn("mp3", "isDone");
testOn("mp3", "valueOf", "a");
testOn("mp3", "valueOf", "b");
testOn("mp3", "valueOf", "c");
testOn("mp3", "step");
testOn("mp3", "step");
testOn("mp3", "step");
testOn("mp3", "step");
testOn("mp3", "programCounter");
testOn("mp3", "isDone");
testOn("mp3", "valueOf", "a");
testOn("mp3", "valueOf", "b");
testOn("mp3", "valueOf", "c");        
"""
