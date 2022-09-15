import math

def factorial(number):
    if number == 0 or number == 1:
        return number
    else:
        return number * factorial(number-1)


def bionomials(number_1, number_2=2):
    sum = 1
    for i in range(1, number_1+1):
        sum += (factorial(number_1)*math.pow(number_2, i))/factorial(i)
        return sum


n = int(input("enter the n value "))
x = int(input("enter the x value "))

print(bionomials(n, x))
