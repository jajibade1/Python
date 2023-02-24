import random

name_string = input("Give me everyone's names, seperated by a comma. ")

names = name_string.split(", ")

num_items = len(names)

random = random.randint(0, num_items - 1)

person = names[random]
print(person + " is the person who is going to pay")
