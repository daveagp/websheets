package websheets;
import java.util.*;
import java.lang.reflect.*;
import java.io.*;
import stdlibpack.*;
import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;
import javax.json.*;

import static websheets.Utils.*;

public abstract class Grader extends Options {

    // the API methods
    protected NamedObject var(String name) {
        return new NamedObject(name);
    }

    protected void remark(String S) {
        graderOut.println("<div class='testcase-desc'>"+S+"</div>");
    }

    protected void store(Object val) {
        BasicTestCase btc = new BasicTestCase("", new Object[]{val}, "");
        btc.justStore = true;
        btc.execute(); // print and save, but won't run any code
    }

    protected void test(String methodName, Object... args) {
        new BasicTestCase(methodName, args, methodName).execute();
    }

    protected void testConstructor(Object... args) {
        new BasicTestCase(className, args, "new " + className) {void test() {testConstructor();}}.execute();
    }

    protected void construct(String packaje, final String className, final String typeParams, Object... args) {
        new BasicTestCase(packaje, className, args, "new " + className + typeParams) {void test() {
            Class stuClazz, refClazz;
            try {
                if (packaje == null) {
                    Class[] classes = setup(className);
                    refClazz = classes[0];
                    stuClazz = classes[1];
                }
                else {
                    stuClazz = Class.forName(packaje+"."+className);
                    refClazz = stuClazz;
                }
            }
            catch (Throwable t) {
                throw new RuntimeException("Internal error finding class "+(packaje==null?"":(packaje+"."))+className);
            }
            testConstructor(refClazz, stuClazz);
        }}.execute();
    }

    protected void testOn(final String thisName, String methodName, Object... args) {
        new BasicTestCase(methodName, args, thisName+"."+methodName, thisName).execute();
    }

    // mainArgs is final just so we can inherit in-line
    protected void testMain(final Object... argObjs) {
        testNamedMain("main", className, argObjs);
    }

    protected void testNamedMain(String realNameOfMain, final String fakeNameOfClass, final Object... argObjs) {
	final String[] argStrings = new String[argObjs.length];
	for (int i=0; i<argStrings.length; i++)
	    argStrings[i] = argObjs[i].toString();
        new BasicTestCase(realNameOfMain, new Object[] {argStrings}, "main") {
            void describe() {

                if (title != null) {
                    graderOut.print(title);
                }
                else {
                    graderOut.print("Testing "); // can't be saved as an object
                    String tmp = "java " + fakeNameOfClass;
                    for (String a : argStrings) tmp += " " + a;
                    tmp = code(tmp);
                    graderOut.print(tmp);
                }

                if (stdinURL != null) {
                    String[] urlSplit = stdinURL.split("/");
                    graderOut.println("<code> &lt; <a target=\"_blank\" href=\""+stdinURL+"\">"+urlSplit[urlSplit.length-1]+"</a></code>");
                    //stdin = new In(stdinURL).readAll();
                    stdin = testerStdin.getJsonObject("fetched_urls").
                        getString(stdinURL);
                }
                describeStdin();
            }}
            .execute();
    }

    protected Random randgen = new Random();

    // public so that template code can access it
    public static class FailException extends RuntimeException {
        public FailException(String msg) {
            super(msg);
        }
    }
    
    // end of API

    // instance variables

    protected String className; // descendants should define this in constructor
    PrintStream graderOut = new PrintStream(new FileOutputStream(FileDescriptor.out));
    ByteArrayOutputStream gbaos = null;
    JsonObject testerStdin;
    Class<?> studentC, referenceC;    
    InputStream orig_stdin = System.in;
    PrintStream orig_stdout = System.out;
    ByteArrayOutputStream baos;
    TreeMap<String,Object> studentObjects = new TreeMap<>();
    TreeMap<String,Object> referenceObjects = new TreeMap<>();

    // exception-related classes for internal use

    static class FailTestException extends RuntimeException {
        FailTestException(String msg) {
            super(msg);
        }
    }
    
    static class TooMuchOutputException extends RuntimeException {
    }
    
    // the rest of this file is
    // methods and inner classes used to implement grading infrastructure
    
    class BasicTestCase {
        String methodName;
        Object[] args;
        String apparentName;
        String thisName;
        String packaje;
        boolean justStore = false;

