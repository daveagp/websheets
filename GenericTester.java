package framework;
import java.util.*;
import java.util.regex.*;
import java.lang.reflect.*;
import java.io.*;
import stdlibpack.*;
import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;
import javax.json.*;

public abstract class GenericTester {

    public static String classToString(Class<?> clazz) {
        if (clazz.isArray()) return classToString(clazz.getComponentType())+"[]";
        if (clazz.isPrimitive()) return clazz.toString();
        return clazz.getSimpleName();
    }

    public static String classListToString(Class<?>[] classes) {
        String result = "(";
        for (int i=0; i<classes.length; i++) {
            if (i > 0) result += ",";
            result += classToString(classes[i]);
        }
        return result+")";
    }

    public static PrintStream graderOut = new PrintStream(new FileOutputStream(FileDescriptor.out));

    public static PrintStream orig_graderOut = new PrintStream(new FileOutputStream(FileDescriptor.out));


    public static ByteArrayOutputStream gbaos = null;

    /* "library" helper methods and exceptions */

    public static String esc(String S) {
        return 
            S.replaceAll("&", "&amp;").replaceAll(">", "&gt;")
            .replaceAll("<", "&lt;").replaceAll("  ", " &nbsp;");
    }
            
    public static String pre(String S, String attr) {
	String adjust = S.equals("") ? "<br>" : "";
	return "<pre "+attr+">" + adjust + esc(S) + "</pre>";
    }
    public static String pre(String S) {return pre(S, "");}

    public static String code(String S, String attr) {
        if (S==null) return "[NULL]";
        return "<code "+attr+">" + esc(S) + "</code>";
    }
    public static String code(String S) {return code(S, "");}
    public static String code(Object O) {return code(O.toString(), "");}

    public boolean opaque(Object a) {
        if (a==null) return false;
        if (a.getClass() == stdlibpack.Queue.class)
            return true;
        if (a.getClass() == stdlibpack.Stack.class)
            return true;
        return false;
    }

    // student first then reference, where possible
    public boolean smartEquals(Object a, Object b) {
        if ((a == null) != (b == null))
            return false;
        if (a==null && b==null)
            return true;
        if (a.getClass() == stdlibpack.Queue.class) {
            return (b.getClass() == stdlibpack.Queue.class);
        }
        if (a.getClass() == studentC || a.getClass() == referenceC)
            return (b.getClass() == studentC || b.getClass() == referenceC);
        if (a.getClass().isArray() != b.getClass().isArray())
            return false;
        if (a.getClass().isArray()) {
            if (Array.getLength(a) != Array.getLength(b))
                return false;
            for (int i=0; i<Array.getLength(a); i++)
                if (!smartEquals(Array.get(a, i), Array.get(b, i)))
                    return false;
            return true;
        }
        if (a.getClass() == Double.class) {
            return equalsApprox((Double)a, (Double)b);
        } else if (a.getClass() == Float.class) {
            return equalsApprox((Float)a, (Float)b);
        }
        return a.equals(b);
    }

    // only works for int[] so far
    public static String typerepr(Object O) {
	if (O instanceof int[]) return "int[]";
	if (O instanceof String[]) return "String[]";
	return "???";
    }

    public static String repr(Object O) {
        if (O instanceof NamedObject) {
            return ((NamedObject)O).name;
        }
        else if (O instanceof String) {
            return '"' + (String)O + '"';
        }
	else if (O == null) {
	    return "null";
	}
	else if (O.getClass().isArray()) {
	    String tmp = //"new " + typerepr(O) +" "+
                       "{";
	    for (int i=0; i<Array.getLength(O); i++) {
		if (i != 0) tmp += ", ";
		tmp += repr(Array.get(O, i));
	    }
	    return tmp + "}";
	}
        else return O.toString();
    }

    private static Pattern RTRIMEND = Pattern.compile(" +$");

    public static String rtrim(String S) {
        return RTRIMEND.matcher(S).replaceAll("");
    }

