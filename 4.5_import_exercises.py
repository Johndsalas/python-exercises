
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


# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

# How many different ways can you combine two of the letters from "abcd"?
# Save this file as profiles.json inside of your exercises directory. 
# Use the load function from the json module to open this file, it will produce a list of dictionaries. 
# Using this data, write some code that calculates and outputs the following information:

# Total number of users
# Number of active users
# Number of inactive users
# Grand total of balances for all users
# Average balance per user
# User with the lowest balance
# User with the highest balance
# Most common favorite fruit
# Least most common favorite fruit
# Total number of unread messages for all users