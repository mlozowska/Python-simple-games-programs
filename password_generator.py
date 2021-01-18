import random
import string

# instead of typing all the chars, import string and add string.printable
#chars = "abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!<>?)([]*&^%$#@,./'=-"
chars = string.printable

while 1:
    password_len = int(input("What length would you like your password to be : "))
    password_count = int(input("How many passwords would you like : "))
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(chars)
            password += password_char
        print("Here is your password : ", password)
    break









