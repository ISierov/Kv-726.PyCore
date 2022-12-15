"""
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
Good Luck!
FUNDAMENTALSSTRINGS
"""

def double_char(s):
    string = ""
    string = "".join([char *2 for char in s])
    return string

