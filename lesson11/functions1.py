def print_max():
    print("max")
    print("hello")

print_max()
 
def greet_customer(special_item, grocery_store):
    print("welcome to " + grocery_store + ". do you want to buy", special_item)
    

greet_customer("avacados","tesco")

def print_to_10(n):
    for number in list(range(1, n + 1)):
        print(number)

def get_first_item(list):
    return list[0]

print(get_first_item([6, 1,2,3,4,5]))

# data types
# if statements
# loops
# functions
# classes


def add(m, n):
    return m + n

def get_first_item(list, index):
    return list[index]

def get_second_item(list):
    return list[1]

print(get_second_item([1,4,6,3]))
