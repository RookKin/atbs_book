def spam():
    global eggs
    eggs = 'spam' # this is global (rule 2)


def bacon():
    eggs = 'bacon' # this is local (rule 3)


def ham():
    print(eggs) # this is global (rule 4)


eggs = 42 # this is global (rule 1)
spam()
print(eggs)