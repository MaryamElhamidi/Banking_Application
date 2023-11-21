#Application
from Bank import Bank
from Account import *

class Application():

    def showMainMenu(self, Bank):
        while True:
            print("Main Menu:")
            print("1. Select Account")
            print("2. Open Account (Bonus - To be implemented)")
            print("3. Exit")

            choice = input("Enter your choice: (Enter 1, 2, or 3): ")

            if choice == '1':
                try:
                    account_number = input("Enter the account number: ")

                    if account_number:
                        self.showAccountMenu(account_number)
                except ValueError:
                    print("Account not found. Please try again.")
                    account_number = input("Enter the account number: ")


            elif choice == '2':
                print("Welcome to Opening an Account")
                accountType = input("Would you like to open a Savings Account or Chequings Account: ")
                try:
                    Bank.openAccount(accountType)

                except ValueError:
                    print("Sorry, the option you have entered is incorrect or does not exist")
                
            elif choice == '3':
                print("Exiting the application. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a valid option.")
                break


    def showAccountMenu(self, account_number):
        while True:
            print("\nAccount Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit Account")

            choice = input("Enter your choice: ")

            if choice == '1':
                balance = Account.getCurrentBalance()
                print(f"Balance: {balance}")

            elif choice == '2':
                try:
                    amount = float(input("Enter the amount to deposit: "))
                    self.__currentBalance__ += amount
                    if amount > 0:
                        Account.deposit(amount)
                        print('Successful Deposit has been made.')
                    else:
                        print("Failed Deposit. Invalid amount. Please enter a positive value.")
                        amount = float(input("Enter the amount to deposit: "))

                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            elif choice == '3':
                try:
                    amount = float(input("Enter the amount to withdraw: "))
                    if amount > 0:
                        Account.withdraw(amount)
                    else:
                        print("Invalid amount. Please enter a positive value.")

                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            elif choice == '4':
                print("Exiting Account Menu.")
                break

            else:
                print("Invalid choice. Please enter a valid option.")




b = Bank("Maryam's Bank")
a = Application()
a.showMainMenu(b)