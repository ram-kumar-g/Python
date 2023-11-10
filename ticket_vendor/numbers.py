'''
module code to be called in main program
'''


def create_token_p():
    token_no = 0
    while True:
        token_no += 1
        yield f'Your token is P-{token_no}'


def create_token_m():
    token_no = 0
    while True:
        token_no += 1
        yield f'Your token is M-{token_no}'


def create_token_c():
    token_no = 0
    while True:
        token_no += 1
        yield f'Your token is C-{token_no}'


perfumes = create_token_p()
cosmetics = create_token_c()
medicines = create_token_m()


def decorators(prod):

    print('\nWelcome to our drug shop')
    if prod == 'P' or prod == 'p':
        print(next(perfumes))
    elif prod == 'C' or prod == 'c':
        print(next(cosmetics))
    elif prod == 'M' or prod == 'm':
        print(next(medicines))
    else:
        print('Enter a valid input')

    print("Our representative will reach you shortly")





