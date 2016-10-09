spam = ['apples', 'bananas','tofu', 'cats', 'truck', 'cow']


def merge(list):
    print ', '.join(list[:-1] + ['and ' + list[-1]])

merge(spam)