        BasicTestCase(String methodName, Object[] args) {
            this(methodName, args, methodName, null);
        }
        BasicTestCase(String methodName, Object[] args, String apparentName) {
            this(methodName, args, apparentName, null);
        }
        BasicTestCase(String methodName, Object[] args, String apparentName, String thisName) {
            this(null, methodName, args, apparentName, thisName);
        }
        BasicTestCase(String packaje, String methodName, Object[] args, String apparentName) {
            this(packaje, methodName, args, apparentName, null);
        }
        BasicTestCase(String packaje, String methodName, Object[] args, String apparentName, String thisName) {
            this.methodName = methodName;
            this.args = args;
            this.packaje = packaje;
            this.thisName = thisName;
            this.apparentName = apparentName;
        }
        void describe() {
            if (title != null) {
                graderOut.print(title);
            }
            else {
                String tmp = "";
                if (saveAs == null) {
                    graderOut.print("Calling ");
                }
                else {
                    graderOut.print("Defining ");
                    tmp = saveAs + " = ";
                }
                if (justStore) {
                    tmp += repr(args[0]);
                }
                else {
                    tmp += apparentName + "(";
                    if (args.length == 0) tmp += ")";
                    else {
                        tmp += repr(args[0]);
                        for (int i=1; i<args.length; i++)
                            tmp += ", " + repr(args[i]);
                        tmp += ")";
                    }
                }
                graderOut.println(code(tmp));
            }
            if (stdinURL != null) {
                String[] urlSplit = stdinURL.split("/");
                graderOut.println("<code> &lt; <a target=\"_blank\" href=\""+stdinURL+"\">"+urlSplit[urlSplit.length-1]+"</a></code>");                
                //stdin = new In(stdinURL).readAll();
                stdin = testerStdin.getJsonObject("fetched_urls").
                    getString(stdinURL);
            }
	    describeStdin();
        }
	void describeStdin() {
            // don't show when "java Foo < input.txt" form is used
	    if (stdin != null && stdinURL == null) {
		graderOut.println(" with standard input"+pre(stdin));
	    }
	}

        void test() {
            test(referenceC, studentC);
        }

        void test(Class clazz) {
            test(clazz, clazz);
        }

        void test(Class refClazz, Class stuClazz) {
            boolean notfound = true;
            tryMethods: for (Method m : refClazz.getMethods())
                if (m.getName().equals(methodName)) {
                    Class[] formalParms = m.getParameterTypes();
                    //System.out.println(java.util.Arrays.toString(formalParms));
                    //System.out.println(java.util.Arrays.toString(args));
                    if (formalParms.length != args.length) continue;
                    for (int i=0; i<args.length; i++) {
                        Object arg = args[i];
                        if (arg instanceof NamedObject) arg = ((NamedObject)arg).value(true); // convert to ref obj to look at class
                        if (formalParms[i] == int.class && arg.getClass() == Integer.class) continue; // ok
                        if (formalParms[i] == double.class && arg.getClass() == Double.class) continue; // ok
                        if (!formalParms[i].isAssignableFrom(arg.getClass())) continue tryMethods;
                    }

                    notfound = false;
                    String argTypes = classListToString(m.getParameterTypes());
                    try {
                        Method referenceM = m;
                        Class[] stuParamTypes = m.getParameterTypes();
                        for (int i=0; i<stuParamTypes.length; i++) {
                            if (stuParamTypes[i] == referenceC)
                                stuParamTypes[i] = studentC;
                            else if (stuParamTypes[i].getName().startsWith("reference."))
                                stuParamTypes[i] = setup(stuParamTypes[i].getSimpleName())[1];
                        }
                        Method studentM = stuClazz.getMethod(methodName, stuParamTypes);
                        Class expectedReturn = referenceM.getReturnType();
                        if (expectedReturn == referenceC) expectedReturn = studentC;
                        else if (expectedReturn.getName().startsWith("reference."))
                            {
     expectedReturn = setup(expectedReturn.getSimpleName())[1];                                                }    
                        if (! studentM.getReturnType().equals(expectedReturn)) {
                            throw new FailTestException("Your method " + code(methodName +argTypes) + " should have return type " + code(classToString(referenceM.getReturnType())));
                        }
                        if (referenceM.getModifiers() != studentM.getModifiers()) {
                            throw new FailTestException("Incorrect declaration for " + code(methodName + "("+argTypes+")") + "; check use of " + code("public") + " and " + code("static") + " or other modifiers");
                        }
                        compare(m, studentM, args, thisName);
                    }
                    catch (NoSuchMethodException e) {
                        throw new FailTestException("You need to declare a method " + code(methodName) + " that accepts arguments" + code(argTypes));
                    }
                }            
            if (notfound) 
                throw new RuntimeException("Could not find the reference method "+ code(methodName)+"! Check that floating-point numbers are explicitly specified.");
        }

