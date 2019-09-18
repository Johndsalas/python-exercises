import json

application = "on"

print("                                             ")
print("                  (\___/)                    ")
print("                  (o\ /o)                    ")
print("                 /|:.V.:|\                   ")
print("                 \\\::::://                  ")
print("    ---------------\"\"-\"\"--------------   ")
print("~~~ Welcome to your terminal checkbook! ~~~")


while application == "on":

    
    print("")
    print("What would you like to do?")
    print("")
    print("1: view current balance")
    print("2: record a debit (withdraw)")
    print("3: record a credit (deposit)")
    print("4: quit application")
    
    choice = input()

    if choice != "1" and choice != "2" and choice != "3" and choice != "4":
        
        print("")
        print("Invalid entry. Please enter 1, 2, 3, or 4.")
        
    else:
        
        while choice == "1":
            
            with open('balance.txt', 'r') as b:
                b_contents = b.read()
                b_contents = float(b_contents)
                b_contents = "{:.2f}".format(b_contents)
            
            print("")
            print(f"Your current balance is ${b_contents}.")
          
            
            y_or_n = "unmade"
            
            while y_or_n != "n" and y_or_n != "y":
            
                print("")
                print("Would you like another tranaction? y/n")    

                y_or_n = input()
            
                if y_or_n == "n":
                    choice = "4"
                
                elif y_or_n == "y":
                    choice = "null"
                
                else:
                
                    print("")
                    print("Invalid entry. Plese type 'y' or 'n'.")
                    
        
        while choice == "2":
            
            with open('balance.txt', 'r') as b:
                b_contents = b.read()
                b_contents = float(b_contents)
                b_contents = "{:.2f}".format(b_contents)
    
                print("")
                print(f"Your current balance is ${b_contents}.")
                
            
            debit = "active"
            while debit == "active":
                
                print("")
                print("Amount to debit? (withdraw)")
                print("Please enter a dollor amount using only numbers and a decimal point.")
                
                
                withdraw = input()
              
                try: withdraw = float(withdraw)
                except: 
                    
                    print("")
                    print("Invalid entry.")
                    
                    continue
            
                new_balance = float(b_contents) - withdraw

                withdraw = "{:.2f}".format(withdraw)
                new_balance = "{:.2f}".format(new_balance)
            
                with open('balance.txt', 'w+') as b:
                
                    b.write(str(new_balance))   
                
                print("")
                print(f"You are withdrawing ${str(withdraw)}. Your current balance is now ${str(new_balance)}.")
                
                y_or_n = "unmade"
            
                while y_or_n != "n" and y_or_n != "y":
            
                    print("")
                    print("Would you like another transaction? y/n")    

                    y_or_n = input()
            
                    if y_or_n == "n":
                        debit = "inactive"
                        choice = "4"
                
                    elif y_or_n == "y":
                        debit = "inactive"
                        choice = "null"
                
                    else:
                
                        print("")
                        print("Invalid entry. Plese type 'y' or 'n'")
                        
    
        while choice == "3":
            
            with open('balance.txt', 'r') as b:
                b_contents = b.read()
    
            print("")
            print(f"Your current balance is ${b_contents}.")
            
            
            credit = "active"
            while credit == "active":
                
                print("")
                print("Amount to credit? (Deposit)")
                print("Please enter a dollor amount using only numbers and a decimal point.")
            
                deposit = input()
                
                try:deposit = float(deposit)
                except: 
                    
                    print("")
                    print("Invalid Entry.")
                    continue
                    
                new_balance = float(b_contents) + deposit

                deposit = "{:.2f}".format(deposit)
                new_balance = "{:.2f}".format(new_balance)
            
                with open('balance.txt', 'w+') as b:
                
                    b.write(str(new_balance))   
                
                print("")
                print(f"You are depositing ${str(deposit)}. Your current balance is now ${str(new_balance)}.")
                
                y_or_n = "unmade"
            
                while y_or_n != "n" and y_or_n != "y":
            
                    print("")
                    print("Would you like another transaction? y/n")    

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
                    
        if choice == "4":
            
            print("")
            print("Thank You! Have a Nice Day!")
            print("")
            application = "off"
            break
            

                
                