def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


fruits = ["Apple", "Pear", "Orange"]
make_pie(4)