        void testConstructor() {
            testConstructor(referenceC, studentC);
        }
        void testConstructor(Class clazz) {
            testConstructor(clazz, clazz);
        }
        void testConstructor(Class refClass, Class stuClass) {
            boolean notfound = true;
            tryMethods: for (Constructor m : refClass.getConstructors()) {
                Class[] formalParms = m.getParameterTypes();
                if (formalParms.length != args.length) continue;
                checkParms: for (int i=0; i<args.length; i++) {
                    Object arg = args[i];
                    if (arg instanceof NamedObject) arg = ((NamedObject)arg).value(true); // convert to ref obj to look at class
                    if (formalParms[i] == int.class && arg.getClass() == Integer.class) continue checkParms;
                    if (formalParms[i] == double.class && arg.getClass() == Double.class) continue checkParms;
                    if (!formalParms[i].isAssignableFrom(arg.getClass())) continue tryMethods;
                }
                notfound = false;
                String argTypes = classListToString(m.getParameterTypes());
                try {
                    Constructor referenceM = m;
                    Constructor studentM = stuClass.getConstructor(m.getParameterTypes());
                    if (referenceM.getModifiers() != studentM.getModifiers()) {
                        throw new FailTestException("Incorrect declaration for " + code(className+"("+argTypes+")") + " constructor; check use of " + code("public") + " and " + code("static") + " or other modifiers");
                    }

                    compare(m, studentM, args, null);                    
                }
                catch (NoSuchMethodException e) {
                    throw new FailTestException("You need to declare a constructor for " + code(className) + " that accepts arguments" + code(argTypes));
                }
            }
            if (notfound) throw new RuntimeException("Could not find the reference constructor! Check that floating-point numbers are explicitly specified.");
        }



        void execute() {
            ((Options)(Grader.this)).fillWithDefaults();
            if (quietOnPass) {
                gbaos = new ByteArrayOutputStream();
                graderOut = new PrintStream(gbaos);
            }
            boolean showHellip = stdin == null;
            graderOut.println("<div class='testcase-desc'>");
            describe();
            
            if (showHellip) graderOut.println("&hellip;");
            graderOut.println("</div>");
            if (justStore) {
                studentObjects.put(saveAs, cloneForStudent ? semicopy(args[0]) : args[0]);
                referenceObjects.put(saveAs, cloneForReference ? semicopy(args[0]) : args[0]);
            }
            else if (thisName != null) {
                // calling instance method on student code
                if (studentObjects.get(thisName).getClass() == studentC) {
                    test();
                }
                // calling instance method in student code from another class
                else if (studentObjects.get(thisName).getClass().getName().startsWith("student.")) {
                    Class[] c = setup(studentObjects.get(thisName).getClass().getSimpleName());
                    test(c[0], c[1]);
                }
                else // calling on a built-in or stdlibpack
                    test(studentObjects.get(thisName).getClass());
            }
            else
                test();
            if (quietOnPass) {
                graderOut = new PrintStream(new FileOutputStream(FileDescriptor.out));//orig_graderOut;
                try {
                    String content = gbaos.toString("UTF-8");
                    if (content.indexOf("class='pass-test'")<0)
                        graderOut.print(content);
                }
                catch (UnsupportedEncodingException e) {
                    throw new RuntimeException(e.toString());
                }                
            }
            ((Options)(Grader.this)).clear();
        }
    }

    // END of basicTestCase

    // descendants must override this
    abstract protected void runTests();

    void startStdoutCapture() {
        baos = new ByteArrayOutputStream() {
                public void write(byte[] b, int off, int len) {
                    super.write(b, off, len);
                    if (size() > maxOutputBytes) throw new TooMuchOutputException();
                }
            };
        System.setOut(new PrintStream(baos));
	StdOut.resync();
    }

    String endStdoutCapture() {
        try {
            String content = baos.toString("UTF-8");
            System.setOut(orig_stdout);
	    StdOut.resync();
            return content;
        }
        catch (UnsupportedEncodingException e) {
            throw new RuntimeException(e.toString());
        }
    }