    /*
    private static Pattern RTRIMLINE = Pattern.compile(" +\n");

    // remove all trailing whitespaces from every line
    public static String rtrimLines(String S) {
        String tmp = RTRIMLINE.matcher(S).replaceAll("\n");
        return RTRIMEND.matcher(tmp).replaceAll("");
    }
    */

    private static class FailTestException extends RuntimeException {
        FailTestException(String msg) {
            super(msg);
        }
    }
    
    private static class TooMuchOutputException extends RuntimeException {
    }
    
    public static class FailException extends RuntimeException {
        public FailException(String msg) {
            super(msg);
        }
    }
    
    static BasicTestCase currentlyExecutingTestCase;

    public static boolean quietOnPass = false;
    
    protected class BasicTestCase {
        final protected String methodName;
        final protected Object[] args;
	final String saveAs;
        final String apparentName;
        final String thisName;
        final String packaje;
        protected BasicTestCase(String methodName, Object[] args) {
            this(methodName, args, methodName, null);
        }
        protected BasicTestCase(String methodName, Object[] args, String apparentName) {
            this(methodName, args, apparentName, null);
        }
        protected BasicTestCase(String methodName, Object[] args, String apparentName, String thisName) {
            this(null, methodName, args, apparentName, thisName);
        }
        protected BasicTestCase(String packaje, String methodName, Object[] args, String apparentName) {
            this(packaje, methodName, args, apparentName, null);
        }
        protected BasicTestCase(String packaje, String methodName, Object[] args, String apparentName, String thisName) {
            currentlyExecutingTestCase = this;
            this.methodName = methodName;
            this.args = args;
            this.packaje = packaje;
	    this.saveAs = GenericTester.this.saveAs;
	    GenericTester.this.saveAs = null; //reset
            this.thisName = thisName;
            this.apparentName = apparentName;
        }
        protected void describe() {
            if (HTMLdescription != null) {
                graderOut.print(HTMLdescription);
                HTMLdescription = null;
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
                tmp += apparentName + "(";
                if (args.length == 0) tmp += ")";
                else {
                    tmp += repr(args[0]);
                    for (int i=1; i<args.length; i++)
                        tmp += ", " + repr(args[i]);
                    tmp += ")";
                }
                graderOut.println(code(tmp));
            }
            if (testStdinURL != null) {
                String[] urlSplit = testStdinURL.split("/");
                graderOut.println("<code> &lt; <a target=\"_blank\" href=\""+testStdinURL+"\">"+urlSplit[urlSplit.length-1]+"</a></code>");                
                //testStdin = new In(testStdinURL).readAll();
                testStdin = testerStdin.getJsonObject("fetched_urls").
                    getString(testStdinURL);
                testStdinURL = null;
                suppressStdinDescription = true;
            }
	    describeStdin();
        }
	protected void describeStdin() {
	    if (testStdin != null && !suppressStdinDescription) {
		graderOut.println(" with standard input"+pre(testStdin));
	    }
	}

        protected void test() {
            test(referenceC, studentC);
        }

        protected void test(Class clazz) {
            test(clazz, clazz);
        }

        protected void test(Class refClazz, Class stuClazz) {
            boolean notfound = true;
            tryMethods: for (Method m : refClazz.getMethods())
                if (m.getName().equals(methodName)) {
                    Class[] formalParms = m.getParameterTypes();
                    //System.out.println(java.util.Arrays.toString(formalParms));
                    //System.out.println(java.util.Arrays.toString(args));
                    if (formalParms.length != args.length) continue;
                    for (int i=0; i<args.length; i++) {
                        if (args[i] instanceof NamedObject) continue; // ok
                        if (formalParms[i] == int.class && args[i].getClass() == Integer.class) continue; // ok
                        if (formalParms[i] == double.class && args[i].getClass() == Double.class) continue; // ok
                        if (!formalParms[i].isAssignableFrom(args[i].getClass())) continue tryMethods;
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
                        throw new FailTestException("You need to declare a public method " + code(methodName) + " that accepts arguments" + code(argTypes));
                    }
                }            
            if (notfound) throw new RuntimeException("Could not find the reference method "+ code(methodName)+"! Check that floating-point numbers are explicitly specified.");
        }

