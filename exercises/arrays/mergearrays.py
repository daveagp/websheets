source_code = r"""
#include <iostream>
using namespace std;

void merge(int src1[], int src2[], int len, int dest[])
{
\[
  int oi = 0;
  for(int i=0; i < len; i++){
    dest[oi++] = src1[i];
    dest[oi++] = src2[i];
  }
]\

}
int main() {
   int a1[] = {1, 3, 5};
   int a2[] = {2, 4, 6};
   int a3[6];
 
   // These are 0-length arrays to make sure you coded things correctly
   int *a4 = NULL, *a5 = NULL, *a6 = NULL;
   
   // test your function
   merge(a1, a2, 3, a3);

   // pass in 0-length arrays
   merge(a4, a5, 0, a6);  
  
   return 0;
}
"""

lang = "C++"

description = r"""
Complete the function <tt>merge()</tt> to merge two arrays of 
length <tt>n</tt>, passed as <tt>src1</tt> and <tt>src2</tt> into
an output array <tt>dest</tt>.  You should alternate items from the
src1 array and the src2 array.  
<br>For example is the src1 array and src2 array contents are<br>
<pre>
1 3 5
2 4 6
</pre>
then the dest array should contain

<pre>
1 2 3 4 5 6
</pre>
"""

tests = [
    ["", []]
] # stdin, args

attempts_until_ref = 0
