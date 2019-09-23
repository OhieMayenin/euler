import math


def is_palindrome(s):
    # reverse string
    rev = s[::-1]
    # Checking if both string are equal or not
    if s == rev:
        return True

    return False


def largest_palindrome(limit):
    palindromes = []
    for a in range(limit, math.floor(limit/2), -1):
        for b in range(limit, a-1, -1):
            product = a * b
            print("a=", a, "b=", b, "product=", product)
            if is_palindrome(str(product)):
                palindromes.append(product)
    return max(palindromes)


print(largest_palindrome(999))
