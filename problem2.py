import math


def isFibonacci(n):
    phi = 0.5 + 0.5 * math.sqrt(5.0)
    a = phi * n
    return n == 0 or abs(round(a) - a) < 1.0 / n


def evenSum(max):
    sum = 0

    for i in range(0, max):
        if (isFibonacci(i) and i % 2 == 0):
            sum += i

    return sum


print(evenSum(4000000))