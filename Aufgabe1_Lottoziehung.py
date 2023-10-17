import random

def List(value):
    return list(range(1, value + 1))

def dict(value):
    dict = {}
    for i in range(1, value + 1):
        dict[i] = 0
    return dict

def lotto(list, number_of_draws):
    for i in range(number_of_draws):
        zug = random.randint(0, len(list) - 1 - i)
        list[zug], list[len(list) - 1 - i] = list[len(list) - 1 - i], list[zug]
    return list[-number_of_draws:]

def add_to_List(dict, list):
    for i in list:
        dict[i] += 1
    return dict

for i in range(1000):
    add_to_List(dict(45), lotto(List(45), 6))
    print(lotto(List(45), 6))
