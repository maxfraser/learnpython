f=open("numbers.txt","r")

import re

numbers = re.findall(r'\d+',f.read())
print(numbers)

new_numbers = []
for f in numbers:
    new_numbers.append(int(f))
    numbers = new_numbers

print(sum(new_numbers))

