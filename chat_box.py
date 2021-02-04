x = input("Enter your name: ")
print(f"Your name is {x}")

y =(input("Is is your real name? Enter: y/n ")).lower()
if y == 'y':
    print(f'I am glad, you\'ve entered correct name, {x}!')
elif y == 'n':
    print('I was duped')
else:
    print('Hey, you do not answer my question correctly!')



