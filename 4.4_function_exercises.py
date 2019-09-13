#Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(input):

    if input in(2,"2"):
        return True

    else: return False

input = "3"

is_two(input)


#Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(vowel):

    if vowel.lower() in("a","e","i","o","u"):
        return True

    else: return False

vowel = "12"

is_vowel(vowel)



#Define a function named is_consonant. 
# It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.

def is_consonant(letter):

    if len(letter) == 1 and letter.isalpha() == True and letter.lower() not in("a","e","i","o","u"):
        return True
        
    else: return False

vowel = "c"

is_consonant(vowel)

#Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.

def capitalize_if_consonant(word):

    if word[0:1] not in ("a","e","i","o","u"):
        word = word.capitalize()
        
    return word


word = "anogram"
capitalize_if_consonant(word)

#Define a function named calculate_tip. 
#It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip_percentage,bill):

    return bill * tip_percentage

tip_percentage = .15
bill = 30

calculate_tip(tip_percentage,bill)

#Define a function named apply_discount. 
# It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(original_price,discount_percentage):

    discount_amount = original_price * discount_percentage

    total = original_price - discount_amount

    return total

original_price = 100
discount_percentage = .15


apply_discount(original_price,discount_percentage)

#Define a function named handle_commas. 
# It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handdle_commas(number):

    return number.replace(",", "")

number = ",,,45,67,89,,,"
handdle_commas(number)

#Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(grade):

    if grade in range(99,101):
        return "A+"
    
    if grade in range(92,99):
        return "A"
        
    if grade in range(90,92):
        return "A-"
        
    if grade in range(88,90):
        return "B+"
        
    if grade in range(82,89):
        return "B"
        
    if grade in range(80,82):
        return "B-"
        
    if grade in range(78,80):
        return "C+"
    
    if grade in range(72,78):
        return "C"
        
    if grade in range(70,72):
        return "C-"
        
    if grade in range(68,70):
        return "D+"
        
    if grade in range(62,68):
        return "D"
    
    if grade in range(60,62):
        return "D-"
        
    if grade in range(1,60):
        return "F"

grade = 99
get_letter_grade(grade)

#Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.



def remove_vowels(word):

    return word.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")


word = "Yaba daba do aeiou"
remove_vowels(word)

#Define a function named normalize_name. 
# It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be rec  cmoved
#leading and trailing whitespace should be removed
#everything should be lowercase
#spaces should be replaced with underscores
#for example:
#Name will become name
#First Name will become first_name
#% Completed will become completed

def normalize_name(input):

    for symbol in input:
        
        if symbol.isalpha() == False and symbol.isdigit() == False and symbol != " ":

            input = input.replace(symbol, "")

    input = input.strip().lower().replace(" ", "_")

    return input


input = " ^&*()    V@#$a@$lid PyT%^&%#&hOn ide@$%ntif@#ier  $#%^$^   "

normalize_name(input)

'''
Write a function named cumsum that accepts a list of numbers 
and returns a list that is the cumulative sum of the numbers in the list.
cumsum([1, 1, 1]) returns [1, 2, 3]
cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]
'''

def cumsum(number_list):

    sum_list = []
    current_sum = 0

    for number in number_list:

        current_sum += number
        sum_list.append(current_sum)

    return sum_list

number_list =[1,1,1,1,1,1,1,1,1,1,1,1]
cumsum(number_list)

'''
Bonus
Create a function named twelveto24. 
It should accept a string in the format 10:45am or 4:30pm 
and return a string that is the representation of the time in a 24-hour format. 
'''

def twelveto24(time):

    if time[-2:] == "am" and time[:2] == "12": 
        return "00" + time[2:-2] 
             
    elif time[-2:] == "am": 
        return time[:-2] 
      
    
    elif time[-2:] == "am" and time[:2] == "12": 
        return time[:-2] 
          
    else: 
        return str(int(time[:2]) + 12) + time[2:5] 

time = "10:45pm"

twelveto24(time)

'''
Bonus write a function that does the opposite.
'''
def reverse_time(time):

    if int(time[:2]) >= 12:

        hour = time[:2]
        hour = int(hour)        
        hour -= 12
        hour = str(hour)

        return hour + time[2:] + "pm"

    else:

        return time + "am"

time = "23:56"

reverse_time(time)


'''
Create a function named col_index. 
It should accept a spreadsheet column name, and return the index number of the column.
col_index('A') returns 1
col_index('B') returns 2
col_index('AA') returns 27
'''

def col_index(column_name):

    index = 0

    index += (len(column_name)-1) * 26

    column_name[len(column_name):]

    if column_name[len(column_name)-1:] == "A": index += 1
    if column_name[len(column_name)-1:] == "B": index += 2
    if column_name[len(column_name)-1:] == "C": index += 3
    if column_name[len(column_name)-1:] == "D": index += 4
    if column_name[len(column_name)-1:] == "E": index += 5
    if column_name[len(column_name)-1:] == "F": index += 6
    if column_name[len(column_name)-1:] == "G": index += 7
    if column_name[len(column_name)-1:] == "H": index += 8
    if column_name[len(column_name)-1:] == "i": index += 9
    if column_name[len(column_name)-1:] == "J": index += 10
    if column_name[len(column_name)-1:] == "K": index += 11
    if column_name[len(column_name)-1:] == "L": index += 12
    if column_name[len(column_name)-1:] == "M": index += 13
    if column_name[len(column_name)-1:] == "N": index += 14
    if column_name[len(column_name)-1:] == "O": index += 15
    if column_name[len(column_name)-1:] == "P": index += 16
    if column_name[len(column_name)-1:] == "Q": index += 17
    if column_name[len(column_name)-1:] == "R": index += 18
    if column_name[len(column_name)-1:] == "S": index += 19
    if column_name[len(column_name)-1:] == "T": index += 20
    if column_name[len(column_name)-1:] == "U": index += 21
    if column_name[len(column_name)-1:] == "v": index += 22
    if column_name[len(column_name)-1:] == "v": index += 23
    if column_name[len(column_name)-1:] == "X": index += 24
    if column_name[len(column_name)-1:] == "Y": index += 25
    if column_name[len(column_name)-1:] == "Z": index += 26

    return index

column_name = "BB"

col_index(column_name)




