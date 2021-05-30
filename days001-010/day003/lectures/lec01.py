print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the roller coaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

# IndentationError
# if height > 120:
# print("You can ride the roller coaster!")

if height >= 120:
    print("You can ride the roller coaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")
