import re

# Write a regex to get a strong password
password_regex = re.compile('''(
    ^(?=.*[A-Z])                # at least one capital letter
    (?=.*[0-9])                 # at least one numeric digit
    (?=.*[a-z])                 # at least one lower case letter
    (?=.*[?!@#$%&*])            # at least one of these special characters
    .{8,}                       # at least 8 total digits
    $
    )''', re.VERBOSE)


def strong_password_checker():
    # Get a password from user through raw input
    print('Please enter a strong password: ')
    get_password = input()

    # Compare input to regex
    mo = password_regex.search(get_password)

    # tell user that the password is either strong or not
    if not mo:
        print('That password is not strong enough. Try again.')
        return False
    else:
        print('You got yourself a strong password right there!')
        return True

strong_password_checker()
