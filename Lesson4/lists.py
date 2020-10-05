empty_list=list()

empty_list.append(65)

empty_list.append("nan")

empty_list.append(0.5)
empty_list.insert(1,True)

# print(empty_list.count(0.5))

for item in empty_list:
    print(item)





numbers=[1,2,3,4,5,6,7,8,9,10]
print(len(numbers))
print(numbers)

for values in numbers:
    print(values ** 0.5)

cube=[]
for integers in numbers:
    cube.append(integers ** 3)

print(cube)
# print(empty_list)
# print(len(empty_list))