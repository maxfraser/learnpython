# number = input('Please enter a number: ')
# number = int(number)

# if (number % 4) == 0:
#     print('{0} is Mulitple of 4!'. format (number))
# else:
#     print('Your number is not a multiple of 4!')

user_input = input("Enter a number: ")
user_input2 = input("Enter a number: ")

user_input = int(user_input)
user_input2 = int(user_input2)

if (user_input % user_input2) == 0:
    print(f"{user_input2} is a multiple of {user_input}" )
else:
    print(f'{user_input2} is not a multiple of {user_input}')

