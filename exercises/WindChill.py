description = r"""
Given two command-line arguments &mdash; <code>t</code>, representing the temperature 
(in Fahrenheit), and <code>v</code>, representing the wind speed 
(in miles per hour) &mdash; print the wind chill <code>w</code> using the 
following formula:
<div style='text-align: center; margin-top: 0.5em'>
<img src='exercises/WindChill.png'>
</div>
Use <code>Math.pow</code> to compute the exponent.
<i>Source</i>: <a href="http://www.nws.noaa.gov/om/windchill/index.shtml">National Weather Service</a>
"""

tests = r"""
oneRealPerLine = true;
testMain("32.0", "15.0");
testMain("-40", "6.2");
testMain("79.5", "27.62");
"""

source_code = r"""
public static void main(String[] args) {
   double t =\[ Double.parseDouble(args[0])]\; // temperature
\[
        double v = Double.parseDouble(args[1]); // velocity
        // careful to add all three * signs:
        double w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * Math.pow(v, 0.16);
        System.out.println(w); // windchill
]\
}
"""
