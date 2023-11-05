from pathlib import Path
import os

print("Welcome to Recipies folder")
rec_loc = Path(Path().cwd(), 'Recipies')
print(f'Recipies are located in {rec_loc}')


def count_recipies(rec_loc):
    recipe_count = 0
    for root, _, files in os.walk(rec_loc):
        for file in files:
            if file.lower().endswith(".txt"):
                recipe_count += 1
    return recipe_count


print(f'You have {count_recipies(rec_loc)} recipies\n')


def choose_option():
    choice1='kjs'
    while choice1 not in '123456':
        choice1 = input('''Choose what you want to do
                                [1] - read recipe
                                [2] - create recipe
                                [3] - create category
                                [4] - delete recipe
                                [5] - delete category
                                [6] - end program\n''')

        if choice1 not in '123456' or int(choice1) > 6:
            print('Choose a correct option\n')
    os.system('cls')
    return choice1


def read_recipe(loc):
    var1 = open(loc)
    print(var1.read())
    return var1.read()


def choose_category(loc):
    os.system('cls')
    cat_list = os.listdir(loc)
    print(cat_list)
    x = int(input('''Enter a number to choose category
             1 for desert
             2 for meat etc\n'''))
    return cat_list[x-1]


def choose_recipe(loc):
    rec_list = os.listdir(loc)
    for i, j in enumerate(rec_list):
        print(i+1, j.split('.')[0])
    x = int(input('Enter a number to choose recipe\n'))
    return rec_list[x - 1]


#def show_recipe(loc):
#    rec_list = os.listdir(loc)
#    for i, j in enumerate(rec_list):
#       print(i + 1, j.split('.')[0])


def create_recipe(loc):
    rec_name = input('Enter a new recipe name\n')
    rec_path = Path(loc, f'{rec_name}.txt')
    if os.path.exists(rec_path):
        print('Recipe already exists')
    else:
        open(rec_path, 'w')
        #x.write("")
    return rec_path


def add_recipe_content(loc):
    x = open(loc, 'a')
    content = input('Enter recipe info\n')
    x.write(content)
    x.close()
    print('Content added to recipe')


def create_category(loc):
    cat_name = input('Enter a category name\n')
    new_cat = Path(loc, cat_name)
    if not os.path.exists(new_cat):
        os.mkdir(new_cat)
    else:
        print('Category already exists')
    return new_cat


def delete_category(loc):
    del_cat = str(loc).split('\\')[-1]
    os.rmdir(loc)
    print(f'Deleted {del_cat} category')

def option1(loc):
    print('You selected option to read recipe')
    category = choose_category(loc)
    category_path = Path(loc, category)
    recipe = choose_recipe(category_path)
    recipe_path = Path(category_path, recipe)
    read_recipe(recipe_path)


def option2(loc):
    print('You selected the option to create recipe')
    category = choose_category(loc)
    category_path = Path(loc, category)
    rec_name = create_recipe(category_path)
    add_recipe_content(rec_name)

def option3(loc):
    print('You selected the option to create category')
    create_category(loc)


def show_rec(loc):
    for base,dir,files in os.walk(rec_loc):
        for file in files:
            if file.endswith(".txt"):
                print(file)

def delete_recipe(loc):
    show_rec(loc)
    del_rec = input('Enter a recipe name to delete\n')
    for base,dir,files in os.walk(rec_loc):
        for file in files:
            if file == f'{del_rec}.txt':
                print(file)
                file_path = Path(base,file)
                os.remove(file_path)
        print(f'Deleted {del_rec} recipe')


def option4(loc):
    delete_recipe(loc)


def option5(loc):
    category = Path(loc, choose_category(loc))
    delete_category(category)


def recipe_manual(loc):
    todo = ''
    while todo != '6':
        todo = choose_option()
        if todo == '1':
            option1(loc)
            os.system('cls')
        match todo:
            case '2':
                option2(loc)
                os.system('cls')
            case '3':
                option3(loc)
                os.system('cls')
            case '4':
                option4(loc)
                os.system('cls')
            case '5':
                option5(loc)
                os.system('cls')
    if todo == '6':
        print('Program end')

recipe_manual(rec_loc)



