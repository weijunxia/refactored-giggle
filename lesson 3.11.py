def div42by(divideBy):
    try:
        return 42/divideBy
    except:
        print('Error: You tried to divide by zero.')

#this code is useful for input variation

print(div42by(2))
print(div42by(12))
print(div42by(0))
#input validation

print('How many cats do you have?')

numCats = input()
try:      
    if int(numCats) < 0:
          print('That is a negative number of cats you psycho ')
    elif int(numCats) >= 4:
        print('That is many cats')
    else:
        print('That is not many cats')
except ValueError:
    print('You did not enter a number.')
    


