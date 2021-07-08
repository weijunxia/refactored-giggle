# For Loops with Lists, Multiple Assignment, and Augmented Operators

supplies = ['pens', 'pens', 'pens', 'pens', 'pens']


for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies: ' + supplies[i])

# multiple assignment trick
# works from left to right
# used to do swap operations with variables


cat = ['fat', 'orange', 'loud']

size, color, disposition = cat

a = 'AAA'
b = 'BBB'

a, b = b, a

# Augmented operators += -= *= /= %=

spam = 42
spam = spam + 1


# for loops iterate over the values in a list
# the range() function retunrs list-like value, which can be passed to the list function if you need an actual list value
# varaiables can swap their values using multiple assignments
# augmented assignment operators are used for shortcuts
