#based on a Creative Commons Att-NC-SA 3.0 exercise from:
#http://cscircles.cemc.uwaterloo.ca/8-remix/

source_code = r"""
#include <iostream>
using namespace std; 
\[
int main() {
   // 6 pairs of lines
   for (int i=0; i<6; i++) {
      // first line in the pair
      cout << "chr:";
      for (int j=16*i+32; j<16*i+48; j++)
         cout << "  " << (char)j << " ";
      cout << endl;

      // second line in the pair
      cout << "asc:";
      for (int j=16*i+32; j<16*i+48; j++) {
         if (j<100)
            cout << " " << j << " ";
         else
            cout << " " << j;
      }
      cout << endl;
   }
   return 0;
}
]\
"""

lang = "C++"

attempts_until_ref = 0

description = r"""
<p>Write a program that prints out the following table of ASCII values:
<pre>
chr:      !   "   #   $   %   &amp;   '   (   )   *   +   ,   -   .   /
asc: 32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47
chr:  0   1   2   3   4   5   6   7   8   9   :   ;   &gt;   =   &lt;   ?
asc: 48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63
chr:  @   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O
asc: 64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79
chr:  P   Q   R   S   T   U   V   W   X   Y   Z   [   \   ]   ^   _
asc: 80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95
chr:  `   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o
asc: 96  97  98  99  100 101 102 103 104 105 106 107 108 109 110 111
chr:  p   q   r   s   t   u   v   w   x   y   z   {   |   }   ~     
asc: 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127
</pre>
You should use nested loops (it will fail if you just literally print
out the 12 lines above).
"""

tests = [["", []]]
