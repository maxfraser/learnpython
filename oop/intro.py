class Animal:
    def __init__(self, name, sound):
        # properties / attribute
        self.name = name
        self.sound = sound
        self.age = 0
           
    def make_sound(self):
        print(self.sound)


    # methods
  


dog = Animal("dolly","whoof")
print(dog)
print(dog.name)
dog.name = "daisy"
print(dog.name)
print (dog.age)
dog.age = 12
print(dog.age)
dog.make_sound()

cat = Animal("pablo", "meow")
print(cat.name)
cat.make_sound()

brian = Animal("brian", "yawning",)
print(brian.name)