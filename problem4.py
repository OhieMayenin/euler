

def is_palindrome(s):
    # reverse string
    rev = s[::-1]
    # Checking if both string are equal or not
    if s == rev:
        return True

    return False


def largest_palindrome(max):
    for a in range(max, 0, -1):
        for b in range(max, a-1, -1):
            product = a * b
            print("a=", a, "b=", b, "product=", product)
            if is_palindrome(str(product)):
                return product


print(largest_palindrome(999))