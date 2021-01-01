import random
from collections import Counter


# numbers = [3,3,3, 1, 5]
# print(three_of_a_kind(numbers))

# quit()
dice_rolls = []
score = 0

for i in range(5):
    die = random.randint(1, 6)
    dice_rolls.append(die)


print(dice_rolls)


for i in range(3):
    indices = input("Choose a dice index between 0 and 4: ")
    
    if indices == "":
        break
    else:
        indices = indices.replace(",", " ")
        indices = indices.split(" ")

        print("Rerolling die at indexes:", indices)

        for index in indices:
            # if they type in a number, convert the number to an integer
            index = int(index)
            die = dice_rolls[index]
            die = random.randint(1, 6)
            dice_rolls[index] = die

        print(dice_rolls)


print(dice_rolls)


def check_if_duplicates_1(dice_rolls):
     if len(dice_rolls) == len(set(dice_rolls)):
         return False
     else:
         return True

result = check_if_duplicates_1

if result:
    print("Yes list contains duplicates")
else:
    print("No duplicates found")

c = Counter(dice_rolls)
print(c)

class Special_list:
    def __init__(self, TOAK, FOAK, FH, LS, HS, Yaht):
        self.TOAK = TOAK
        self.FOAK = FOAK
        self.FH = FH
        self.LS = LS
        self.HS = HS
        self.Yaht = Yaht
    
    def three_of_a_kind(self):
        return(self.TOAK)

    def four_of_a_kind(self):
        return(self.FOAK)
    
    def Full_House(self):
        return(self.FH)

    def Low_straight(self):
        return(self.LS)

    def High_straight(self):
        return(self.HS)

    def Yahtzee(self):
        return(self.Yaht)

special_scores = Special_list()

    

    