    class NamedObject {
	final String name;
	NamedObject(String S) {name = S;}
        Object value(boolean reference) {
            return (reference?referenceObjects:studentObjects).get(name);
        }
        public String toString() {return name;}
    }

    // are they different? return null if not, html description if so
    String describeOutputDifference(String stu, String ref) {
        String[] stulines = stu.split("\n", -1);
        String[] reflines = ref.split("\n", -1);
        int samelines = 0;
        while (samelines < Math.min(stulines.length, reflines.length)
               && equalsApprox(rtrimConditional(stulines[samelines], Grader.this),
                               rtrimConditional(reflines[samelines], Grader.this),
                               Grader.this))
            samelines++;

        // were they the same?
        if (samelines == stulines.length && samelines == reflines.length)
            return null; // yup!

        // two special cases
        if (samelines == stulines.length - 1 && samelines == reflines.length
            && rtrimConditional(stulines[stulines.length - 1], Grader.this).equals(""))
            return "Your program printed this output:" + pre(stu)
                + " which is almost correct but <i>an extra newline character was printed at the end</i>.";

        if (samelines == reflines.length - 1 && samelines == stulines.length
            && rtrimConditional(reflines[reflines.length - 1], Grader.this).equals(""))
            return "Your program printed this output:" + pre(stu)
                + " which is almost correct but <i>a newline character is missing at the end</i>.";
        
        // general case
        final int samelines2 = samelines; // woo java 8!
        final StringBuilder sb = new StringBuilder();

        class DescriptionLoop {
            void handle(String[] lines) {
                if (lines.length == 1) { 
                    if (lines[0].equals(""))
                        sb.append("<pre><i>(no output)</i></pre>");
                    else
                        sb.append("<pre>"+esc(lines[0])+"</pre>");
                    return;
                }
                sb.append("<pre><span class='before-diff-line'>");
                for (int i=0; i<lines.length; i++) {
                    if (i==samelines2) sb.append("</span><span class='diff-line'>");
                    sb.append(esc(lines[i]));
                    if (i==samelines2) sb.append("</span><span class='after-diff-line'>");
                    if (i != lines.length-1 || lines.length == 1) 
                        sb.append("<br>"); // wasn't student output for i==length-1, but add it to fix pre appearance
                }
                sb.append("</span></pre>");
            }
        };
        DescriptionLoop dl = new DescriptionLoop();

        boolean stured = samelines < stulines.length - 1
            || samelines == stulines.length - 1 && !rtrim(stulines[stulines.length-1]).equals("");
        boolean refred = samelines < reflines.length - 1
            || samelines == reflines.length - 1 && !rtrim(reflines[reflines.length-1]).equals("");
        
        sb.append("Your program printed this output" + 
                  (stured ? " (first difference in red)" : "")
                  + ":");
        dl.handle(stulines);
        sb.append("It was supposed to print this output" + 
                  ((samelines < reflines.length) ? " (first difference in red)" : "")
                  + ":");
        dl.handle(reflines);
        return sb.toString();
    }
    
    abstract class Capturer {
        String stdout;
        boolean crashed;
        boolean notdone = false;
        Set<Thread> oldThreadSet;

        Capturer() {
            startStdoutCapture();
            oldThreadSet = Thread.getAllStackTraces().keySet();
        }
        void end() {
            stdout = endStdoutCapture();
        }
        boolean threadsLeftOver() {
            for (Thread t : Thread.getAllStackTraces().keySet())
                if (!oldThreadSet.contains(t)) return true;
            return false;
        }

        Object retval; // not used by class initializer; used by invoke and construct

        abstract void run_command() throws IllegalAccessException, InvocationTargetException,
                                           InstantiationException, ClassNotFoundException;

        void runUserCode() throws IllegalAccessException, InvocationTargetException,
                                  InstantiationException, ClassNotFoundException {
            try {
                run_command();
                crashed = false;
            }
            finally {
                if (threadsLeftOver())
                    notdone = true;
                else
                    end();
            }
        }
    }

    class InvokeCapturer extends Capturer {
        Method m;
        Object dis;
        Object[] args;
        InvokeCapturer(Method m, Object dis, Object[] args) {
            super();
            this.m=m; this.dis=dis; this.args=args;
            crashed = true;
        }
        void run_command() throws IllegalAccessException, InvocationTargetException {
            retval = m.invoke(dis, args);
        }
    }
    
