# The Raise and Assert Statements

"""

************
*          *
*          *
*          *
************

"""

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string with a length of 1.')
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater or equal to 2.')
    print(symbol * width)   
    for i in range(height - 2):
        print(symbol + (' ' * (width -2)) + symbol)
    print(symbol * width)

boxPrint('*', 10, 10)

# in this example if length of symbol != 1 raise new exception 


market_2nd = {'ns': 'green', 'ew': 'red'} # dic DS for street intersection

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

# assert statement holds that this statement always true or else there is something wrong
# you can raise your own exceptions: rase Exception('This is the error message')
# you can also use assertions: assert condition 'Error message'
# Assertions are for detecting programmer errors that are not meant to be recovered from
# User errors should raise exceptions


switchLights(market_2nd)

