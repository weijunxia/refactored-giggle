# Using the Debugger

# the debugger lets your run your code one line at a time

print('Enter the first number to add:')
first = input()
print('Enter the second number to add:')        
second = input()
print('Enter the third number to add:')
third = input()
print('The sum is ' + first + second + third)

def blahBlahBlah():
    print('blah')
    print('blah')
    print('blah')
    moreBlah()
    print('blah')
    print('blah')
    print('blah')
    moreBlah()
    print('blah')
    print('blah')
    print('blah')

    def moreBlah():
    print('more blahs')
    print('more blahs')
    print('more blahs')

blahBlahBlah()

#! python3

import random

heads = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads =  heads + 1
    if i == 500:
        print('Halfway done!') # Right click to highlight and set breakpoint then do the same to unset breakpoint

print('Heads came up ' + str(heads) + ' times.')

# the debugger is a tool that lets you execute Python code one line at a time and shows you the values in the variables
# open the debug control window with debug > debugger before running the program
# the over button will step over the current line of code and pause on the next one
# the step button will step into a function call.
# the out button will step out of the current function you are in
# the go function will continue the program until the next breakpoint or end of the program.
# the quit button will immediately terminate the program
# breakpoints can be set by right-clicking the file editor window and selecting 'Set breakpoint'
