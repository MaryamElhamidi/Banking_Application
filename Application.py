#Application
from Bank import Bank #Imports class Bank.
from Account import * #Imports all classes, and methods from the file Account using *.

class Application():
    my_bank = Bank("Maryam's Bank") # Class object of class bank.

    '''
    This function allows the user to enter the account number of the account they want to work with.
    Upon searching the account successfully, the application will call the method showAccountMenu to display the Account Menu as 
    described next. This method has a HAS-A relation with class Bank, which is why it is passed as a parameter.
    ''' 
    def showMainMenu(self):
        while True:
            print("Main Menu:") #Prints options 1, 2, and 3 of a Main Menu.
            print("1. Select Account")
            print("2. Open Account") #Bonus - Allows the user to open a new account.
            print("3. Exit")

            choice = input("Enter your choice: (Enter 1, 2, or 3): ") #Prompts the user to enter a choice.

            if choice == '1': #For
                try: #Error Handling for choice 1
                    account_number = int(input("Enter the account number: ")) #Prompts the user to enter an account number.
                    if(self.my_bank.searchAccount(account_number) == None): #If the user enters an account number that is not part of the pre-defined list of accounts it prompts them to create an account
                        print("Invalid account number. Please select the open a new account function.")
                    else: self.showAccountMenu(account_number)#Validates account number  #Runs and iteraties the showAccountMenu method using the user's input.
                except ValueError: #Raises value error
                    print("Account not found. Please try again.")
                    account_number = input("Enter the account number: ") #Prompts the user to enter another valid account number.


            elif choice == '2':
                print("Welcome to Opening an Account")
                accountType = input("Would you like to open a Savings Account or Chequings Account: ") #Prompts the user to make a savings or chequings account.
                accountType.lower() #Takes the user input, and uses the lower() method to ensure the user's input is passed.
                if accountType == "savings":
                    account_minimum_balance = int(input("Enter minimum balance:"))
                    account_overdraft_limit = 0

                elif accountType == "chequing":
                    account_overdraft_limit = int(input("Enter the overdraft limit: "))
                    account_minimum_balance = 0

                account_holder_name = input("Enter the account holder name:")
                account_current_balance = int(input("Enter the current balanceble to open an account: "))
                rate_of_interest = int(input("Enter the rate of interest of the account: "))
                
                try: #Error Handling for choice 2
                    self.my_bank.openAccount(accountType,0,account_holder_name,rate_of_interest,account_current_balance,account_minimum_balance,account_overdraft_limit) #Opens an account. Uses the users input, and passes it through as a parameter for the method function "Open Account" of class Bank.

                except ValueError: #Raises value error is user does not enter the option of savings or chequing account.
                    print('The account you are trying to make is not possible. Only savings and chequings is allowed.')
                except RuntimeError: #Handles error through runtime error, because the balance is seperate from user interaction.
                    print("Sorry, Our systems are down, can't open an account currently") #Displays that the system is unable to open an account.
                
            elif choice == '3':
                print("Exiting the application. Goodbye!") 
                break #Exists the loop.

            else:
                print("Invalid choice. Please enter a valid option.") #Displays that the user made a wrong choice. Loop will continue iterating and asking the user to re-enter a valid option. 


    def showAccountMenu(self, account_number): #A method that loops to display different options to the user until the user chooses to exit the Account Menu.
        while True:
            print("\nAccount Menu:") #Prints a new line with the Account Menu options.
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit Account")
        
            choice = input("Enter your choice: ") #Prompts user to make a choice.
            
            if choice == '1':
                try: #Error Handling for choice 1
                    balance = self.my_bank.searchAccount(account_number).getCurrentBalance() #Creates an object, and accesses the getter from class 'Account' through the search account function.
                    print(f"Balance: {balance}") #Prints the updated balance.
                except RuntimeError: #Handles error through runtime error, because the balance is seperate from user interaction. 
                    print("Unable to find Balance.") #Displays that the balance is not accessable.

            elif choice == '2': #Prompt the user for an amount to deposit and perform the deposit using the methods in account class.
                try: #Error Handling for choice 2
                    amount = float(input("Enter the amount to deposit: ")) #Prompts the user to enter desired deposited amount
                    #self.my_bank.searchAccount(account_number).__currentBalance__ += amount #Updates the Current Balance field variable with the users input.
                    #if amount > 0:  #Validates that the user input is a greater than zero
                    self.my_bank.searchAccount(account_number).deposit(amount) #Accesses and uses the deposit function in class 'Account' using the user's desired input.
                    #print('Successful Deposit has been made.') 

                except ValueError:
                    print("Invalid input. Please enter a valid number, greater than 0.") #Displays to the user the value is incorrect.
                    amount = float(input("Enter the amount to deposit: ")) #Prompts the user to enter desired deposited amount

            elif choice == '3': #Prompt the user for an amount to withdraw and perform the withdrawal using the methods in the account class. 
                try: #Error Handling for choice 3
                    amount = float(input("Enter the amount to withdraw: ")) #Prompts the user to enter desired withdrawl amount
                    if amount > 0:  #Validates that the user input is a greater than zero
                        self.my_bank.searchAccount(account_number).withdraw(amount) #Accesses the withdraw method in class account using the users input.
                    else:
                        print("Invalid amount. Please enter a positive value.") #If the number is not greater than 0 and not an integer, it prompts the user to enter again, with instructions stating that it must be an integer.
                        amount = float(input("Enter the amount to withdraw: ")) #Prompts the user to enter desired withdrawl amount
                except ValueError: #Raises a value error
                    print("Invalid input. Please enter a valid number.") #Displays to the user the value is incorrect.
                    amount = float(input("Enter the amount to withdraw: ")) #Prompts the user to enter desired withdrawl amount
            elif choice == '4': 
                print("Exiting Account Menu.") #Displays Goodbye Message
                break #Breaks and exits the loop. No error handling further here due to exiting menu.

            else:
                print("Invalid choice. Please enter a valid option.") #Displays that the user made a wrong choice. Loop will continue iterating and asking the user to re-enter a valid option. 




#b = Bank("Maryam's Bank") #An object of class Bank.
a = Application() #An object of class Application.
a.showMainMenu() #Passes through Application class, and iterates/runs the loop using the object of the class Bank.