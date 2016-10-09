import sys

def collatz(number):
    if number % 2 == 0:
        result = number // 2

        print(result)
        return result
    elif number % 2 == 1:
        result = 3 * number + 1

        print(result)
        return result

try:
    user_number = input('Please enter a number:\n')
    if user_number > 0:
        while user_number != 1:
            user_number = collatz(int(user_number))
    else:
        print('Negative Integers do not compute')
        sys.exit

except ValueError:
    print('Please provide a valid integer')

except NameError:
    print('Please provide a valid integer')

except TypeError:
    print('Please provide a valid integer')