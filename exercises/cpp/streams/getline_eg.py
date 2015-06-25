source_code = r"""
#include <iostream>
#include <string>
using namespace std;

int main() {
   int i=0;
   while (true) {
      i++;
      string text;
      getline(cin, text); // buffer to write to, then buffer size
      if (cin.fail()) return 0;
      cout << "Line " << i << ", " << text.length() << " chars: ";
      cout << text << endl;
   }
}
"""

example = True

lang = "C++"

description = r"""
Using <tt>getline(ifstream, string)</tt>.
"""

tests = [
    ["first line\nsecond   line\na very long long long long long long line\nanother line", []]
]


