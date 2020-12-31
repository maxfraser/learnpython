import random

# number = "55"

# if type(number) == int:
#     print('Value is a integer')
# else:
#     print("value is not an integer")
    

text = 'hello'

if text[0] == 'e':
    print("text starts with e")
elif text[1] == 'e':
    print('the second character is e')
elif text[2] == 'l':
    print("the third character is l")
else:
    print("invalid")



# when there is alif, it only executes the first true statement
number1 = random.randint(1,10)
number2 = random.randint(1,10)

if number1  >  number2:
    print(str(number1) + " is greater than " + str(number2))
elif number1 == number2:
    print("values are the same")
else:
    print(str(number1) + " is less than " + str(number2))


