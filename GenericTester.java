package framework;
import java.util.*;
import java.lang.reflect.*;
import java.io.*;
import stdlibpack.*;
public abstract class GenericTester {

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
        return "<code "+attr+">" + esc(S) + "</code>";
    }
    public static String code(String S) {return code(S, "");}
    public static String code(Object O) {return code(O.toString(), "");}

    public static boolean smartEquals(Object a, Object b) {
        if ((a == null) != (b == null))
            return false;
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
        return a.equals(b);
    }

    // only works for int[] so far
    public static String typerepr(Object O) {
	if (O instanceof int[]) return "int[]";
	if (O instanceof String[]) return "String[]";
	return "???";
    }

    public static String repr(Object O) {
        if (O instanceof String) {
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

    private static class FailTestException extends RuntimeException {
        FailTestException(String msg) {
            super(msg);
        }
    }
    
    protected class BasicTestCase {
        final protected String methodName;
        final protected Object[] args;
        protected BasicTestCase(String methodName, Object[] args) {
            this.methodName = methodName;
            this.args = args;
        }
        protected void describe() {
            System.out.print("Testing ");
            String tmp = methodName + "(";
            if (args.length == 0) tmp += ");";
            else {
                tmp += repr(args[0]);
                for (int i=1; i<args.length; i++)
                    tmp += ", " + repr(args[i]);
                tmp += ")";
            }
            System.out.println(code(tmp));
	    describeStdin();
        }
	protected void describeStdin() {
	    if (testStdin != null && !suppressStdinDescription) {
		System.out.println("with standard input"+pre(testStdin));
	    }
	}
        protected void test() {
            for (Method m : referenceC.getMethods())
                if (m.getName().equals(methodName)) {
                    try {
                        Method referenceM = m;
                        Method studentM = studentC.getMethod(methodName, m.getParameterTypes());
                        if (! referenceM.getReturnType().equals(studentM.getReturnType())) {
                            throw new FailTestException("Your method " + code(methodName) + " should have return type " + code(referenceM.getReturnType().toString()));
                        }
                        if (referenceM.getModifiers() != studentM.getModifiers()) {
                            throw new FailTestException("Incorrect declaration for " + code(methodName) + "; check use of " + code("public") + " and " + code("static") + " or other modifiers");
                        }
                        compare(m, studentM, args);
                    }
                    catch (NoSuchMethodException e) {
                        String argTypes = Arrays.toString(m.getParameterTypes());
                        argTypes = "(" + argTypes.substring(1, argTypes.length()-1) + ")";
                        throw new FailTestException("You need to declare a public method " + code(methodName) + " that accepts arguments" + code(argTypes));
                    }
                }
            
        }
        public void execute() {
            boolean showHellip = testStdin == null;
            System.out.println("<div class='testcase-desc'>");
            describe();
            if (showHellip) System.out.println("&hellip;");
            System.out.println("</div>");
            test();
	    cleanup();
        }
	public void cleanup() {
	    suppressStdinDescription = false;	    
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

    protected void startStdoutCapture() {
        baos = new ByteArrayOutputStream();
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

    // if true, any reference line comprised of a real number
    // allows 1E-4 relative/absolute error in student output
    public boolean oneRealPerLine = false;

    public String testStdin = null;
    public String testStdinURL = null;
    public boolean suppressStdinDescription = false;

    protected String describeOutputDifference(String studentO, String referenceO) {
	if (oneRealPerLine) {
	    String[] stulines = studentO.split("\n");
	    String[] reflines = referenceO.split("\n");
	    String desc = "Your output:" + pre(studentO) + "Correct output:" + pre(referenceO);
	    if (reflines.length > stulines.length)
 		return "Printed too few lines of output. " + desc;
	    if (reflines.length < stulines.length) 
 		return "Printed too many lines of output. " + desc;
	    for (int i=0; i<reflines.length; i++) {		
		double r, s;
		try {
		    r = Double.parseDouble(reflines[i]);
                    if (reflines[i].indexOf(".") < 0) throw new Exception();
		    try {
			s = Double.parseDouble(stulines[i]);
		    }
		    catch (Exception e) {
			return "Line "+(i+1)+" of your output is not a number. " + desc;
		    }
		    if (Math.abs(s-r) > 1E-4 * Math.max(1, Math.abs(r)))
			return "Line "+(i+1)+" of your output doesn't match ours. " + desc;
		}
		catch (Exception e) {
		    // reference line not a double
		    if (!stulines[i].equals(reflines[i]))
			return "Line "+(i+1)+" of your output doesn't match ours. " + desc;

		}
	    }
	    return null;
	}
	else {
	    if (referenceO.equals(studentO))
		return null;

	    if (referenceO.equals(studentO+"\n"))
		return "Your program printed this output:" + pre(studentO)
		    + " which is almost correct but <i>a newline character is missing at the end</i>.";
	    
	    if (studentO.equals(referenceO+"\n"))
		return "Your program printed this output:" + pre(studentO)
		    + " which is almost correct but <i>an extra newline character was printed at the end</i>.";
	    
	    return "Your program printed this output:" + pre(studentO)
		+ " but it was supposed to print this output:" + pre(referenceO);
	}
    }	    
    
    abstract class Capturer {
        String stdout;
        boolean crashed;

        Capturer() {
            startStdoutCapture();
        }
        void end() {
            stdout = endStdoutCapture();
        }
    }

    class InvokeCapturer extends Capturer {
        Object retval;
        InvokeCapturer(Method m, Object dis, Object[] args) throws IllegalAccessException, InvocationTargetException {
            super();
            crashed = true;
            try {
                retval = m.invoke(dis, args);
                crashed = false;
            } finally {
                end();
            }
        }
    }

    class ClassInitCapturer extends Capturer {
        Class foundClass;
        ClassInitCapturer(String className) throws ClassNotFoundException {
            super();
            crashed = true;
            try {                
                foundClass = Class.forName(className);
                crashed = false;
            } finally {
                end();
            }
        }
    }

    Object semicopy(Object O) {
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
                r[i] = semicopy(OA[i]);
            return r;
        }
        throw new RuntimeException("Don't know how to semicopy "+O.toString());
    }

    // only works for non-nested arrays so far
    void checkForArgMutations(Object[] orig, Object[] ref, Object[] stu) {
        String commentary = "";
        int n = orig.length;
        for (int i=0; i<n; i++) {
            if (orig[i].getClass().isArray()) {
                int len = Array.getLength(orig[i]);
                for (int j=0; j<len; j++) {
                    Object oj = Array.get(orig[i], j);
                    Object rj = Array.get(ref[i], j);
                    Object sj = Array.get(stu[i], j);
                    boolean correct = smartEquals(rj, sj);
                    boolean refChanged = !smartEquals(rj, oj);
                    boolean stuChanged = !smartEquals(sj, oj);
                    if (refChanged && correct)
                        commentary += "<p>Changed element "+code(j)+" of arg "+code(i)+" to "+code(repr(rj))+" as expected.";
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
        if (commentary != "") { // passed, and some expected mutations were performed 
            System.out.println("<div class='side-effects'>"+commentary+"</div>");
        }
    }

    @SuppressWarnings("unchecked")
    protected void compare(Method referenceM, Method studentM, Object[] args) {
        InvokeCapturer ref = null, stu = null;
	String currStdin = testStdin;
	testStdin = null;
        Object[] argsPassedToRef = (Object[])semicopy(args);
        Object[] argsPassedToStu = (Object[])semicopy(args);
	if (currStdin != null)
	    StdIn.setString(currStdin);
        try {
            ref = new InvokeCapturer(referenceM, null, argsPassedToRef);
        }
        catch (IllegalAccessException | InvocationTargetException e) {
            e.printStackTrace();
            throw new RuntimeException("Internal error: " + e.toString() + "<br>Partial output:" + ((ref != null && ref.stdout != null) ? pre(ref.stdout) : ""));
        }
	if (currStdin != null)
	    StdIn.setString(currStdin);
        try {
            stu = new InvokeCapturer(studentM, null, argsPassedToStu);
        }
        catch (IllegalAccessException e) {
            throw new RuntimeException("Internal error: " + e.toString() + "<br>Partial output:" + pre(stu.stdout));
        }
        catch (InvocationTargetException e) {
            Throwable exc = e.getTargetException();

            String stackTrace = exc.toString();
            boolean first = true;
            for (StackTraceElement ste : exc.getStackTrace()) {
                if (ste.getClassName().equals("student."+studentName+"."+className)) {
                    stackTrace += "\n   "+(first?"at":"called from")+" line " + ste.getLineNumber() + " in " + ste.getMethodName() + "()";
                    first = false;
                }
            }
            throw new FailTestException("Runtime error: " 
					+ 
					pre(stackTrace) 
					+ 
                                        (stu == null || stu.stdout == null || stu.stdout.equals("") ? "" : "<br>Partial printed output:" + pre(stu.stdout)));
        }
        if (ref.stdout.length() > 0) {
	    String reason = describeOutputDifference(stu.stdout, ref.stdout);
	    if (reason != null)
		throw new FailTestException(reason);
        }
        if (ref.stdout.equals("") && !stu.stdout.equals("")) {
            System.out.println("Found this printed output (not required):" + pre(stu.stdout));
        }
        if (referenceM.getReturnType() != Void.TYPE) {
            if (!smartEquals(ref.retval, stu.retval)) {
                throw new FailTestException("Expected return value " + code(repr(ref.retval)) + " but instead your code returned " + code(repr(stu.retval)));
            }
        }
        
        checkForArgMutations(args, argsPassedToRef, argsPassedToStu);
        
        System.out.print("<div class='pass-test'>");
        System.out.println("Passed test!");
        if (!ref.stdout.equals("")) {
            System.out.println("Printed correct output " + pre(ref.stdout));
        }
        if (referenceM.getReturnType() != Void.TYPE) {
            System.out.println("Returned correct value " + pre(repr(ref.retval)));
        }
        System.out.println("</div>");
    }

    protected void test(String methodName, Object... args) {
        new BasicTestCase(methodName, args).execute();
    }

    // mainArgs is final just so we can inherit in-line
    protected void testMain(final Object... argObjs) {
	final String[] argStrings = new String[argObjs.length];
	for (int i=0; i<argStrings.length; i++)
	    argStrings[i] = argObjs[i].toString();
        new BasicTestCase("main", new Object[] {argStrings}) {
            protected void describe() {
                System.out.print("Testing ");
                String tmp = "java " + className;
                for (String a : argStrings) tmp += " " + a;
		tmp = code(tmp);
		if (testStdinURL != null) {
		    String[] urlSplit = testStdinURL.split("/");
		    tmp += "<code> &lt; <a target=\"_blank\" href=\""+testStdinURL+"\">"+urlSplit[urlSplit.length-1]+"</a></code>";
		    testStdin = new In(testStdinURL).readAll();
		    testStdinURL = null;
		    suppressStdinDescription = true;
		}
                System.out.println(tmp);
		describeStdin();
            }}
            .execute();
    }

    private void setup() {
        try {
            ClassInitCapturer stu = new ClassInitCapturer("student."+studentName+"."+className);
            ClassInitCapturer ref = new ClassInitCapturer("reference."+className);
            studentC = stu.foundClass;
            referenceC = ref.foundClass;

            if (stu.stdout.length() > 0) {
                System.out.println("<div>Warning: your class printed the output "+pre(stu.stdout)+" before any method was called.</div>");
            }
        }
        catch (ClassNotFoundException e) {
            throw new RuntimeException("Internal error: class not found " + e);
        }
    }
    
    protected void genericMain(String[] args) {
        studentName = args[0];
        setup();
        try {
            runTests();
            System.out.println("<div class='all-passed'>All tests passed!</div>");
        }
        catch (FailTestException e) {
            System.out.println("<div class='error'>"+e.getMessage()+"</div>");
            System.out.println("<div class='not-all-passed'>Did not pass all tests.</div>");
        }
    }

}