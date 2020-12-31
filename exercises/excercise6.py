text = "abcdefghijklmnopqrstuvwxyz"

"acefh........"


for alphabet in str(text):
    index = text.index(alphabet)

    if index % 2 == 0:
        print(alphabet)