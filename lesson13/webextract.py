import requests
import re

url = 'https://stackoverflow.com/questions'
r = requests.get(url)


questions = re.findall(r'<a href=".*?" class="question-hyperlink">(.*?)</a>', r.text)

for question in questions:
    print(question)


with open("questions.txt","w") as filehandle:
    for listitem in questions:
        filehandle.write('%s\n' % listitem)