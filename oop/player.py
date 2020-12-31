# second calss
#called Player. this should inherit from the Person class
# create two instanes of this clas and print their full names and their age

from person import Person

class Player(Person):
    pass
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age


player = Player("mike", "ston", 28, "m", "12ft")
print(player.age)