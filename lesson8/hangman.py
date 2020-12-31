import random

with open("countries.txt") as f:
    contents = f.read()

# split by a newline '\n' and assign to the variable countries
countries=contents.split('\n')

# print a random country in the list
country = random.choice(countries)

# empty spaces
# multiply wordguess by the 
wordguess="_" * len(country)
wordguess = list(wordguess)

print(wordguess)

wrong_guesses = 0
# if the user input is in the country then replace the _ in that position by the alphabet
while True:
    letter = input("enter letter: ")

    # check for match
    index = 0
    for alphabet in country:
        if alphabet == letter:
            wordguess[index] = letter
        index += 1

    if not letter in country:
        wrong_guesses += 1

    print(wordguess)
    print()

    if wrong_guesses == 5:
        print("You lose")
        break

    elif wordguess.count("_") == 0:
        print("You won")
        break

print(f"You entered {''.join(wordguess)}")
print(f"Computer chose {country}")