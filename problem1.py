import numpy as np


def sum(max):
    sum = 0
    for i in range(1, max):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    return sum


print(sum(1000))