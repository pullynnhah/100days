# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name = name1.lower() + name2.lower()

true_score = name.count('t') + name.count('r') + name.count('u') + name.count('e')
love_score = name.count('l') + name.count('o') + name.count('v') + name.count('e')

true_love_score = true_score * 10 + love_score

if true_love_score < 10 or true_love_score > 90:
    print(f"Your score is {true_love_score}, you go together like coke and mentos.")
elif true_love_score >= 40 and true_love_score <= 50:
    print(f"Your score is {true_love_score}, you are alright together.")
else:
    print(f"Your score is {true_love_score}.")
