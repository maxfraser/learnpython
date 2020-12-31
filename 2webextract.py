import requests
import re

url = "https://www.geeksforgeeks.org/"
url2 = requests.get(url)
print(url2)

extract = re.findall(r'<a href="(.*?)" title=".*?" rel="bookmark">.*?</a>', url2.text)

for artical in extract:
    print(artical)


with open("2questions.txt","w") as filehandle:
    for listitem in extract:
        filehandle.write('%s\n' % listitem)