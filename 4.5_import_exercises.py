
# Import and test 3 of the functions from your functions exercise file.
# Your functions exercise are not currently in a file with a name that can be easily imported. 
# Copy your functions exercise file and name the copy functions_exercises.py.
# Import each function in a different way:

import functions_exercises as f

# 1) import the module and refer to the function with the . syntax

string = " ^&-_-*()  __  V@#$a@$lid_PyT%^&%#&hOn ide@$%ntif@#ier  $#%^-$^   "

f.normalize_name(string)

# 2) use from to import the function directly

from functions_exercises import cumsum

number_list = [1,2,3,4,5,6]

cumsum(number_list)

# 3) use from and give the function a different name

from functions_exercises import col_x as c

column = "BB"

c(column)


# For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.

import itertools as i

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3? 

step_one = list(i.product("abc", "123"))

print(len(step_one))

# How many different ways can you combine two of the letters from "abcd"?

import itertools as i

step_one = list(i.combinations("abcd", 2))

print(step_one)

len(step_one)

# Save this file as profiles.json inside of your exercises directory. 
# Use the load function from the json module to open this file, 
# it will produce a list of dictionaries. 
# Using this data, write some code that calculates and outputs the following information:

import json
with open("profiles.json") as p:
    p1 = json.load(p)

p1


# Total number of users
count = 0

for dictionary in p1:

    for key,value in dictionary.items():

        if key == "_id":

            print(value)
            count += 1

print(count)

# Number of active users

import json
with open("profiles.json") as p:
    p1 = json.load(p)

count = 0

for dictionary in p1:

    for key,value in dictionary.items():
        if key == "isActive" and value == True:

            count += 1

print(count)

# Number of inactive users

import json
with open("profiles.json") as p:
    p1 = json.load(p)

count = 0

for dictionary in p1:

    for key,value in dictionary.items():
        if key == "isActive" and value == False:

            count += 1

print(count)


# Grand total of balances for all users

import json
with open("profiles.json") as p:
    p1 = json.load(p)

total = 0

for dictionary in p1:

    for key,value in dictionary.items():
        if key == "balance":

            comma_removed = value.replace(",", "").replace("$", "")
            number_value = float(comma_removed)

            total +=  number_value

print(total)

# Average balance per user

import json
with open("profiles.json") as p:
    p1 = json.load(p)

sub_total = 0
denominator = 0

for dictionary in p1:

    for key,value in dictionary.items():
        if key == "balance":

            comma_removed = value.replace(",", "").replace("$", "")
            number_value = float(comma_removed)

            sub_total +=  number_value
            denominator += 1

    total = sub_total / denominator

print(total)


# User with the lowest balance

import json
with open("profiles.json") as p:
    p1 = json.load(p)

lowest_balance = 9999999999999999999999999999999999999999999999

for dictionary in p1:

    for key,value in dictionary.items():
        if key == "balance":

            comma_removed = value.replace(",", "").replace("$", "")
            number_value = float(comma_removed)

            if number_value < lowest_balance:

                lowest_balance = number_value

print(lowest_balance)

# User with the highest balance

import json
with open("profiles.json") as p:
    p1 = json.load(p)

highest_balance = -9999999999999999999999999999999999999999999999

for dictionary in p1:

    for key,value in dictionary.items():
        if key == "balance":

            comma_removed = value.replace(",", "").replace("$", "")
            number_value = float(comma_removed)

            if number_value > highest_balance:

                highest_balance = number_value

print(highest_balance)

# Most common favorite fruit
# Least most common favorite fruit

# get friut types
import json
with open("profiles.json") as p:
    p1 = json.load(p)

for dictionary in p1:

    for key,value in dictionary.items():
        if key == "favoriteFruit":

            print(value)

# count each friut type
import json
with open("profiles.json") as p:
    p1 = json.load(p)

strawberry = 0
apple = 0
banana = 0

for dictionary in p1:

    for key,value in dictionary.items():

        if key == "favoriteFruit" and value == "strawberry":
            strawberry += 1

        if key == "favoriteFruit" and value == "apple":
            apple += 1

        if key == "favoriteFruit" and value == "banana":        
            banana += 1

print("strawberry: " + str(strawberry))
print(" apple: " + str(apple))
print(" banana: " + str(banana))

if strawberry > apple and strawberry > banana:
    print("strawberry in the most common favorite fruit!")

if apple > strawberry and apple > banana:
    print("apple in the most common favorite fruit!")

if banana > apple and banana > strawberry:
    print("banana in the most common favorite fruit!")

if strawberry < apple and strawberry < banana:
    print("strawberry in the least common favorite fruit!")

if apple < strawberry and apple < banana:
    print("apple in the least common favorite fruit!")

if banana < apple and banana < strawberry:
    print("banana in the most common favorite fruit!")


# Total number of unread messages for all users

import json
with open("profiles.json") as p:
    p1 = json.load(p)

total_mail = 0

for dictionary in p1:

    for key,value in dictionary.items():

        if key == "greeting":

            for letter in value:

                if letter.isdigit() == False:

                    value = value.replace(letter, "")
            
            total_mail += int(value)   
            
            #unread_message_total += int(value[-19:-17])

print(total_mail)

