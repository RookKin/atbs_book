# Guess the number game!!!

# import the random module
import random

# randomly select a number and tell the player
secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20...')


# Ask the player to guess 6 times
for guesses_taken in range(1, 7):
    print('Take a guess! You have 6 chances.')
    guess = int(input())

    if guess < secret_number:
        print('Your guess is too low')
    elif guess > secret_number:
        print('You number is too high')
    else:
        break # this condition is the correct guess


if guess == secret_number:
    print('Good job! You guessed my number in ' + str(guesses_taken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secret_number))