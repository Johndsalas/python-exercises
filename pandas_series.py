# Use pandas to create a Series from the following data:
# ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi",
#  "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
# Name the variable that holds the series fruits.

import pandas as pd

fruits =  pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi",
            "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

# Run .describe() on the series to see what describe returns for a series of strings.

fruits.describe()

# Run the code necessary to produce only the unique fruit names.

fruits.unique()

# Determine how many times each value occurs in the series.
import pandas as pd
frequencies = fruits.value_counts()
frequencies

# Determine the most frequently occurring fruit name from the series.
most_frequent = frequencies.max()
fruit = frequencies.idxmax()
print("Most frequently occuring fruit is", fruit, "and it shows up", most_frequent, "times" )

# Determine the least frequently occurring fruit name from the series.
least_frequent = fruits.value_counts().min()

frequencies = fruits.value_counts()
frequencies[frequencies == least_frequent]

# Write the code to get the longest string from the fruits series.

import pandas as pd

fruits =  pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi",
            "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])


fruits[fruits.str.len().max()==]

# Find the fruit(s) with 5 or more letters in the name.

fruit_names = fruits.unique()
fruit_names = pd.Series(fruit_names)
length_of_longest_string = fruit_names.str.len().max() 
index_of_longest_string = fruit_names.str.len().idxmax()
longest_string = fruit_names[index_of_longest_string]

print("The longest string in the list of fruits is", longest_string, "and it has", length_of_longest_string, "letters")


# Capitalize all the fruit strings in the series.

fruits.str.capitalize()

# Count the letter "a" in all the fruits (use string vectorization)

fruits.str.count("a")

# Output the number of vowels in each and every fruit.

def count_vowels(item):

    return item.count("a") + item.count("e") +item.count("i") +item.count("o") +item.count("u")

fruits.apply(count_vowels)
# Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.

fruits[fruits.apply(lambda n: True if n.count("o") > 1 else False)]

# Write the code to get only the fruits containing "berry" in the name

fruits[fruits.apply(lambda n: True if "berry" in n else False)]

# Write the code to get only the fruits containing "apple" in the name

fruits[fruits.apply(lambda n: True if "apple" in n else False)]

# Which fruit has the highest amount of vowels?

fruits[fruits.apply(lambda n: n if count_vowels(n).max()]

# Use pandas to create a Series from the following data:

import pandas as pd
import numpy as np

money =  pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', 
'$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', 
'$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', 
'$2,791,759.67', '$769,681.94', '$452,650.23'])

# What is the data type of the series?

type(money)

# Use series operations to convert the series to a numeric data type.

money_float = money.apply(lambda n: n.replace("$","").replace(",","")).astype('float')

# What is the maximum value? The minimum?

print(money_float.max())

print(money_float.min())

############ Bin the data into 4 equally sized intervals and show how many values fall into each bin.

money_float[pd.cut(money_float, 4).value_counts]

# Plot a histogram of the data. Be sure to include a title and axis labels.


money_float.plot.hist()

# Use pandas to create a Series from the following exam scores:

grades = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

# What is the minimum exam score? The max, mean, median?

grades.describe()

grades.median()

# Plot a histogram of the scores.

grades.plot.hist()

# Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.

Letter_grades = grades.apply(lambda n: "A" if n > 89 else "B" if n > 79 else "C" if n > 69 else "F")

print(Letter_grades)

# Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, and that many points should be given to every other score as well.

curve_grade = grades.apply(lambda n: n + (100 - grades.max())).apply(lambda n: "A" if n > 89 else "B" if n > 79 else "C" if n > 69 else "F")

print(curve_grade)

# Use pandas to create a Series from the following string:
import pandas as pd

string = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))

# What is the most frequently occuring letter? Least frequently occuring?

string.value_counts()

########## How many vowels are in the list?

num_vowels = string[string.apply(lambda n: True if n in("a","e","i","o","u") else False).value_counts()]

print(num_vowels)

# How many consonants are in the list?
# Create a series that has all of the same letters, but uppercased
# Create a bar plot of the frequencies of the 6 most frequently occuring letters.