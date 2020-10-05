print('overview')
print(2*8)
print(16/2)
print('over' + 'view')
name='overview'
age='33'
print(name.replace("o","u"))
print(name[-4])
print(len(name))

import datetime
now = datetime.datetime.now()
print("current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

username='wah'
print("username")
password='wah1'
print("password")

ig_username= input ('enter_username:')
ig_password= input ('enter_username:')

if ig_username == username and ig_password == password:
    print("logged in")
else:
    print("cant loggin") 