        protected void testConstructor() {
            testConstructor(referenceC, studentC);
        }
        protected void testConstructor(Class clazz) {
            testConstructor(clazz, clazz);
        }
        protected void testConstructor(Class refClass, Class stuClass) {
            boolean notfound = true;
            tryMethods: for (Constructor m : refClass.getConstructors()) {
                Class[] formalParms = m.getParameterTypes();
                if (formalParms.length != args.length) continue;
                checkParms: for (int i=0; i<args.length; i++) {
                    if (args[i] instanceof NamedObject) continue; // ok
                    if (formalParms[i] == int.class && args[i].getClass() == Integer.class) continue checkParms;
                    if (formalParms[i] == double.class && args[i].getClass() == Double.class) continue checkParms;
                    if (!formalParms[i].isAssignableFrom(args[i].getClass())) continue tryMethods;
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
                    throw new FailTestException("You need to declare a public constructor for " + code(className) + " that accepts arguments" + code(argTypes));
                }
            }
            if (notfound) throw new RuntimeException("Could not find the reference constructor! Check that floating-point numbers are explicitly specified.");
        }



        public void execute() {
            if (quietOnPass) {
                gbaos = new ByteArrayOutputStream();
                graderOut = new PrintStream(gbaos);
            }
            boolean showHellip = testStdin == null;
            graderOut.println("<div class='testcase-desc'>");
            describe();
            
            if (showHellip) graderOut.println("&hellip;");
            graderOut.println("</div>");
            if (thisName != null) {
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
	    cleanup();
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
        }
	public void cleanup() {
	    suppressStdinDescription = false;
            currentlyExecutingTestCase = null;
            expectException = false;
	}
    }

    // descendants must override this
    protected abstract void runTests();

    protected String className; // descendants should define this in constructor
    private String studentName;
    private Class<?> studentC, referenceC;    
    protected Random randgen = new Random();

    private InputStream orig_stdin = System.in;
    private PrintStream orig_stdout = System.out;
    private ByteArrayOutputStream baos;

    static int maxOutputBytes = 10000;
    public void setMaxOutputBytes(int limit) {
        maxOutputBytes = limit;
    }

    public static boolean dontRunReference = false;

    protected void startStdoutCapture() {
        baos = new ByteArrayOutputStream() {
                public void write(byte[] b, int off, int len) {
                    super.write(b, off, len);
                    if (size() > maxOutputBytes) throw new TooMuchOutputException();
                }
            };
        System.setOut(new PrintStream(baos));
	StdOut.resync();
    }

