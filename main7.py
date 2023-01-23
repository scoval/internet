from random import random

def func(x = random()):
    return x
print(func() == func())