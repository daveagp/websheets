lang = "multichoice"

description = """
How would you copy all files in the current directory to
its parent directory? <i>Select one answer.</i>
"""

choices = [
    ["<tt>mv .. *</tt>", False],
    ["<tt>cp / ~</tt>", False],
    ["<tt>mv ~ /</tt>", False],
    ["<tt>cp * ..</tt>", True],
    ["<tt>mv .. ~</tt>", False],
    ["<tt>cp / *</tt>", False]
]

