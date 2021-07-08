# Dictionary Data Type

# Dictionary is typed w/ {}

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

# Dictionary's keys are size color and disp.
# Values are fat, gray, and loud
# You can access values through keys

myCat['size']

# Dictionaries are unordered unlike lists
# Dics can't be sliced because they aren't ordered
# they are also mutable

# keys(), values(), items()
# tuples are the same things as lists except theyre immutable and use () instead of []
# get() has 2 arguements gets key value or default if doesnt exist 
#   ex: eggs.get('age', 0) OR eggs.get('color', '')

spam = {'name': 'Zophie', 'age': 7}
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
            

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}


if 'color' not in eggs:
    eggs['color'] = 'black'

eggs.setdefault('color', 'black')

