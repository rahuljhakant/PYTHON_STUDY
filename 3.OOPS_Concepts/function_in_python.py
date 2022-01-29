def add(a, b):
    c = (a+b)
    return c


def countVowels(str):
    count = 0
    for i in str:
        if i in "aeiouAEIOU":
            count += 1
    return count


def sumTwo(a, b):
    return a+b


def palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False


def primenumber(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