    class ConstructCapturer extends Capturer {
        Constructor c;
        Object[] args;
        ConstructCapturer(Constructor c, Object[] args) {
            super();
            this.c=c; this.args=args;
            crashed = true;
        }
        void run_command() throws IllegalAccessException, InvocationTargetException, InstantiationException {
            //graderOut.println(c);
            //graderOut.println(repr(args));
            retval = c.newInstance(args);
        }
    }

    class ClassInitCapturer extends Capturer {
        Class foundClass;
        String className;
        ClassInitCapturer(String className) {
            super();
            this.className = className;
            crashed = true;
        }
        void run_command() throws IllegalAccessException, ClassNotFoundException {
            foundClass = Class.forName(className);
        }
    }

    Object[] lookupNamedObjects(Object[] args, TreeMap<String, Object> dict) {
        Object[] result = new Object[args.length];
        for (int i=0; i<args.length; i++)
            if (args[i] instanceof NamedObject)
                result[i] = dict.get(((NamedObject)args[i]).name);
            else
                result[i] = args[i];
        return result;
    }

    // only works for non-nested arrays so far
    String checkForArgMutations(Object[] orig, Object[] ref, Object[] stu) {
        String commentary = "";
        int n = orig.length;
        for (int i=0; i<n; i++) {
            if (orig[i].getClass().isArray()) {
                int len = Array.getLength(orig[i]);
                for (int j=0; j<len; j++) {
                    Object oj = Array.get(orig[i], j);
                    Object rj = Array.get(ref[i], j);
                    Object sj = Array.get(stu[i], j);
                    boolean correct = smartEquals(sj, rj, (Options)this);
                    boolean refChanged = !smartEquals(oj, rj, (Options)this);
                    boolean stuChanged = !smartEquals(sj, oj, (Options)this);
                    if (refChanged && correct)
                        commentary += "<p>Changed element "+code(j)+" of arg "+code(i)+" from " + code(repr(oj)) + " to "+code(repr(rj))+" as expected.";
                    else if (refChanged && !stuChanged)
                        throw new FailTestException
                            ("Missing side-effect, your code was supposed to change element "+code(j)+" of arg "+code(i)+" from " + code(repr(oj))+" to "+code(repr(rj)));
                    else if (refChanged)
                        throw new FailTestException
                            ("Wrong side-effect, your code changed element "+code(j)+" of arg "+code(i)+" from " + code(repr(oj))+" to "+code(repr(sj))
                             + ", was expected to change to " + code(repr(rj)));
                   if (!refChanged && stuChanged)
                        throw new FailTestException
                            ("Unexpected side-effect, your code changed element "+code(j)+" of arg "+code(i)+" from " + code(repr(oj))+" to "+code(repr(sj)));
                }
            }
        }
        return commentary;
    }

