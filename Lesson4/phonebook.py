phonebook={}
print(phonebook)
phonebook['max']='0874836268'
phonebook['ollie']='8867397978'
print(phonebook)
print(phonebook['max'])
print(len(phonebook))
print(phonebook.values())
print(phonebook.keys())


for i in range(1):  
    name = input("please enter name")
    number = input("please enter number")
    phonebook[name] = number
    print()

print(phonebook)


phonebook["max"]
phonebook.get("key")

phonebook["max"] = ""


