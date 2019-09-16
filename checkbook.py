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

    if choice == "1" or "2" or "3" or "4":
        choice = int(input())

    if choice == "1":
        balance == "on"
        
    elif choice == "2":
        debit == "on"
    
    elif choice == "3":
        credit == "on"
    
    elif choice == "4":
        
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
            print("How much are you withdrawing?")
            
            withdraw = input()
            withdraw = int(withdraw)
            
            #subtract withdraw from balance
            
            print(f"You are withdrawing ${withdraw}. Your current balance is now {balance}.)
            print("")
            print("")
            print("Would you like another tranaction? y/n")      
            
        while choice == "3":
                
            print("")
            print(f"Your current balance is ${balance}.")
            print("")
            print("How much are you withdrawing?")
            
            withdraw = input()
            withdraw = int(withdraw)
            
            #subtract withdraw from balance
            
            print(f"You are withdrawing ${withdraw}. Your current balance is now {balance}.)
            print("")
            print("")
            print("Would you like another tranaction? y/n")      
                