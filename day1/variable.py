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

website1 = "https://google.com"
website2 = "https://wiki.com"

slice = slice(7, -4)

website1 = website1[slice]
website2 = website2[slice]

print(website1)
print(website2)
