# Regex Dot-Star and Caret/Dollar Characters

# ^ indicates looking for match at beginning of string
# $ indicates looking for match at the end of string
# using both means string must match pattern
# (r'^\d+$') indicates that the full string needs to begin and end in that pattern
# . searches for any single character but the new line
# .* pattern to find anything (greedy mode: most text as possible)
# .*? non greedy match
# re.compile(r'.*', re.DOTALL) compiles EVERYTHING in the string
# re.compile(r'', re.I) makes it case insensitive.

Python 3.9.4 (v3.9.4:1f2e3088f3, Apr  4 2021, 12:19:19) 
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> beginsWithHelloRegex = re.compile(r'^Hello')
  >>> beginsWithHelloRegex.search('Hello There')
  <re.Match object; span=(0, 5), match='Hello'>
>>> beginsWithHelloRegex.search('Hello There') == True
False
>>> beginsWithHelloRegex.search('Hello There') == None
False
>>> beginsWithHelloRegex.search('Hello There') == False
False
>>> beginsWithHelloRegex.search('Hello There') == match
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    beginsWithHelloRegex.search('Hello There') == match
NameError: name 'match' is not defined
>>> allDigitsRegex = re.compile(r'\d+$')
>>> allDigitsRegex.search('12312412412412')
<re.Match object; span=(0, 14), match='12312412412412'>
>>> allDigitsRegex.search('12312312x12312')
<re.Match object; span=(9, 14), match='12312'>
>>> allDigitsRegex = re.compile(r'^\d+$')
>>> allDigitsRegex.search('12312312x')
>>> atRegex = re.compile(r'.at')
>>> atRegex.findall('The cat in the hat sat on the flat mat.')
['cat', 'hat', 'sat', 'lat', 'mat']
>>> atRegex = re.compile(r'.{1,2}at')
>>> atRegex.findall('The cat in the hat sat on the flat mat.')
[' cat', ' hat', ' sat', 'flat', ' mat']
>>> 'First Name: Wei Jun Last Name: Xia'
'First Name: Wei Jun Last Name: Xia'
>>> 'First Name: Wei Jun Last Name: Xia'.find(':')
10
>>> 'First Name: Wei Jun Last Name: Xia'[12:]
'Wei Jun Last Name: Xia'
>>> 
>>> nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
>>> nameRegex.findall('First Name: Wei Jun Last Name: Xia')
[('Wei Jun', 'Xia')]
>>> serve = '<To serve humans> for dinner.>'
>>> nongreedy = re.compile(r'<(.*?)>')
>>> nongreedy.findall(serve)
['To serve humans']
>>> greedy = re.compile(r'<(.*)>')
>>> greedy.findall(serve)
['To serve humans> for dinner.']
>>> prime = 'Serve the public trust. \n Protect the innocent. \nUphold the law.'
>>> print(prime)
Serve the public trust. 
 Protect the innocent. 
Uphold the law.
>>> dotStar = re.compile(r'.*')
>>> dotStar.search(prime)
<re.Match object; span=(0, 24), match='Serve the public trust. '>
>>> prime = 'Serve the public trust. \nProtect the innocent. \nUphold the law.'
>>> print(prime)
Serve the public trust. 
Protect the innocent. 
Uphold the law.
>>> dotStar = re.compile(r'.*', re.DOTALL)
>>> dotStar.search(prime)
<re.Match object; span=(0, 63), match='Serve the public trust. \nProtect the innocent. \>
>>> vowelRegex = re.compile(r'[aeiou]')
>>> vowelRegex.search('Wei, why does your programming book talk about RoboCop so much?')
<re.Match object; span=(1, 2), match='e'>
>>> vowelRegex.findall('Wei, why does your programming book talk about RoboCop so much?')
['e', 'i', 'o', 'e', 'o', 'u', 'o', 'a', 'i', 'o', 'o', 'a', 'a', 'o', 'u', 'o', 'o', 'o', 'o', 'u']
>>> vowelRegex = re.compile(r'[aeiou]', re.I)
>>> vowelRegex.findall('Wei, why does your programming book talk about RoboCop so much?')
['e', 'i', 'o', 'e', 'o', 'u', 'o', 'a', 'i', 'o', 'o', 'a', 'a', 'o', 'u', 'o', 'o', 'o', 'o', 'u']
>>> 
