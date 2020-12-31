def say_hello(name, last_name):
    print("hello " + name.capitalize() + last_name.capitalize())


num = list(range(10))
previousnum = 0

for i in num:
    sum = previousnum + i
    print('current number' + str(i) + "previous number" + str(previousnum) + 'is' + str(sum))
    previousnum = i


    

