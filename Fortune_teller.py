import random

answer = "yes"

print("Welcome to the Fortune Teller")
print("You need to select a color and I will tell you what the future holds for you!\n")

while answer == "yes":
    color = input("Select a color [yellow, green, blue, red]")

    if color == "yellow" or color == "green":
        number = int(input("Select a number [1,2,5,6]"))
        if number == 1:
            print("Worried about your future career? Don't worry! You'll get want you want, be patient.")
        elif number == 2:
            print("You will become a millionaire at the age of 35!")
        elif number == 5:
            print("You will have a great family with 6 kids!")
        elif number == 6:
            print("You will become famous and everyone will love you!")
        else:
            print("Numbers 1,2,5,6 are the only numbers allowed")

    elif color == "blue" or color == "red":
        number = int(input("Select a number [3,4,7,8]"))
        if number == 3:
            print("You'll live a happy life with for 100 years at least")
        elif number == 4:
            print("You'll become a successful doctor one day!")
        elif number == 7:
            print("You will travel around the world!")
        elif number == 8:
            print("You will get married 3 times!")
        else:
            print("Numbers 3,4,7,8 are the only numbers allowed")
    else:
        print("Colors [yellow, green, blue, red] are only allowed")
    answer = input("Play again? [yes/no]")
