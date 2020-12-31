import numpy

number = 123456

#1, 2, 4, 5, 10, 20, 25, 50, 100

for i in range(1, number+1):
    if (number % i) % i == 0:
        print(f'{i} is a multiple of {number}')