    // the arguments can either be two Methods or two Constructors
    @SuppressWarnings("unchecked")
    void compare(AccessibleObject referenceM, AccessibleObject studentM, Object[] args, String thisName) {
        boolean methods = referenceM instanceof Method;
        boolean constructors = referenceM instanceof Constructor;

        Capturer ref = null, stu = null;
        Object[] argsPassedToRef = lookupNamedObjects(args, referenceObjects);
        if (cloneForReference) argsPassedToRef = (Object[]) semicopy(argsPassedToRef);
        Object[] argsPassedToStu = lookupNamedObjects(args, studentObjects);
        if (cloneForStudent) argsPassedToStu = (Object[]) semicopy(argsPassedToStu);
        Throwable referenceException = null;
        Throwable studentException = null;
	if (stdin != null)
	    StdIn.setString(stdin);

        try {
            if (!dontRunReference) {
                if (methods) {
                    //if (thisName != null) System.out.println(thisName+" "+referenceObjects.get(thisName));
                    ref = new InvokeCapturer((Method)referenceM, thisName==null?null:referenceObjects.get(thisName), argsPassedToRef);
                    ((InvokeCapturer)ref).runUserCode();
                }
                else { // constructors
                    ref = new ConstructCapturer((Constructor)referenceM, argsPassedToRef);
                    ((ConstructCapturer)ref).runUserCode();
                }
            }
            if (expectException) 
                throw new RuntimeException("Internal error: bad exception flag");
            if (!dontRunReference && ref.notdone) {
                while (ref.threadsLeftOver()) 
                    Thread.yield();
                ref.end();
            }
        }
        catch (ClassNotFoundException e) {
            throw new RuntimeException("Internal error: CNFE");
        }
        catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            if (e instanceof InvocationTargetException && expectException) {
                referenceException = ((InvocationTargetException)e).getTargetException();
            }
            else {
                Throwable ex = e;
                if (e instanceof InvocationTargetException) {
                    ex = ((InvocationTargetException)e).getTargetException();
                    ex.printStackTrace();
                }
                e.printStackTrace();
                throw new RuntimeException("Internal error: " + ex.toString() + "<br>Partial output:" + ((ref != null && ref.stdout != null) ? pre(ref.stdout) : ""));                
            }
        }
        
        
        if (stdin != null)
            StdIn.setString(stdin);
        try {
            if (methods) {                
                stu = new InvokeCapturer((Method)studentM, thisName==null?null:studentObjects.get(thisName), argsPassedToStu);
                ((InvokeCapturer)stu).runUserCode();
            }
            else { // constructors
                stu = new ConstructCapturer((Constructor)studentM, argsPassedToStu);
                ((ConstructCapturer)stu).runUserCode();
            }
            if (expectException) throw new FailTestException("Was supposed to throw a " + referenceException.getClass().getSimpleName() + " but did not.");
            if (stu.notdone) {
                graderOut.println("<div class='no-bottom-line'>Some new threads were spawned. Waiting until they all finish&hellip;</div>");
                while (stu.threadsLeftOver()) 
                    Thread.yield();
                graderOut.println("<div class='no-top-line'>&hellip;all terminated ok.</div>");
                stu.end();
            }
        }
        catch (ClassNotFoundException e) {
            throw new RuntimeException("Internal error: CNFE");
        }
        catch (IllegalAccessException e) {
            throw new RuntimeException("Internal error: " + e.toString() + "<br>Partial output:" + pre(stu.stdout));
        }
        catch (InstantiationException e) {
            throw new FailTestException("Error: " + className + " must not be abstract.");
        }
        catch (InvocationTargetException e) {
            if (stu.notdone) {
                stu.end(); // crashed, so leftover threads may not be worth waiting for
                graderOut.println("<div class='no-top-line no-bottom-line'>Warning: leftover threads after crash may cause extra output below.</div>");
            }
            studentException = e.getTargetException();
            
            if (studentException instanceof TooMuchOutputException) {
                graderOut.println("<div>Printed too much output:" + pre(stu.stdout) + "</div>");
                throw new FailTestException("Did not pass due to output overflow.");
            }
            if (studentException instanceof FailException) {
                System.out.println("<div>Your program printed this output: " + pre(stu.stdout) + "</div>");
                throw new FailTestException("Failed: "+code(studentException.getMessage()));
            }
            
            if (referenceException != null && referenceException.getClass() == studentException.getClass()) {
                // passed!
            }
            else {
                String stackTrace = studentException.toString();
                boolean first = true;
                for (StackTraceElement ste : studentException.getStackTrace()) {
                    if (ste.getClassName().equals("student."+className)) {
                        stackTrace += "\n   "+(first?"at":"called from")+" line " + ste.getLineNumber() + " in " + ste.getMethodName() + "()";
                        first = false;
                    }
                }
                String msg = "Runtime error:";
                if (referenceException != null) // expected an exception, but not this kind.
                    msg = "An unexpected error was thrown: expected a "+code(referenceException.getClass().getSimpleName())+" but got a "
                        +code(studentException.getClass().getSimpleName()+":");
                throw new FailTestException(msg
                                            + 
                                            pre(stackTrace) 
                                            + 
                                            (stu == null || stu.stdout == null || stu.stdout.equals("") ? "" : "Partial printed output:" + pre(stu.stdout)));
            }
        }
        
        
        if (!dontRunReference && ref.stdout.length() > 0) {
            String reason = describeOutputDifference(stu.stdout, ref.stdout);
            if (reason != null)
                throw new FailTestException(reason);
            
        }
        if (!dontRunReference && ref.stdout.equals("") && !stu.stdout.equals("")) {
            throw new FailTestException("Found this printed output when none was expected:" + pre(stu.stdout));
        }
        if (dontRunReference && stu.stdout.length() > 0) {
            graderOut.println("<div class='output'>Printed this output:"+pre(stu.stdout)+"</div>");
        }
        if (methods && !expectException && ((Method)referenceM).getReturnType() != Void.TYPE
            && ((Method)referenceM).getReturnType() != referenceC
            && (!((Method)referenceM).getReturnType().getName().startsWith("reference."))) {
            if (!smartEquals(stu.retval, ref.retval, (Options)Grader.this)) {
                throw new FailTestException("Expected return value " + code(repr(ref.retval)) + " but instead your code returned " + code(repr(stu.retval)));
            }
        }

