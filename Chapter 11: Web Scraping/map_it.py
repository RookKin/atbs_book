#! /usr/bin/python3
# map_it.py -   Gets a street address from the command line arguments or clipboard
#               Opens the web browser to the Google maps page for the address

# Read the command line arguments from sys.argv
# Read the clipboard contents
# Call the web browser.open() function to open the web browser

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from the command line
    address = ' '.join(sys.argv[1:])

else:
    # Get address from the clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
