import math


def isPrime(num):
    isPrime = True
    for i in range(2, math.floor(math.sqrt(num))):
        if (num % i) == 0:
            isPrime = False
            break
    return isPrime


def largestPrimeFactors(x):
    maxFactor = 0
    for i in range(math.floor(math.sqrt(x)), 1, -1):
        if isPrime(i) and (x % i == 0):
            maxFactor = i
            break
    return maxFactor


print(largestPrimeFactors(600851475143))