

print("welcome to notebook 2.0")

application = "on"

while application == "on":

print("what would you like to do?")
print("1: view balance")
print("2: record a debit/credit")
print("3: view previous transactions ")

choice = input()

#if choice == 1: veiw_balance()

if choice == 2: transaction()

#if choice == 3: history()

if choice == 4: 

    print("")
    print("Thank you! Have a nice day!")
    break

def transaction():

    print("")
    print("credit or debit?")
    print("1: credit")
    print("2: debit")

    num = input()

    if num == 1: typ = 'credit'
    elif num == 2: typ = 'debit'
    elif: transaction()
    
    print("")
    print(f"amount of {typ}?")
    print("Please enter a positive number amount with only numbers and one decimal point")

    change = input()

    print("enter a comment for this transaction")

    comment = input()

    













typ = "debit"

amount = 50

comment = "Electric Bill"

dictionary = {"type": typ, 'amount': amount, 'comment': comment}
   
with open('sample.txt', 'a') as s:

    s.write(str(dictionary) + "\n")