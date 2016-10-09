# The command line argument for the keyword is checked
# If the argument is save, then the clipboard contents are saved to the keyword
# if the argument is list, then all the keywords are copied to the clipboard
# Otherwise, the text for the keyword is copied to the keyboard

# Read the command line arguments from sys.argv
# Read and write to the clipboard
# Save and load to a shelf file

#! python3
# mcb.py - Saves and loads pieces of text to the clipboard
# Usage:    py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#           py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#           py.exe mcb.pyw list - loads all keywords to clipboard

import sys, shelve, pyperclip

mcb_shelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
        # List keywords and load content
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcb_shelf.keys())))
        elif sys.argv[1] in mcb_shelf:
            pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
