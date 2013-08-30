package framework;
import java.util.*;
import java.lang.reflect.*;
import java.io.*;
public abstract class GenericTester {

    /* "library" helper methods and exceptions */

    public static String esc(String S) {
        return 
            S.replaceAll("&", "&amp;").replaceAll(">", "&gt;")
            .replaceAll("<", "&lt;").replaceAll("  ", " &nbsp;");
    }
            
    public static String pre(String S, String attr) {
        return "<pre "+attr+">\n" + esc(S) + "</pre>";
    }
    public static String pre(String S) {return pre(S, "");}

    public static String code(String S, String attr) {
        return "<code "+attr+">" + esc(S) + "</code>";
    }
    public static String code(String S) {return code(S, "");}

    public static String repr(Object O) {
        if (O instanceof String) {
            return '"' + (String)O + '"';
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
            System.out.println("<div class='testcase-desc'>");
            describe();
            System.out.println("&hellip;</div>");
            test();
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
    }

    protected String endStdoutCapture() {
        try {
            String content = baos.toString("ISO-8859-1");
            System.setOut(orig_stdout);
            return content;
        }
        catch (UnsupportedEncodingException e) {
            throw new RuntimeException(e.toString());
        }
    }

    @SuppressWarnings("unchecked")
    protected void compare(Method referenceM, Method studentM, Object[] args) {
        String referenceO = null, studentO = null;
        Object referenceR = null, studentR = null;
        try {
            startStdoutCapture();
            referenceR = referenceM.invoke(null, args);
            referenceO = endStdoutCapture();
        }
        catch (IllegalAccessException | InvocationTargetException e) {
            referenceO = endStdoutCapture();
            throw new RuntimeException("Internal error: " + e.toString() + "<br>Partial output:" + pre(referenceO));
        }
        try {
            startStdoutCapture();
            studentR = studentM.invoke(null, args);
            studentO = endStdoutCapture();
        }
        catch (IllegalAccessException e) {
            studentO = endStdoutCapture();
            throw new RuntimeException("Internal error: " + e.toString() + "<br>Partial output:" + pre(studentO));
        }
        catch (InvocationTargetException e) {
            studentO = endStdoutCapture();            
            Throwable exc = e.getTargetException();

            String stackTrace = exc.toString();
            boolean first = true;
            for (StackTraceElement ste : exc.getStackTrace()) {
                if (ste.getClassName().equals("student."+studentName+"."+className)) {
                    stackTrace += "\n   "+(first?"at":"called from")+" line " + ste.getLineNumber() + " in " + ste.getMethodName() + "()";
                    first = false;
                }
            }
            throw new FailTestException("Runtime error: " + pre(stackTrace) + 
                                        (studentO.equals("") ? "" : "<br>Partial printed output:" + pre(studentO)));
        }
        if (referenceO.length() > 0 && !referenceO.equals(studentO)) {
            throw new FailTestException("Expected this printed output :" + pre(referenceO)
                                        + " and got this instead :" + pre(studentO));
        }
        if (referenceO.equals("") && !studentO.equals("")) {
            System.out.println("Found this printed output (not required):" + pre(studentO));
        }
        if (referenceM.getReturnType() != Void.TYPE) {
            if (!referenceR.equals(studentR)) {
                throw new FailTestException("Expected return value " + code(repr(referenceR)) + " but instead your code returned " + code(repr(studentR)));
            }
        }
        System.out.print("<div class='pass-test'>");
        System.out.println("Passed test!");
        if (!referenceO.equals("")) {
            System.out.println("Printed correct output " + pre(referenceO));
        }
        if (referenceM.getReturnType() != Void.TYPE) {
            System.out.println("Returned correct value " + pre(referenceR.toString()));
        }
        System.out.println("</div>");
    }

    protected void test(String methodName, Object... args) {
        new BasicTestCase(methodName, args).execute();
    }

    // mainArgs is final just so we can inherit in-line
    protected void testMain(final String... mainArgs) {
        new BasicTestCase("main", new Object[] {mainArgs}) {
            protected void describe() {
                System.out.print("Testing ");
                String tmp = "java " + className;
                for (String a : mainArgs) tmp += " " + a;        
                System.out.println(code(tmp));
            }}
            .execute();
    }

    private void setup() {
        try {
            studentC = Class.forName("student."+studentName+"."+className);
            referenceC = Class.forName("reference."+className);
        }
        catch (ClassNotFoundException e) {
            throw new RuntimeException("Internal error: class not found");
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