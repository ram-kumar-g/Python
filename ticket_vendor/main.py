''' Program for ticket vending machine in a drug store
    Asks user to choose a department
    Based on department this program creates a token using generators and decorators'''

import os

import numbers

while True:
    print('*'*180)
    print('Have a great day')
    print('Please select one of the below ')
    todo = input('P- Perfumes  C- Cosmetics  M- Medicines')
    os.system('cls')

    numbers.decorators(todo)


