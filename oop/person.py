# a Person class with different attributes like, first_name , last_name, age, gender, height
# and two methods get_full_name and year_of_birth (to calculate this you need to use the datettime module. have a read online)

from datetime import datetime

class Person:
    def __init__(self, first_name, last_name, age, gender, height):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.height = height

    def __str__(self):
        return self.get_full_name()
        

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def year_of_birth(self):
        return datetime.today().year - self.age


player = Person("Mike", "Ston", 28, "M", "7ft")
print(player)
print(player.year_of_birth())