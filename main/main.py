# # first_name = "Bro"
# # last_name = "Code"
# # full_name = first_name + " " + last_name

# # print("Hello " + full_name)

# age = 31
# age = age + 1
# print(age)
# print(type(age))

# height = 250.5
# print("your height is " + str(height) + "cm")
# print(type(height))

# human = False
# print("Are you a human: " + str(human))
# print(type(human))

# multiple assignment
# name = "bro"
# age = 21
# attractive = True

# print(name)
# print(age)
# print(attractive)

# nultiple assignment of code in one line
# a = b = c = 10
# print(a)
# print(b)
# print(c)

# few usefull string methods

# name = "Bro code"

# print(len(name))
# print(name.find("B"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("o"))
# print(name.replace("o", "w"))
# print(name*3)

# type casting in python
# x = 1 #int
# y = 2.0 #float
# z = "3" #string

# x = float(x)
# y = float(y)
# z = str(z)

# print("x is " + str(x))
# print("y is " + str(y))
# print("z is " + z * 3)

# user input in python
# name = input("What is your name? ")
# age = int(input("How old are you? "))

# age = age + 1

# print("Hello " + name)
# print("You are " + str(age) + " years old")

# math function 

# import math

# pi = -3.14
# x = 1
# y = 2
# z = 3
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(pow(pi, 2))
# print(math.sqrt(420))
# print(max(x, y, z))
# print(min(x, y, z))
# print(math.pi)

# slicing = create a substring by extractiong elements from another string indexing[] or slice()
            # [start: stop: steep]
# name = "Bro code"

# first_name = name[0:3]
# last_name = name[4:8]
# funky_name = name[0:8:2]
# reverse_name = name[::-1]

# print(first_name)
# print(last_name)
# print(funky_name)
# print(reverse_name)

# website1 = "https://google.com"
# website2 = "https://wiki.com"

# slice = slice(7, -4)

# website1 = website1[slice]
# website2 = website2[slice]

# print(website1)
# print(website2)

# if statement 
# age = int(input("How old are you? : "))

# if age == 100:
#     print("You are a century old!")
# elif age >= 18:
#     print("Yor are and adult")
# elif age < 0:
#     print("You haven't born yet!")
# else:
#     print("Yor are a child!")

# logical operatore(and, or, not) in python

# temp = int(input("What is the temperature outside? : "))

# if not(temp >= 0 and temp <= 30):
#     print("The temperature is good today!")
#     print("go outside!")
# elif not(temp < 0 or temp > 30):
#     print("the temperature is bad today!")
#     print("stay inside!")

# while loop in python

# name = None

# while len(name) == 0:
#     name = input("Enter your name: ")

# print("Hello " + name)

# for loop in python
# for i in range(10):
    # print(i+1)
# for i in range(1, 10):
    # print(i)

# for i in range(1, 10, 2):
#     print(i)

# for i in "Bro Code":
#     print(i)

# import time

# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("Happy new year!")

# nested loop 
# rows = int(input("How many rows?: "))
# columns = int(input("How many column? "))
# symbol = input("Enter a symbol to use: ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end=" ")
#     print()

# loop control statement

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break;

# phone_number = "123-456-8090"

# for i in phone_number:
#     if i == '-':
#         continue
#     print(i, end="")

# for i in range(1, 5):
#     if i == 4:
#         pass
#     else:
#         print(i)

# list 

# food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
# food[0] = "suci"
# print(food[0])

# food.append("ice cream")
# food.remove("suci")
# food.pop()
# food.insert(0, "cake")
# food.sort()
# food.clear()

# for x in food:
#     print(x)

# 2D lists

# dinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["case", "ice cream"]

# food = [dinks, dinner, dessert]

# print(food[0][1])

# tuple = collection which is ordered and unchangeable used to group together related data

# student = ("Bro", 21, "male")

# print(student.count("Bro"))
# print(student.index("male"))

# for x in student:
#     print(x)

# if "Bro" in student:
#     print("Brow is here!")

# set 

utensils = {"fork", "fork", "spon", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()

# for x in utensils:
#     print(x)

# dishes = {"bowl", "plate", "cup", "spon"}

# # utensils.update(dishes)
# # dinner_table = utensils.union(dishes)

# print(utensils.difference(dishes))
# print(utensils.intersection(dishes))

# # for x in dinner_table:
# #     print(x)

# capitals = {'USA':'Wasington DC',
#             'India':'New Dehli',
#             'China':'Beijing',
#             'Russia':'Moscow'}

# capitals.update({'Germany':'Berlin'})
# capitals.update({'USA':'Las Vegas'})
# capitals.pop('China')
# capitals.clear()
# # print(capitals['Germany'])
# # print(capitals.get('Germany'))
# # print(capitals.keys())
# # print(capitals.values())
# # print(capitals.items())

# for key, value in capitals.items():
#     print(key, value)

# index operator [] = gives access to a sequence's element (str, list, tuples)

# name = "bro Code"

# # if name[0].islower():
# #     name = name.capitalize()

# first_name = name[0: 3].upper()
# last_name = name[3:].lower()
# last_character = name[-2]

# # print(first_name + " " + last_name)
# print(last_character)

# ------- function --------------
# def hello(name):
#     print("Hello " + name)
#     print("have a nice Day")

# name = "Bro"
# hello(name)

# ---------- return statement ---------
def multiply(number1, number2):
    return number1 * number2

x = multiply(6, 8)

print(x)
