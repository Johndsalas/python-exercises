
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

