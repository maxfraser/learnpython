import random

# number guessing game
counter = 0
name = input('NAME PLEASE: ')
    
while True:
    #1. computer chooses a random number between 1 and 10
    r = random.randint(1,5)

    #2. ask user to enter a number then print it out
   
    number = input("please enter a number: ") 
    number = int(number)
    #3. we print the two numbers
    print(r)
    print(number)
    counter += 1

    #4. if the two numbers are equal, print you won
    if number == r:
        print(f"{name} won after {counter} times")
        break
    else:
        print("you lose")

    