def show_message(name):
    print(name)

# show_message("max")
# show_message("jack")

def login(username):
    user_input = input("Enter your name: ")
    show_message(username)
    
    if username == user_input:
        print("Login succesful")
    else:
        print('Try again')
    return username

user = (login("oliver"))
print(user * 5)
