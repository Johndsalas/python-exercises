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

    if choice == "1" or "2" or "3" or "4":
        choice = int(input())

    if choice == "1":
        print("1")
        
    elif choice == "2":
        print("2")
    
    elif choice == "3":
        print("3")
    
    elif choice == "4":
        print(4)
        print("END DEMO")
        break

 '''       
        print("")
        print("")
        print("Thanks, have a great day!")
        break
        
        
        while choice == "1":
    
            print("")
            print(f"Your current balance is ${balance}.")
            print("")
            print("Would you like another tranaction? y/n")
            print("")
            print("")
            
            balance_choice = input()
            
            if balance_choice == n:
                choice = "4"
                
            if balance_choice == y:
                choice = "null"
                
            else:
                
                print("Invalid entry. Plese type 'y' or 'n'")
                
        
        while choice == "2":
            
            print("")
            print(f"Your current balance is ${balance}.")
            print("")
            print("Amount to debit? (withdraw)")
            
            withdraw = input()
            withdraw = int(withdraw)
            
            #subtract withdraw from balance
            
            print(f"You are withdrawing ${withdraw}. Your current balance is now ${balance}.)
            print("")
            print("")
            print("Would you like another tranaction? y/n")    

            debit_choice = input()
            
            if debit_choice == n:
                choice = "4"
                
            if debit_choice == y:
                choice = "null"
                
            else:
                
                print("Invalid entry. Plese type 'y' or 'n'")
            
        while choice == "3":
                
            print("")
            print(f"Your current balance is ${balance}.")
            print("")
            print("Amount to credit?")
            
            credit= input()
            credit= int(credit)
            
            #add to balance
            
            print(f"You are crediting ${credit}. Your current balance is now {balance}.)
            print("")
            print("")
            print("Would you like another tranaction? y/n")      
                
            credit_choice = input()
            
            if credit_choice == n:
                choice = "4"
                
            if debit_choice == y:
                choice = "null"
                
            else:
                
                print("Invalid entry. Plese type 'y' or 'n'")

        if choice == 4:

            print("Thank You, Have a nice day")