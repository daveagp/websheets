description = r"""
<i>COS 126 Fall 2013 Programming Midterm 2, part 2/2</i><br>
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
  * MiniPro2: Interpreter for version 2 of a miniature programming language.
  * 
  * COS 126, Princeton University, Fall 2013, Programming Midterm 2 Part 1
  * 
  * Notes: functionally different from MiniPro in step() and isDone();
  * has private helper method evaluate(), not part of API.
  * 
  * Dependencies: ST, StdOut
  * 
  * Compilation: javac-introcs MiniPro.java
  **************************************************************************/
    private int pc;                       // the program counter
    private String[][] program;           // the program itself
    private ST<String, Integer> varTable; // values of all defined variables
    
    // Create interpreter for this program. Don't execute it yet!
    public MiniPro2(String[][] program) {
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
    
    // Check if this token is an integer or variable, and give the value
    // of it in either case.
    private int evaluate(String token) {
        // look at token, evaluate it
        if (token.matches("[a-z]+"))       // it's a variable name
            return varTable.get(token);
        else                               // it's an integer
            return Integer.parseInt(token);
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
            int rhsValue = evaluate(rhsToken);
            
            // save value in variable
            varTable.put(line[0], rhsValue);
        }

        // println statement
        else if (command.equals("println")) {
            // get value of desired variable, then print it
            int value = varTable.get(line[0]);
            StdOut.println(value);
        }

        // mathematical operations
        else if (command.equals("+=")) {
            // which variable are we updating?
            int oldValue = varTable.get(line[0]);

            // what should its new value be?
            int newValue = oldValue + evaluate(line[2]);
            
            // update
            varTable.put(line[0], newValue);
        }
        else if (command.equals("-=")) {
            // which variable are we updating?
            int oldValue = varTable.get(line[0]);

            // what should its new value be?
            int newValue = oldValue - evaluate(line[2]);
            
            // update
            varTable.put(line[0], newValue);
        }
        else if (command.equals("*=")) {
            // which variable are we updating?
            int oldValue = varTable.get(line[0]);

            // what should its new value be?
            int newValue = oldValue * evaluate(line[2]);
            
            // update
            varTable.put(line[0], newValue);
        }

        // jump if positive statement
        else if (command.equals("pos?jump")) {
            // value of variable we are testing
            int testValue = evaluate(line[0]);
            
            if (testValue > 0) { // positive?
                pc += evaluate(line[2]); // jump!
                // return right now so that we don't hit the pc++ line below
                return;
            }
            // else, take no special action
        }
        
        // increment the program counter
        pc++;
    }

    // Is the program done?
    // For MiniPro2, we have to check not only being at the end,
    // but also after the end or before the start.
    public boolean isDone() {
        return pc >= program.length || pc < 0;
    }
]\\hide[
public static void MP2Run_main() {

   // read all input into lines; handle Windows newlines & extra space
   String[] allLines = StdIn.readAll().trim().split("\\s*\\n");

   // two-dimensional array to hold program
   String[][] program = new String[allLines.length][];

   // break each line into tokens
   for (int i=0; i<allLines.length; i++)
      program[i] = allLines[i].split(" ");
      
   // construct intepreter
   MiniPro2 mp = new MiniPro2(program);

   // execute the program
   int steps = 0;
   while (!mp.isDone()) {
      mp.step();
      steps++;
      if (steps > 500) throw new Error("MP2Run ran this MiniPro2 instance for 500 step()s, halting!\nCheck for infinite looping behavior.");
   }
}                                                                                                                        
]\
"""