    protected String endStdoutCapture() {
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

    // ignore trailing space characters on every line
    public boolean ignoreTrailingSpaces = true;

    // see equalsApprox methods for more info
    public boolean ignoreRealFormatting = true;

    // accept replacements for double tokens that are pretty close
    // only has any meaning if ignoreRealFormatting is true
    public double realTolerance = 1E-4;

    public String testStdin = null;
    public String testStdinURL = null;
    public String HTMLdescription = null;
    public String saveAs = null;
    public boolean suppressStdinDescription = false;
    public boolean expectException = false;

    TreeMap<String,Object> studentObjects = new TreeMap<>();
    TreeMap<String,Object> referenceObjects = new TreeMap<>();

    static class NamedObject {
	public final String name;
	NamedObject(String S) {name = S;}
    }

    public NamedObject var(String name) {
        return new NamedObject(name);
    }

    // same within relative error 1E-4? 
    // Except: if reference is 0, allow absolute error 1E-4
    // student first, reference second
    public boolean equalsApprox(double s, double r) { 
        if (r == 0)
            return Math.abs(s) <= realTolerance;        
        return Math.abs(s-r) <= realTolerance * Math.max(Math.abs(s), Math.abs(r));
    }

    // pattern from regular expression for real number literals
    // note that this requires a period inside the number!
    // so it is not "all double literals" but rather
    // "things a sane problem could print for a double"
    // except, it doesn't catch NaN, infinity, octal, etc
    public static final Pattern REAL_NUMBER = 
        Pattern.compile("[+-]?(\\d+\\.\\d*|\\.\\d+)"+
                        "([eE][+-]?\\d+)?");

    // split string at "real number" literals
    // return alternating array of non-number text and number tokens
    // note that some strings like "2.2.2" are sort of ambiguous
    public static String[] splitAtReals(String a) {
        ArrayList<String> result = new ArrayList<String>();
        int lastend = 0;
        Matcher m = REAL_NUMBER.matcher(a);
        while (m.find()) {
            result.add(a.substring(lastend, m.start()));
            result.add(m.group());
            lastend = m.end();
        }
        result.add(a.substring(lastend));
        return result.toArray(new String[result.size()]);
    }

    // are these equal, discounting errors and formatting of doubles?
    // student first, reference second (real comparison is asymmetric)
    // does not normalize for trailing whitespace.
    // accepts multi-line strings (\n treated like any other character)
    public boolean equalsApprox(String sline, String rline) {
        if (!ignoreRealFormatting) return sline.equals(rline);
        String[] ssegments = splitAtReals(sline);
        String[] rsegments = splitAtReals(rline);
        if (rsegments.length != ssegments.length) return false;
        for (int i=0; i<rsegments.length; i++)
            if (i%2 == 0 && !rsegments[i].equals(ssegments[i])
                ||
                i%2 != 0 && !equalsApprox(Double.parseDouble(rsegments[i]), 
                                          Double.parseDouble(ssegments[i]))) 
                return false;
        return true;        
    }

    public String rtrimConditional(String S) {
        return ignoreTrailingSpaces ? rtrim(S) : S;
    }

    // are they different? return null if not, html description if so
    public String describeOutputDifference(String stu, String ref) {
        String[] stulines = stu.split("\n", -1);
        String[] reflines = ref.split("\n", -1);
        int samelines = 0;
        while (samelines < Math.min(stulines.length, reflines.length)
               && equalsApprox(rtrimConditional(stulines[samelines]),
                               rtrimConditional(reflines[samelines])))
            samelines++;

        // were they the same?
        if (samelines == stulines.length && samelines == reflines.length)
            return null; // yup!

        // two special cases
        if (samelines == stulines.length - 1 && samelines == reflines.length
            && rtrimConditional(stulines[stulines.length - 1]).equals(""))
            return "Your program printed this output:" + pre(stu)
                + " which is almost correct but <i>an extra newline character was printed at the end</i>.";

        if (samelines == reflines.length - 1 && samelines == stulines.length
            && rtrimConditional(reflines[reflines.length - 1]).equals(""))
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

    Object semicopy(Object O, TreeMap<String, Object> dict) {
        // basic immutable types
        if (O == null || O instanceof String || O instanceof Integer || O instanceof Long || O instanceof Character
            || O instanceof Boolean || O instanceof Short || O instanceof Float || O instanceof Double
            || O instanceof Byte)
            return O;
        if (O instanceof int[]) return Arrays.copyOf((int[])O, ((int[])O).length);
        if (O instanceof short[]) return Arrays.copyOf((short[])O, ((short[])O).length);
        if (O instanceof long[]) return Arrays.copyOf((long[])O, ((long[])O).length);
        if (O instanceof byte[]) return Arrays.copyOf((byte[])O, ((byte[])O).length);
        if (O instanceof boolean[]) return Arrays.copyOf((boolean[])O, ((boolean[])O).length);
        if (O instanceof float[]) return Arrays.copyOf((float[])O, ((float[])O).length);
        if (O instanceof double[]) return Arrays.copyOf((double[])O, ((double[])O).length);
        if (O instanceof char[]) return Arrays.copyOf((char[])O, ((char[])O).length);
        if (O instanceof Object[]) {
            Class cType = O.getClass().getComponentType();
            Object[] OA = (Object[])O;
            Object[] r = (Object[]) Array.newInstance(cType, OA.length);
            for (int i=0; i<OA.length; i++)
                r[i] = semicopy(OA[i], dict);
            return r;
        }
        if (O instanceof NamedObject) return dict.get(((NamedObject)O).name);
        throw new RuntimeException("Don't know how to semicopy "+O.toString());
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
                    boolean correct = smartEquals(sj, rj);
                    boolean refChanged = !smartEquals(oj, rj);
                    boolean stuChanged = !smartEquals(sj, oj);
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
        protected void compare(AccessibleObject referenceM, AccessibleObject studentM, Object[] args, String thisName) {
        boolean methods = referenceM instanceof Method;
        boolean constructors = referenceM instanceof Constructor;

        Capturer ref = null, stu = null;
	String currStdin = testStdin;
	testStdin = null;
        Object[] argsPassedToRef = (Object[])semicopy(args, referenceObjects);
        Object[] argsPassedToStu = (Object[])semicopy(args, studentObjects);
        Throwable referenceException = null;
        Throwable studentException = null;
	if (currStdin != null)
	    StdIn.setString(currStdin);
        try {
            if (dontRunReference) ; else {
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
            if (expectException) throw new RuntimeException("Internal error: bad exception flag");
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
                e.printStackTrace();
                if (e instanceof InvocationTargetException)
                    ((InvocationTargetException)e).getTargetException().printStackTrace();
                throw new RuntimeException("Internal error: " + e.toString() + "<br>Partial output:" + ((ref != null && ref.stdout != null) ? pre(ref.stdout) : ""));                
            }
        }
	if (currStdin != null)
	    StdIn.setString(currStdin);
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
                                            (stu == null || stu.stdout == null || stu.stdout.equals("") ? "" : "<br>Partial printed output:" + pre(stu.stdout)));
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
            if (!smartEquals(stu.retval, ref.retval)) {
                throw new FailTestException("Expected return value " + code(repr(ref.retval)) + " but instead your code returned " + code(repr(stu.retval)));
            }
        }

        if (currentlyExecutingTestCase.saveAs != null) {
            studentObjects.put(currentlyExecutingTestCase.saveAs, stu.retval);
            referenceObjects.put(currentlyExecutingTestCase.saveAs, ref.retval);
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

    protected void test(String methodName, Object... args) {
        new BasicTestCase(methodName, args, methodName).execute();
    }

    protected void testConstructor(Object... args) {
        new BasicTestCase(className, args, "new " + className) {protected void test() {testConstructor();}}.execute();
    }

    protected void construct(String packaje, final String className, final String typeParams, Object... args) {
        new BasicTestCase(packaje, className, args, "new " + className + typeParams) {protected void test() {
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
            protected void describe() {

                if (HTMLdescription != null) {
                    graderOut.print(HTMLdescription);
                    HTMLdescription = null;
                }
                else {
                    graderOut.print("Testing "); // can't be saved as an object
                    String tmp = "java " + fakeNameOfClass;
                    for (String a : argStrings) tmp += " " + a;
                    tmp = code(tmp);
                    graderOut.print(tmp);
                }

                if (testStdinURL != null) {
                    String[] urlSplit = testStdinURL.split("/");
                    graderOut.println("<code> &lt; <a target=\"_blank\" href=\""+testStdinURL+"\">"+urlSplit[urlSplit.length-1]+"</a></code>");
                    //testStdin = new In(testStdinURL).readAll();
                    testStdin = testerStdin.getJsonObject("fetched_urls").
                        getString(testStdinURL);
                    testStdinURL = null;
                    suppressStdinDescription = true;
                }
                describeStdin();
            }}
            .execute();
    }

    private Class[] setup() {
        return setup(className);
    }
    
    // return the reference class and the student class with this name
    private Class[] setup(String whichClass) {
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

    JsonObject testerStdin;
    
    protected void genericMain(String[] args) {
        studentName = args[0];

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
                    graderOut = new PrintStream(new FileOutputStream(FileDescriptor.out));//orig_graderOut;
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
        // but this is to make sure internally generated errors are handles sanely
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