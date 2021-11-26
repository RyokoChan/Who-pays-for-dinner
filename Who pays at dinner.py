
import random

print("Welcome to the Who-pays picker")
names_string = input("Give me everybody's names, separated by a comma and Ill decide who pays. ")
names = names_string.split(", ")

random_integer = random.randint(0, len(names) - 1)


print(names[random_integer] + " " + "is going to buy the meal")