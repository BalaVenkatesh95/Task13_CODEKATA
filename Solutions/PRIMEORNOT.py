from sympy import isprime
number = int(input())
if number > 1 and isprime(number):
    print("yes")
else:
    print("no")
