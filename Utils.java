package websheets;

// a bunch of public static methods without side-effects

import java.util.ArrayList;
import java.util.Arrays;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.lang.reflect.Array;

public class Utils {
    // string representation of class
    public static String classToString(Class<?> clazz) {
        if (clazz.isArray()) return classToString(clazz.getComponentType())+"[]";
        if (clazz.isPrimitive()) return clazz.toString();
        return clazz.getSimpleName();
    }

    // string representation of list of classes, like arg list
    public static String classListToString(Class<?>[] classes) {
        String result = "(";
        for (int i=0; i<classes.length; i++) {
            if (i > 0) result += ",";
            result += classToString(classes[i]);
        }
        return result+")";
    }

    // escape necessary html entities
    public static String esc(String S) {
        return 
            S.replaceAll("&", "&amp;").replaceAll(">", "&gt;")
            .replaceAll("<", "&lt;").replaceAll("  ", " &nbsp;");
    }
            
    // print <pre> element containing this text with these attributes
    public static String pre(String S, String attr) {
	String adjust = S.equals("") ? "<br>" : "";
	return "<pre "+attr+">" + adjust + esc(S) + "</pre>";
    }
    // or no attributes
    public static String pre(String S) {return pre(S, "");}

    // print <code> element containing this text with these attributes
    public static String code(String S, String attr) {
        if (S==null) return "[NULL]";
        return "<code "+attr+">" + esc(S) + "</code>";
    }
    // or no attributes
    public static String code(String S) {return code(S, "");}
    // accept object
    public static String code(Object O) {return code(O.toString(), "");}

    // convert object to human-readable form
    public static String repr(Object O) {
        if (O instanceof String) {
            return '"' + (String)O + '"';
        }
	else if (O == null) {
	    return "null";
	}
	else if (O.getClass().isArray()) {
	    String tmp = "{";
	    for (int i=0; i<Array.getLength(O); i++) {
		if (i != 0) tmp += ", ";
		tmp += repr(Array.get(O, i));
	    }
	    return tmp + "}";
	}
        else return O.toString(); // including NamedObjects
    }

    // remove spaces from end of string
    private static final Pattern RTRIMEND = Pattern.compile(" +$");
    public static String rtrim(String S) {
        return RTRIMEND.matcher(S).replaceAll("");
    }

    // trim if options dictate it
    public static String rtrimConditional(String S, Options o) {
        return o.ignoreTrailingSpaces ? rtrim(S) : S;
    }

    // pattern from regular expression for real number literals
    // note that this requires a period inside the number!
    // so it is not "all double literals" but rather
    // "things a sane problem could print for a double"
    // except, it doesn't catch NaN, infinity, octal, etc
    private static final Pattern REAL_NUMBER = 
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

    // same within relative error 1E-4? 
    // Except: if reference is 0, allow absolute error 1E-4
    // student first, reference second
    public static boolean equalsApprox(double s, double r, Options o) { 
        if (r == 0)
            return Math.abs(s) <= o.realTolerance;        
        return Math.abs(s-r) <= o.realTolerance * Math.max(Math.abs(s), Math.abs(r));
    }

    // are these equal, discounting errors and formatting of doubles?
    // student first, reference second (real comparison is asymmetric)
    // does not normalize for trailing whitespace.
    // accepts multi-line strings (\n treated like any other character)
    public static boolean equalsApprox(String sline, String rline, Options o) {
        if (!o.ignoreRealFormatting) return sline.equals(rline);
        String[] ssegments = splitAtReals(sline);
        String[] rsegments = splitAtReals(rline);
        if (rsegments.length != ssegments.length) return false;
        for (int i=0; i<rsegments.length; i++)
            if (i%2 == 0 && !rsegments[i].equals(ssegments[i])
                ||
                i%2 != 0 && !equalsApprox(Double.parseDouble(rsegments[i]), 
                                          Double.parseDouble(ssegments[i]), o)) 
                return false;
        return true;        
    }

    // similar to clone
    public static Object semicopy(Object O) {
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
        if (opaque(O)) return O;

        throw new RuntimeException("Don't know how to semicopy "+O.toString()+O.getClass());
    }

    // is this a complex object?
    public static boolean opaque(Object o) {
        if (o==null) return false;
        String qualname = o.getClass().toString().substring(6); // trim "class "
        return qualname.startsWith("student.") 
            || qualname.startsWith("reference.")
            || qualname.startsWith("stdlibpack.");
    }

    // is this a stdlib object?
    public static boolean inStdlib(Object o) {
        String qualname = o.getClass().toString();
        return qualname.startsWith("stdlibpack.");
    }

    // student first then reference, where possible
    public static boolean smartEquals(Object a, Object b, Options o) {
        if (a == null || b == null)
            return (a == null && b == null);
        if (inStdlib(a) || inStdlib(b))
            return (a.getClass() == b.getClass()); // for stdlibpack.Queue etc
        if (opaque(a) || opaque(b))
            return opaque(a) && opaque(b);
        if (a.getClass().isArray() != b.getClass().isArray())
            return false;
        if (a.getClass().isArray()) {
            if (Array.getLength(a) != Array.getLength(b))
                return false;
            for (int i=0; i<Array.getLength(a); i++)
                if (!smartEquals(Array.get(a, i), Array.get(b, i), o))
                    return false;
            return true;
        }
        if (a.getClass() == Double.class) 
            return equalsApprox((Double)a, (Double)b, o);
        if (a.getClass() == Float.class)
            return equalsApprox((Float)a, (Float)b, o);
        if (a.getClass() == String.class)
            return equalsApprox((String)a, (String)b, o);

        return a.equals(b);
    }    

    // are they different? return null if not, html description if so
    public static String describeOutputDifference(String stu, String ref, Options o) {
        String[] stulines = stu.split("\n", -1);
        String[] reflines = ref.split("\n", -1);
        int samelines = 0;
        while (samelines < Math.min(stulines.length, reflines.length)
               && equalsApprox(rtrimConditional(stulines[samelines], o),
                               rtrimConditional(reflines[samelines], o),
                               o))
            samelines++;

        // were they the same?
        if (samelines == stulines.length && samelines == reflines.length)
            return null; // yup!

        // two special cases
        if (samelines == stulines.length - 1 && samelines == reflines.length
            && rtrimConditional(stulines[stulines.length - 1], o).equals(""))
            return "Your program printed this output:" + pre(stu)
                + " which is almost correct but <i>an extra newline character was printed at the end</i>.";

        if (samelines == reflines.length - 1 && samelines == stulines.length
            && rtrimConditional(reflines[reflines.length - 1], o).equals(""))
            return "Your program printed this output:" + pre(stu)
                + " which is almost correct but <i>a newline character is missing at the end</i>.";
        
        // general case
        final int samelines2 = samelines; // woo java 8! wouldn't have to do this since samelines is effectively final
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
}