# Similarties between Lists and Strings

# Slicing
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]

# the difference between immutable and mutable comes up with 'references'
# a reference is a name that refers to the specific location in memory of a value(obj)


spam = [0, 1, 2, 3, 4, 5]

cheese = spam
cheese[1] = 'Hello'

# Reference here has an ID, it refers to the same ID
# can cause subtle bugs, variables don't contain mutable values,
# immutable values don't have this problem b/c they can't be modified in place
# can only be replaced by another value

def eggs(cheese):
    cheese.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

# in this example spam stores reference to a list variable
# IDs are useful because lists can be huge and you don't
# want to call that list everytime in a function (computationally cheap)
# copy module has function called deepcopy creates brand new list
# off the values in original list and returns a reference to new list



import copy

spam = ['A', 'B', 'C', 'D']

cheese = copy.deepcopy(spam)

cheese[1] = 42

# List continuation

spam = ['hello',
        'hola',
        'nihao']

print('4444444' + \
'jasdadjo')

  
    
