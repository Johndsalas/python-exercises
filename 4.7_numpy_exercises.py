#Use the following code for the questions below:

import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

'''
How many negative numbers are there?
'''

len(a[a < 0])

'''
How many positive numbers are there?
'''

import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

len(a[a > 0])

'''
How many even positive numbers are there?
'''

import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

a = a[a > 0]
print(a)

a = a[a % 2 == 0]

len(a)

'''
If you were to add 3 to each data point, how many positive numbers would there be?
'''

import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

a = a + 3

a = a[a > 0]

len(a)

'''
If you squared each number, what would the new mean and standard deviation be?
'''
import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

a = a**2

a.mean()

a.std()


'''
A common statistical operation on a dataset is centering. 
This means to adjust the data such that the center of the data is at 0. 
This is done by subtracting the mean from each data point. Center the data set.
'''

import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

a_mean = a.mean()

print(a_mean)

a = a - a_mean

print(a)


'''
Calculate the z-score for each data point. Recall that the z-score is given by:
'''

import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

a_mean = a.mean()

print(a_mean)

a_std = a.std()

print(a_std)

a = (a-a_mean)/a_std

print(a)

'''
Copy the setup and exercise directions from More Numpy Practice into your 4.7_numpy_exercises.py and add your solutions.
'''
import numpy as np

# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:

# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_of_a = 0

for num in a: sum_of_a += num

print(sum_of_a)


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min_of_a = min(a)
print(min_of_a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max_of_a = max(a)
print(max_of_a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mean_of_a = sum(a)/len(a)

print(mean_of_a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

product_of_a = 1

for number in a: product_of_a *= number

print(product_of_a)

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

squares_of_a = []

for number in a: squares_of_a.append(number**2)

print(squares_of_a)

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

odds_in_a = [num for num in a if num % 2 == 1]
print(odds_in_a)

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = [num for num in a if num % 2 == 0]
print(evens_in_a)

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares 
# for this list of two lists.

b = np.array(
                [3, 4, 5],
                [6, 7, 8]
            )

# Exercise 1 - refactor the following to use numpy. 
# Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**

import numpy as np

b = np.array([
                [3, 4, 5],
                 [6, 7, 8]
            ])

sum_of_b = b.sum()

print(sum_of_b)

# Exercise 2 - refactor the following to use numpy. 

import numpy as np

b = np.array([
                [3, 4, 5],
                 [6, 7, 8]
            ])

min_of_b = b.min()
print(min_of_b)

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.

import numpy as np

b = np.array([
                [3, 4, 5],
                 [6, 7, 8]
            ])

max_of_b = b.max()
print(max_of_b)


# Exercise 4 - refactor the following using numpy to find the mean of b

import numpy as np

b = np.array([
                [3, 4, 5],
                 [6, 7, 8]
            ])

mean_of_b = b.mean()
print(mean_of_b)

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.

import numpy as np

b = np.array([
                [3, 4, 5],
                 [6, 7, 8]
            ])


squares_of_b = np.prod(b)

print(squares_of_b)

# Exercise 6 - refactor the following to use numpy to find the list of squares 

import numpy as np

b = np.array([
                [3, 4, 5],
                 [6, 7, 8]
            ])

b = b**2
squares_of_b = b.reshape(1,6).tolist()

print(squares_of_b)

# Exercise 7 - refactor using numpy to determine the odds_in_b

import numpy as np

b = np.array([
                [3, 4, 5],
                 [6, 7, 8]
            ])

odds_in_b = b[b % 2 == 1]

print(odds_in_b)

# Exercise 8 - refactor the following to use numpy to filter only the even numbers

import numpy as np

b = np.array([
                [3, 4, 5],
                [6, 7, 8]
            ])

evens_in_b = b[b % 2 == 0]

print(evens_in_b)

# Exercise 9 - print out the shape of the array b.

import numpy as np

b = np.array([
                [3, 4, 5],
                [6, 7, 8]
            ])

print(b.shape)


# Exercise 10 - transpose the array b.

import numpy as np

b = np.array([
                [3, 4, 5],
                [6, 7, 8]
            ])

b = np.transpose(b)
print(b)


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

import numpy as np

b = np.array([
                [3, 4, 5],
                [6, 7, 8]
            ])

b = b.reshape(1,6)
print(b)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

import numpy as np

b = np.array([
                [3, 4, 5],
                [6, 7, 8]
            ])

b = b.reshape(6,1)
print(b)

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

# Exercise 2 - Determine the standard deviation of c.

# Exercise 3 - Determine the variance of c.

# Exercise 4 - Print out the shape of the array c

# Exercise 5 - Transpose c and print out transposed result.

# Exercise 6 - Multiply c by the c-Transposed and print the result.

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d

# Exercise 2 - Find the cosine of all the numbers in d

# Exercise 3 - Find the tangent of all the numbers in d

# Exercise 4 - Find all the negative numbers in d

# Exercise 5 - Find all the positive numbers in d

# Exercise 6 - Return an array of only the unique numbers in d.

# Exercise 7 - Determine how many unique numbers there are in d.

# Exercise 8 - Print out the shape of d.

# Exercise 9 - Transpose and then print out the shape of d.

# Exercise 10 - Reshape d into an array of 9 x 2