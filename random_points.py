import random


def random_point():
    return random.randrange(100), random.randrange(100)


def starting_point(players):
    return [random_point() for p in players]


print(starting_point([1, 3, 5]))
