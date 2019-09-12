
# Conditional Basics

#prompt the user for a day of the week, print out whether the day is Monday or not

print("Name a day of the week.")

day = input()

if day.lower() == "monday":
    print("The named day is monday!")
    
else:
    print("The named day is not monday!")


#prompt the user for a day of the week, print out whether the day is a weekday or a weekend

def weekend():

    print("Name a day of the week.")
    
    day = input()

    if day.lower() == ("saturday" or "sunday"):
        print(f"{day} is a weekend!")
    
    elif day.lower() == "monday" or "tuseday" or "wednesday" or "thursday" or "friday":
        print(f"{day} is a weekday!")
    
    else: 
        print("Invalid entry!")
        print("")
        weekend()
        
weekend()

#create variables and make up values for

#the number of hours worked in one week
hours_per_week = 50
#the hourly rate

hourly_rate = 12.50

#how much the week's paycheck will be

pay_check = hours_per_week * hourly_rate

#write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

def weekly_paycheck(hours_per_week,hourly_rate):
    
    overtime = 0
    regular_time = 0
    
    if hours_per_week > 50:
        overtime = (hours_per_week-40) * (hourly_rate * 1.5)
        
    regular_time = hours_per_week * hourly_rate
    
    weekly_pay = overtime + regular_time
    
    return weekly_pay

weekly_paycheck(50,12.50)
#Loop Basics

#While

#Create an integer variable i with a value of 5.
#Create a while loop that runs so long as i is less than or equal to 15
#Each loop iteration, output the current value of i, then increment i by one.

i = 5

while i <= 15:
    print(i)
    i += 1

#Create a while loop that will count by 2's starting with 0 and ending at 100. 
#Follow each number with a new line.

i = 0

while i <= 100:
    print(i)
    i += 2

#Alter your loop to count backwards by 5's from 100 to -10.

i = 100

while i >= -10:
    print(i)
    i -= 5


#Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. 

i = 2

while i < 1000000:
    print(i)
    i = (i * i)

#Write a loop that uses print to create the output shown below.

100
95
90
85
80
75
70
65
60
55
50
45
40
35
30
25
20
15
10
5

i = 100

while i >= 5:
    print(i)
    i -= 5

#Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

print("Give me a number.")

number = input()

x = 1

while x <= 10:
    
    print(f"{number} X {x} = " + str(int(number) * x))
    x += 1

#Create a for loop that uses print to create the output shown below.

1
22
333
4444
55555
666666
7777777
88888888
999999999

x = 1

while x <= 9:

    print(str(x) * int(x))

    x += 1

#break and continue

"""break and continue

Prompt the user for an odd number between 1 and 50. 
Use a loop and a break statement to continue prompting the user if they enter invalid input. 
(Hint: use the isdigit method on strings to determine this). 
Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
"""


gate_keeper = True

while gate_keeper == True:
    
    print("Odd number, please?")
    number = input()
    
    if number.isdigit() == True:
        number = int(number)
        
        if number % 2 != 0:
            break
            
i = 1

print(f"The number being skipped is: {number}")
print("")

while i <= 50:
    
    if i == 1 and number == 1:
        print(f"Yikes! Skipping number: {i}")
        i += 1
        continue
    
    if i % 2 == 0: 
        i += 1
        continue
        
    if i == number:
        print(f"Yikes! Skipping number: {i}")
        i += 1
        continue
    
    print(f"Here is an odd number: {i} ")
    i += 1

"""
The input function can be used to prompt for input and use that input in your python code. 
Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
(Hints: first make sure that the value the user entered is a valid number, also note that the input function 
returns a string, so you'll need to convert this to a numeric type.)

"""

gate_keeper = True
count = 0 

while gate_keeper == True:

    print("Positive number, please?")
    number = input()
    print("")
    
    if number.isdigit() == True:
        number = int(number)
        
        if number > 0:
            break
            
