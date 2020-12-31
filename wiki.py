import requests
import re

url = "https://www.brainyquote.com/topics/websites-quotes"
response = requests.get(url)


extract = re.findall(r'<a href=".*?" title="view quote">(.*?)</a>', response.text)

for quote in extract:
    print(quote)

with open("quote.txt","w") as filehandle:
    for listitem in extract:
        filehandle.write('%s\n' % listitem)    