tests = r"""
HTMLdescription = "Running <tt>java-introcs MP2Run </tt>";
testStdinURL = "http://www.cs.princeton.edu/courses/archive/spring14/cos126/docs/data/MiniPro/math.txt";
test("MP2Run_main");

HTMLdescription = "Running <tt>java-introcs MP2Run </tt>";
testStdinURL = "http://www.cs.princeton.edu/courses/archive/spring14/cos126/docs/data/MiniPro/absL.txt";
test("MP2Run_main");

HTMLdescription = "Running <tt>java-introcs MP2Run </tt>";
testStdinURL = "http://www.cs.princeton.edu/courses/archive/spring14/cos126/docs/data/MiniPro/absR.txt";
test("MP2Run_main");

HTMLdescription = "Running <tt>java-introcs MP2Run </tt>";
testStdinURL = "http://www.cs.princeton.edu/courses/archive/spring14/cos126/docs/data/MiniPro/sum10.txt";
test("MP2Run_main");

HTMLdescription = "Running <tt>java-introcs MP2Run </tt>";
testStdinURL = "http://www.cs.princeton.edu/courses/archive/spring14/cos126/docs/data/MiniPro/gcf.txt";
test("MP2Run_main");

HTMLdescription = "Running <tt>java-introcs MP2Run</tt> ";
testStdin = "x = 2\ny = 3\nx += y\nx println\ny println";
test("MP2Run_main");

HTMLdescription = "Testing += with variable: running <tt>java-introcs MP2Run</tt> ";
testStdin = "x = 2\ny = 3\nx -= y\nx println\ny println";
test("MP2Run_main");

HTMLdescription = "Testing -= with variable: running <tt>java-introcs MP2Run</tt> ";
testStdin = "x = 2\ny = 3\nx *= y\nx println\ny println";
test("MP2Run_main");

HTMLdescription = "Testing *= with variable: running <tt>java-introcs MP2Run</tt> ";
testStdin = "x = 2\ny = 3\nx *= y\nx println\ny println";
test("MP2Run_main");

HTMLdescription = "Testing += with int: running <tt>java-introcs MP2Run</tt> ";
testStdin = "x = 2\nx += 3\nx println";
test("MP2Run_main");

HTMLdescription = "Testing -= with int: running <tt>java-introcs MP2Run</tt> ";
testStdin = "x = 2\nx += 3\nx println";
test("MP2Run_main");

HTMLdescription = "Testing *= with int: running <tt>java-introcs MP2Run</tt> ";
testStdin = "x = 2\nx += 3\nx println";
test("MP2Run_main");

HTMLdescription = "Testing pos?jump with +ve LHS: running <tt>java-introcs MP2Run</tt> ";
testStdin = "x = 2\nx pos?jump 2\nx println\nx println\nx println";
test("MP2Run_main");

HTMLdescription = "Testing pos?jump with 0 LHS: running <tt>java-introcs MP2Run</tt> ";
testStdin = "x = 0\nx pos?jump 2\nx println\nx println\nx println";
test("MP2Run_main");

HTMLdescription = "Testing pos?jump with -ve LHS: running <tt>java-introcs MP2Run</tt> ";
testStdin = "x = -2\nx pos?jump 2\nx println\nx println\nx println";
test("MP2Run_main");

HTMLdescription = "Testing pos?jump with +ve LHS, var RHS: running <tt>java-introcs MP2Run</tt> ";
testStdin = "x = 2\nx pos?jump x\nx println\nx println\nx println";
test("MP2Run_main");

HTMLdescription = "Testing pos?jump to before start: running <tt>java-introcs MP2Run</tt> ";
testStdin = "x = 2\nx pos?jump -126\n100 print";
test("MP2Run_main");

HTMLdescription = "Testing pos?jump to just before start: running <tt>java-introcs MP2Run</tt> ";
testStdin = "x = 2\nx pos?jump -2\n100 print";
test("MP2Run_main");

HTMLdescription = "Testing pos?jump to just after end: running <tt>java-introcs MP2Run</tt> ";
testStdin = "x = 2\nx pos?jump 2\n100 print";
test("MP2Run_main");

HTMLdescription = "Testing pos?jump to after end: running <tt>java-introcs MP2Run</tt> ";
testStdin = "x = 2\nx pos?jump 126\n100 print";
test("MP2Run_main");

"""
