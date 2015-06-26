description = r"""
Write a program <code>Kettles</code> with a recursive static method
<code>sing(n)</code> which prints the famous "kettles of tea" song.
For example, when <code>n</code> is 3, calling <code>sing(3)</code>
should print out
<pre>
3 kettles of tea on the wall
3 kettles of tea
take one down, pass it around
2 kettles of tea on the wall!
2 kettles of tea on the wall
2 kettles of tea
take one down, pass it around
1 kettles of tea on the wall!
1 kettles of tea on the wall
1 kettles of tea
take one down, pass it around
no more kettles of tea on the wall!
</pre>
<div>
<i>To sing this song, first sing the first four lines, and then sing
the song for a smaller value of n (unless you are done).</i>
This is the strategy that you can turn into
a recursive method.
</div>
Note that we require your song to say <code>1 kettles</code>
instead of the grammatically correct <code>1 kettle</code>. Fixing this 
is left as a challenge for the thirsty.
"""

source_code = r"""
#include <iostream>
using namespace std;

// sings a well-known song about n kettles
void sing(int n) {
   // print three lines
\[
   cout << n << " kettles of tea on the wall" << endl;
   cout << n << " kettles of tea" << endl;
   cout << "take one down, pass it around" << endl;
]\
   if (n > 1) {
      // sing fourth line, with exclamation point!
\[
      cout << n-1 << " kettles of tea on the wall!" << endl;
]\
      // call sing recursively on remaining kettles
      sing(\[n-1]\);
   }
   else { 
      // sing the final line, with exclamation point!
\[
      cout << "no more kettles of tea on the wall!" << endl;
]\
   }
}

int main() {
   int n;
   cin >> n;
   sing(n);
}
"""

lang = "C++"

tests = [
    ["3", []],
    ["1", []],
    ["9", []],
]

attempts_until_ref = 0

