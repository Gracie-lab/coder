print("Welcome. This is a number profile system")
number = int(input("Enter a number: "))
#check if number is negative
def check_negate(n):
    if n > 0:
        print(n, ' is a positive number')
    elif n == 0:
        print(n, ' is zero')
    else:
        print(n, ' is a negative number')

def even_odd(n):
    if n % 2 == 0:
        print(n, ' is even')
    else:
        print(n, ' is an odd number')

def prime(n):
    count = 0
    factors = []
    check = 0
    for value in range(2,n):
        if (n%value == 0):
            factors.append(value)
            check+=1
    if check >= 1:
        print (n, " is not a prime number")
        print("  It's factors are: " ,factors)
    else:
        print(n, " is a prime number")

def decimal(n):
    if isinstance(n, int) == True:
        print(n, " is not a decimal number.")
    else:
        print(n, " is a decimal number")
def palindrome(n):
    originalNum=n
    reverse=0
    while(n>0):
        remainder=n%10
        reverse=reverse*10+remainder
        n=n//10
    if(originalNum==reverse):
        print(originalNum, " is palindrome!")
    else:
        print(originalNum, " is not a palindrome!")

def perfect(n):
    divisor = 0
    sum = 0
    for element in range(1,number):
        if number % element == 0:
            divisor = element
            sum+=divisor
    if sum == number:
        print(number+ " is a perfect number")
    elif sum > number:
        print(number, " is an abundant number")
    else:
        print(number, " is a deficient number")


check_negate(number)
even_odd(number)
prime(number)
decimal(number)
palindrome(number)
perfect(number)

import math
root = math.sqrt(number)
print("The square root of {} is {}" .format(number, root))

square = number * number
print("The square of {} is {}" .format(number, square))
