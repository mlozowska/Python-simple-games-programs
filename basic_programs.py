# basic calculator
name = input('Enter your name: ')
num1 = input('Enter a number: ')
num2 = input('Enter another number: ')  # input = always string
result = float(num1) + float(num2) # need int() to be added to change FLOAT into STRING (possible for both floats and Integer types)
print(f'{name}, your result is: {result}')