while count <= number:
    
    print(count)
    count += 1



#Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.


gate_keeper = True

while gate_keeper == True:
    
    print("Positive number, please?")
    number = input()
    print("")
    
    if number.isdigit() == True:
        number = int(number)
        
        if number > 0:
            break
            
while number > 0:
    
    print(number)
    number -= 1

Fizzbuzz

'''
One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

Write a program that prints the numbers from 1 to 100.
For multiples of three print "Fizz" instead of the number
For the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".

'''
count = 1

while count <= 100:

    if count % 3 == 0 and count % 5 == 0:
        print("FizzBuzz")
    
    elif count % 3 == 0:
        print("Fizz")

    elif count % 5 == 0:
        print("Buzz")

    else: print(count)

    count += 1

'''
Display a table of powers.
Prompt the user to enter an integer.
Display a table of squares and cubes from 1 to the value entered.
Ask if the user wants to continue.
Assume that the user will enter valid data.
Only continue if the user agrees to.
Example Output

What number would you like to go up to? 5

Here is your table!

number | squared | cubed
------ | ------- | -----
1      | 1       | 1
2      | 4       | 8
3      | 9       | 27
4      | 16      | 64
5      | 25      | 125

Bonus: Research python's format string specifiers to align the table
'''


gate_keeper = True

while gate_keeper == True:
    
    print("What number do you want to go to?")
    number = input()

    count = 1
    number = int(number)

    print("")
    print("number | squared | cubed")
    print("------ | ------- | -----")

    while count <= number:
    
        print("{:7}|{:9}|{:6}".format(count, count ** 2, count ** 3))
    
        count += 1
    
    print("")
    print("Do you wish to continue?")
    wish = input()
    
    if wish.lower() != "yes":
        gate_keeper = False
        
 '''
Convert given number grades into letter grades.

Prompt the user for a numerical grade from 0 to 100.
Display the corresponding letter grade.
Prompt the user to continue.
Assume that the user will enter valid integers for the grades.
The application should only continue if the user agrees to.
Grade Ranges:

A : 100 - 88
B : 87 - 80
C : 79 - 67
D : 66 - 60
F : 59 - 0
Bonus

Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).
'''

gate_keeper = True

while gate_keeper == True:
    
    print("Enter numerical grade.")
    grade = input()
    grade = int(grade)

    if grade in range(99,101):
        print("A+")
    
    if grade in range(92,99):
        print("A")
        
    if grade in range(90,92):
        print("A-")
        
    if grade in range(88,90):
        print("B+")
        
    if grade in range(82,89):
        print("B")
        
    if grade in range(80,82):
        print("B-")
        
    if grade in range(78,80):
        print("C+")
    
    if grade in range(72,78):
        print("C")
        
    if grade in range(70,72):
        print("C-")
        
    if grade in range(68,70):
        print("D+")
        
    if grade in range(62,68):
        print("D")
    
    if grade in range(60,62):
        print("D-")
        
    if grade in range(1,60):
        print("F")
    
    print("Would you like to input another grade? yes or no")
    again = input()

    if again.lower() != "yes":
        gate_keeper = False
    
'''
Create a list of dictionaries where each dictionary represents a book that you have read. 
Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.
'''

books = [
            {"Title":"Dune", "Auther":"Frank Hurbert", "Genre":"Science Fiction"}, 
            {"Title":"The Hobbit", "Auther":"J.R.R. Tolkien", "Genre":"Fantasy"},
            {"Title":"We", "Auther":"Yevgeny Zamyatin","Genre":"Science Fiction"}
        ]

for dictionary in books:
    for key,value in dictionary.items():
        print(key," >>> ",value)
    print("")

print("Please, select a Genre.")
request = input()

for dictionary in books:
    
    for key,value in dictionary.items():
        if value.lower() == request.lower():
            print("")
            
            for key,value in dictionary.items():
                if key.lower() == "Title".lower():
                    print(value)
            
           
