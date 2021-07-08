# REGEX SUB() METHOD AND VERBOSE MODE
# https://pythex.org cheatsheet

import re

re.compile(r'''
(\d\d\d) |   # area code (without parens, with dash)
(\(\d\d\d))  # -or- area code with parens and no dash
-            # first dash 
\d\d\d       # first 3 digits
-            # second dash
\d\d\d\d     # last 4 digits
\sx\d{2,4}   # extensions 
''',re.VERBOSE)

# the sub() regex method will sub matches with other text
# using \1, \2 etc will sub group 1,2 etc in the regex patt
# passing re.VERBOSE lets you add whitespace and comments to the regex string passed to re.compile()
# if you want to pass multiple args (re.DOTALL, re.IGNORECASE, re.VERBOSE),
# combine them with | bitwise o perator
