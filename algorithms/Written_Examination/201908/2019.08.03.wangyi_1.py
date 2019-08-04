import sys


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


a = int(input())
b = int(input())
print(gcd(a, b))
