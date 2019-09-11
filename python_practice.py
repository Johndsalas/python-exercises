type(99.9)
type("False")
type(False)
type('0')
type(0)
type(True)
type('True')
type([{}])
type({'a': []})
'''
Predictions!!!!!

What data type would best represent:

A term or phrase typed into a search box?

string

If a user is logged in?

bool

A discount amount to apply to a user's shopping cart?

float

Whether or not a coupon code is valid?

bool

An email address typed into a registration form?

string

The price of a product?

float

A Matrix?

list or dict

The email addresses collected from a registration form?

string

Information about applicants to Codeup's data science program?

string

'1' + 2 

error

6 % 4

2

type(6 % 4)

int

type(type(6 % 4))

type

'3 + 4 is ' + 3 + 4

error

0 < 0

False

'False' == False

error

True == 'True'

error

5 >= -5

True

!False or False

True

True or "42"

error

!True && !False

False

6 % 5

1

5 < 4 and 1 == 1

False

'codeup' == 'codeup' and 'codeup' == 'Codeup'

False

4 >= 0 and 1 !== '1'

error

6 % 3 == 0

True

5 % 2 != 0

True

[1] + 2

[3]

[1] + [2]

error

[1] * 2

[2]

[1] * [2]

error

[] + [] == []

True

{} + {}

return empty dict

Results!!!!!!!!!!!!

>>> '1' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> 6 % 4
2
>>> type(6 % 4)
<class 'int'>
>>> type(type(6 % 4))
<class 'type'>
>>> '3 + 4 is ' + 3 + 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> 0 < 0
False
>>> 'False' == False
False
>>> True == 'True'
False
>>> 5 >= -5
True
>>> !False or False
  File "<stdin>", line 1
    !False or False
    ^
SyntaxError: invalid syntax
>>> True or "42"
True
>>> !True && !False
  File "<stdin>", line 1
    !True && !False
    ^
SyntaxError: invalid syntax
>>> 6 % 5
1
>>> 5 < 4 and 1 == 1
False
>>> 'codeup' == 'codeup' and 'codeup' == 'Codeup'
False
>>> 4 >= 0 and 1 !== '1'
  File "<stdin>", line 1
    4 >= 0 and 1 !== '1'
                   ^
SyntaxError: invalid syntax
>>> 6 % 3 == 0
True
>>> 5 % 2 != 0
True
>>> [1] + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "int") to list
>>> [1] + [2]
[1, 2]
>>> [1] * 2
[1, 1]
>>> [1] * [2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'list'
>>> [] + [] == []
True
>>> {} + {}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

Write some Python code, that is, variables and operators, to describe the following scenarios. Do not worry about the real operations to get the values, the goal of these exercises is to understand how real world conditions can be represented with code.

You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?

def rent_amount():

    the_little_mermaid = 3
    brother_bare = 5
    hercules = 1

    return (the_little_mermaid + brother_bare + hercules) * 3

Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

def pay_day():

    google = 400 * 6
    amazon = 380 * 4
    facebook = 350 * 10

    return google + amazon + facebook

A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

def can_enroll(enrollment,planning):

    class = enrollment
    class_schedule = planning

    if (class != "full") and (class_scudule != "Conflicted"):
        student = "can enroll"
    else:
        student = "can_not_enroll"
    
    return student

A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

def product_offer(customer,items,offer):

    if (items > 2) or (customer = "Premium") or (offer = "expired"):
        status = "Can Be Applied"
    
    else:
        status = "Cannot Be Applied"

    return status

Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'

Create a variable that holds a boolean value for each of the following conditions:

the password must be at least 5 characters

five_or_grater = len(password) >= 5

the username must be no more than 20 characters

twenty_or_less = len(username) <=  20

the password must not be the same as the username

no_match = password != username

bonus neither the username or password can start or end with whitespace

no_whitespace = (username == username.strip()) and (password == password.strip())

'''
