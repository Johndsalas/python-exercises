import json

application = "on"

print("~~~ Welcome to your terminal checkbook! ~~~")


while application == "on":

    print("")
    print("")
    print("What would you like to do?")
    print("")
    print("1: View Balance")
    print("2: Record a Debit (Withdraw)")
    print("3: Record a Credit (Deposit)")
    print("4: Quit Application")
    print("")
    choice = input()

    if choice != "1" and choice != "2" and choice != "3" and choice != "4":
        
        print("Please enter 1, 2, 3, or 4.")
        
    else:
        
        while choice == "1":
            
            with open('balance.txt', 'r') as b:
                b_contents = b.read()
            
            print("")
            print(f"Your current balance is ${b_contents}.")
            print("")
            print("")
            
            y_or_n = "unmade"
            
            while y_or_n != "n" and y_or_n != "y":
            
                print("Would you like another tranaction? y/n")    

                y_or_n = input()
            
                if y_or_n == "n":
                    choice = "4"
                
                elif y_or_n == "y":
                    choice = "null"
                
                else:
                
                    print("")
                    print("Invalid entry. Plese type 'y' or 'n'")
                    print("")
        
        while choice == "2":
            
            with open('balance.txt', 'r') as b:
                b_contents = b.read()
    
            print("")
            print(f"Your current balance is ${b_contents}.")
            print("")
            print("Amount to debit? (withdraw)")
            
            withdraw = input()
            withdraw = float(withdraw)
            
            new_balance = float(b_contents) - withdraw
            
            with open('balance.txt', 'w+') as b:
                
                b.write(str(new_balance))   
                
            print(f"You are withdrawing ${str(withdraw)}. Your current balance is now ${str(new_balance)}.")
            print("")
            print("")
            y_or_n = "unmade"
            
            while y_or_n != "n" and y_or_n != "y":
            
                print("Would you like another tranaction? y/n")    

                y_or_n = input()
            
                if y_or_n == "n":
                    choice = "4"
                
                elif y_or_n == "y":
                    choice = "null"
                
                else:
                
                    print("")
                    print("Invalid entry. Plese type 'y' or 'n'")
                    print("")
    
        while choice == "3":
            
            with open('balance.txt', 'r') as b:
                b_contents = b.read()
    
            print("")
            print(f"Your current balance is ${b_contents}.")
            print("")
            
            credit = "active"
            while credit == "active":
                
                print("Amount to credit? (Deposit)")
            
                deposit = input()
                
                try:deposit = float(deposit)
                except: continue
                    
                new_balance = float(b_contents) + deposit
            
                with open('balance.txt', 'w+') as b:
                
                    b.write(str(new_balance))   
                
                print(f"You are depositing ${str(deposit)}. Your current balance is now ${str(new_balance)}.")
                print("")
                print("")
            
                y_or_n = "unmade"
            
                while y_or_n != "n" and y_or_n != "y":
            
                    print("Would you like another tranaction? y/n")    

                    y_or_n = input()
            
                    if y_or_n == "n":
                        credit = "inactive"
                        choice = "4"
                
                    elif y_or_n == "y":
                        credit = "inactive"
                        choice = "null"
                
                    else:
                
                        print("")
                        print("Invalid entry. Plese type 'y' or 'n'")
                        print("")
    
    
        if choice == "4":
            print("")
            print("Thank You! Have a Nice Day!")
            application = "off"
            break
            
