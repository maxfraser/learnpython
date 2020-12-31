import re 

text = '''
We’re here to help!
If you would like to get in touch, don’t hesitate to pick up the phone or drop us a message. We’d love to hear from you.
 0114 3830989
Monday - Friday
Tuesday - Thursday
9am - 7pm
'''
# print(text)
# print(text.split())

numbers = re.findall(r"\w+day", text)
# print(numbers)


'''
\d means numbers
\s means spaces and newlin characters or tabs
\w means words or string
everything else matches the alphabet e.g. m matches m
. any character

* match 0 or more characters
+ match 1 or more characters
{m,n} -> match characters of length between m and n
m|n means m or n
^m anything that starts with m
n$ endswith n
'''

sentences = """
i love cats and dogs pear fear ear
mat
jack
spear
spare
rate
"""

numbers2 = re.findall(r'^s+', sentences,)
print(numbers2)