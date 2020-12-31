import random

mylist = []
for i in range(20):
    mylist.append(random.randint(1, 50))

print(mylist)

#### print out every number in mylist that is less than 25
number = input("Enter a number: ")
number = int(number)

for i in mylist:
    if i < number:
        print(f"{i} is less than {number}")