        if (saveAs != null) {
            studentObjects.put(saveAs, stu.retval);
            referenceObjects.put(saveAs, ref.retval);
        }
        
        String mutationCommentary = checkForArgMutations(args, argsPassedToRef, argsPassedToStu);
        
        String goodStuff = "";
        if (!dontRunReference && !ref.stdout.equals("")) {
            goodStuff += "Printed correct output " + pre(stu.stdout) + "\n";
        }
        if (methods && !expectException && ((Method)referenceM).getReturnType() != Void.TYPE
            && ((Method)referenceM).getReturnType() != referenceC
            && (!((Method)referenceM).getReturnType().getName().startsWith("reference."))
            && (!opaque(stu.retval))) {
            goodStuff += "Returned correct value " + pre(repr(stu.retval)) + "\n";
        }
        if (expectException) {
            goodStuff += "Threw a "+code(referenceException.getClass().getSimpleName())+" as required!";
        }
        goodStuff += mutationCommentary;
        if (!goodStuff.equals("")) {
            graderOut.print("<div class='pass-test'>");
            graderOut.print("Passed test!\n"+goodStuff);
            graderOut.println("</div>");
        }
    }

    Class[] setup() {
        return setup(className);
    }
    
    // return the reference class and the student class with this name
    Class[] setup(String whichClass) {
        try {
            ClassInitCapturer stu = new ClassInitCapturer("student."+whichClass);
            stu.runUserCode();
            ClassInitCapturer ref = new ClassInitCapturer("reference."+whichClass);
            ref.runUserCode();
            if (whichClass == className) {
                studentC = stu.foundClass;
                referenceC = ref.foundClass;
            }

            if (stu.stdout.length() > 0) {
                graderOut.println("<div>Warning: your class printed the output "+pre(stu.stdout)+" before any method was called.</div>");
            }
            return new Class[]{ref.foundClass, stu.foundClass};
        }
        catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            throw new RuntimeException("Internal error: IAE|ITE|IE");
        }
        catch (ClassNotFoundException e) {
            throw new RuntimeException("Internal error: class not found " + e);
        }
    }

    protected void genericMain(String[] args) {
        JsonReader jr = Json.createReader(System.in);
        testerStdin = jr.readObject();
        jr.close();

        //System.out.println(testerStdin.toString());

        // quit with code -1 after 5 seconds
        Timer timer = new Timer();
        timer.schedule(new TimerTask() { public void run() {System.err.println("Time Limit Exceeded"); System.exit(-1);}},
                       new Date(System.currentTimeMillis()+5*1000));

        setup();
        Error throw_e = null;
        RuntimeException throw_rte = null;
        try {
            try {
                runTests();
                System.out.println("<div class='all-passed'>All tests passed!</div>");
            }
            catch (FailTestException e) {
                if (quietOnPass) {
                    graderOut = new PrintStream(new FileOutputStream(FileDescriptor.out));
                    try {
                        String content = gbaos.toString("UTF-8");
                        if (content.indexOf("class='pass-test'")<0)
                            graderOut.print(content);
                    }
                    catch (UnsupportedEncodingException ex) {
                        throw new RuntimeException(ex.toString());
                    }                
                }
                System.out.println("<div class='error'>"+e.getMessage()+"</div>");
                System.out.println("<div class='not-all-passed'>Did not pass all tests.</div>");
            }
            timer.cancel();
            timer.purge();
        }
        // now, any usercode errors should already have been caught.
        // but this is to make sure internally generated errors are handled sanely
        catch (Error | RuntimeException t) { // throwable == catchable
            // don't hang forever
            timer.cancel();
            timer.purge();
            if (t instanceof Error) throw_e = (Error) t;
            else throw_rte = (RuntimeException) t;
        }
        if (throw_e != null) throw throw_e;
        if (throw_rte != null) throw throw_rte;
    }

}