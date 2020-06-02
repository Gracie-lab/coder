import random
start = input("To start, type y, to end, type n: ")
firstInt = random.randrange(1,10)
secondInt = random.randrange(1,10)
product = firstInt * secondInt
try:
    while start != "n":
        answer = int(input("{} multiplied by {} is : " .format(firstInt,secondInt)))
        if product != answer:
            print("Wrong. Try again")
            start = input("To continue, type y, to stop, type n: ")
        else:
            print("Very good")
            start = input("To continue, type y, to stop, type n: ")
            firstInt = random.randrange(1,10)
            secondInt = random.randrange(1,10)
            product = firstInt * secondInt
    else:
        print("End of test")
except ValueError:
    print("invalid input")
    

