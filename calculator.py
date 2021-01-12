# Python program for simple calculator
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


operation = """
Please select operation:
1. Add
2. Subtract
3. Multiply
4. Divide 
"""
print(operation)


#take input from the user
select = int(input('Select operation from 1,2,3,4 : '))

number_1 = int(input('Enter first number: '))
number_2 = int(input('Enter second number: '))

if select == 1:
    print(f'{number_1} + {number_2} =',
          add(number_1, number_2))

elif select == 2:
    print(f'{number_1} - {number_2} =',
          subtract(number_1, number_2))

elif select == 3:
    print(f'{number_1} * {number_2} =',
          multiply(number_1, number_2))

elif select == 4:
    print(f'{number_1} / {number_2} =',
          divide(number_1, number_2))

else:
    print('Invalid input')
