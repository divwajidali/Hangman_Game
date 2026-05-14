easy_words = [
    "apple",
    "table",
    "chair",
    "bread",
    "plant",
    "phone",
    "mouse",
    "water",
    "pizza",
    "happy"
]
medium_words = [
    "python",
    "laptop",
    "science",
    "diamond",
    "picture",
    "country",
    "teacher",
    "monster",
    "battery",
    "holiday"
]
hard_words = [
    "algorithm",
    "developer",
    "artificial",
    "cybersecurity",
    "programming",
    "javascript",
    "engineering",
    "microprocessor",
    "communication",
    "transformation"
]
animals = [
    "tiger",
    "elephant",
    "giraffe",
    "kangaroo",
    "dolphin",
    "penguin",
    "alligator",
    "rabbit",
    "monkey",
    "zebra"
]
countries = [
    "pakistan",
    "canada",
    "brazil",
    "germany",
    "japan",
    "turkey",
    "france",
    "italy",
    "china",
    "india"
]
technology = [
    "python",
    "computer",
    "keyboard",
    "internet",
    "database",
    "software",
    "hardware",
    "network",
    "coding",
    "developer"
]
fun_words = [
    "banana",
    "popcorn",
    "chocolate",
    "burger",
    "toaster",
    "robot",
    "dragon",
    "ninja",
    "zombie",
    "pirate"
]


word_categories = {
    1 : easy_words,
    2 : medium_words,
    3 : hard_words,
    4 : animals,
    5 : countries,
    6 : technology,
    7 : fun_words
}
while True:

    choice = input("1. Easy Words\n2. Medium Words\n3. Hard Words\n4. Animals\n5. Countries\n6. Technologies\n7. Fun Words\nEnter Choice :")
    try:
        choice = int(choice)
        if choice in range(1, 8):
            selected_words = word_categories[choice]
            break

        else:
            print("You entered an invalid option.\nPlease enter valid choice.")



    except ValueError:
        print("You entered an invalid option.\nPlease enter valid choice.")
    

    


    
import random

target = random.choice(selected_words)

display = []

for i in range(len(target)):
    display.append("_")

print(display)


lives = 10

while True:
    if "_" not in display:
        print(f"Word : {target}")
        print("You Win!\nGame Over.")
        break

    elif (lives == 0):
        print(f"You Loose!\nWord : {target}\nGame Over")
        break

    guess = input("Enter Guess :")


    if guess in target:
        for i in range(len(target)):
            if target[i] == guess:
                display[i] = guess
                print(f"Lives : {lives}")
                print(display)

    else:
        print("Wrong Guess.")
        lives -= 1
        print(f"Lives : {lives}")
