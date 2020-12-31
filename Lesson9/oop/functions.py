# how to define a function
# def function_name(parameters_if_any):
#   method_body_and_other_code_to_be_§executed

# how to call a function
# function_name(parameers_if_any)
import math
def square_root(number):
    # calculate the square root here
    return  math.sqrt(number)

# print(square_root(49))
# print(square_root(64))
# print(square_root(16))
# print(square_root(81))


def average(numbers: list):
    # sum of all the numbers divide by how many items in the list
   return sum(numbers) / len(numbers)



# print(average([1,2,3,4,5,6,7,7,8,8,9,10,11,12,13]))
# print(average([91,84,62,81,83,23,27,68,91,11]))
# print(average([1,2,3]))
    

# create a method called mode. pass it a lst and return the most common numer
def mode(intergers: list):
    # find the unique numbers in the list and store in another list
    unique = []
    for num in intergers:
        if not num  in unique:
            unique.append(num)

    # loop through the unique numbers and print each of the numbers
    if num in unique:
        pass

    return (intergers)


mode([1,2,3,5,2,1,6,3,6,2,4,2,7])


# loops
# functions
# if statements
# classes
# data types


35.5
12.3
17.9
293.44

"hello world"
"hello taiwo"
"24"
"jfsfvjt"

{1,2,3,4,5}
{2,4,6,"8"}
{4,8,12,"16"}
{7,14,21,28,"35"}

{1, '', [], {}}

(0, "", 3.5, [])
("", 7, {}, 8)
(9, 6, 7, {})
([], 34, 287, "")

12
2
6
4


{"hello world": 2, "forty": 40}
{"ab": 3, "88": 55}
price = {"shoe": 34, "bag": 12}
{"ya": 45, "bag": 56}
{"shoe": 34, "bag": 55, "t-shirt": 10}

