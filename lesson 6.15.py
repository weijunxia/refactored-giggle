# List Methods

# Method basically same as function

spam = ['hello', 'hi', 'howdy', 'heya']

# method calls variable and .
# methods find 

spam.index('hello')

# index value will return first instance of multiples
# append adds value to end, 'insert' adds value to specific point

spam.append('yo')

spam.insert(0, 'hola')

# str data type doesnt have an append
# remove specifies value del removes indexed value
# remove only removes first instance of the value if there are multiple


spam.remove('yo')


# .sort() sorts by numerical and alphabetical order ASCII-betical order and keyword argument
# upper case comes first then lower case starting letters
# TRUE alphabetical sorting needs keyword spam.sort(key = str.lower)
# spam.sort(reverse=True)

# cant reverse multiple values with str and integers


