import random

cpu_guess = random.randint(1, 6)
user_input=input("Enter a number: ")

print(cpu_guess)
print(user_input)

if cpu_guess == int(user_input):
    print("You won")
else:
    "You lose"