# This is a guess the number game.

import random
print('Hello, what is your name?')
name = input()
secretNumber = random.randint(1, 20)
print('Well, ' + name + ', I am thinking of a number between ', secretNumber)

# Ask the player to guess 6 times

for guessTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())
        
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # this condition is the corrrect guess!

if guess == secretNumber:
    print('Good Job, ' + name + '! You guessed the number in my head in ' + str(guessTaken) + ' tries.')
else:
    print('Nope. This number I  was thinking of was ' + str(secretNumber))
    
