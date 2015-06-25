lang = "multichoice"

description = """
Consider the following line of C++ code:
<pre>x = y;</pre>
Which of the following are true statements about it?
<i>Select all correct answers.</i>
"""

choices = [
    ["it does the same thing as the line <tt>y = x;</tt>", False],
    ["if <tt>x</tt> has not been declared, it results in an error", True],
    ["if <tt>y</tt> has not been declared, it results in an error", True],
    ["it copies <tt>y</tt>'s value into <tt>x</tt>", True],
    ["it makes <tt>x</tt> and <tt>y</tt> equal forever", False],
]

