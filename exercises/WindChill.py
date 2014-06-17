description = r"""
Your program will be given two command-line arguments: <code>t</code>, representing the temperature 
(in Fahrenheit), and <code>v</code>, representing the wind speed 
(in miles per hour). It should print the wind chill <code>w</code> using the 
following formula:
$$\LARGE w = 35.74 + 0.6215 \times t + (0.4275 \times t - 35.75) v ^ {0.16}$$
Use <code>Math.pow</code> to compute the exponent.
<i>Source</i>: <a href="http://www.nws.noaa.gov/om/windchill/index.shtml">National Weather Service</a>
"""

tests = r"""
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
