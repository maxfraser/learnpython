# contents = open('info.log')
# file_contents = contents.read().split("\n")
# print(file_contents)
# contents.close()


with open("info.log") as contents:
    file_contents = contents.read().split("\n")



# checki if the word "WARNING" is present on each line of the list and if yes, print it out

new_content = ""

for i in file_contents:
    if "address" in i:
        new_content = (new_content + i + "\n")

import re

f = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",new_content)
print(f)

uniq = set(f)
print(uniq)


with open('ip_address.txt','w') as filehandle:
    for listitem in uniq:
        filehandle.write('%s\n' % listitem)