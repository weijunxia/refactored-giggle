import re

message = 'Call me 917-618-8627 tomorrow, or for office line 917-618-8627'

# regex uses a lot of backslashes ie \d (for num char) r'\d'
# import re module first
# call re.compile() fx to create regex obj
# call .search() method to match obj
# call match obj group() to create matched string
# regex is minilang for specifying text patterns. 
# mo or matchObject has .group()
# .findall()

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

print(phoneNumRegex.findall(message))
