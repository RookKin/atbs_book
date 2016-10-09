while True:
    try:
        print('Enter first number to add:')
        first = int(input())
        print('Enter second number to add:')
        second = int(input())
        print('Enter third number to add:')
        third = int(input())

        total = first + second + third
        print('The sum is: %s' % total)
        break

    except ValueError:
        print('Please enter a valid integer')
        continue
