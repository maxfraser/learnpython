import requests

imageurl="https://images.theconversation.com/files/319375/original/file-20200309-118956-1cqvm6j.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1200&h=675.0&fit=crop"

image_source=requests.get(imageurl).content

with open("dog2.jpg","wb") as f:
    f.write(image_source)

