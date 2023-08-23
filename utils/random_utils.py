import string

from random import Random


def generate_number_in_range(start=1, end=10):
    return Random().randint(start, end)


def generate_word(length=10):
    return ''.join(Random().choices(string.ascii_lowercase, k=length))
