#Bank
from Account import *
import random

class Bank(): #Keeps track of all the accounts.
    def __init__(self, bankName):
        self.__bankName__ = bankName #Field variable for Bank.
        
        #A defined list/constructor of instances of SavingsAccount and ChequingAccount.
        self.accounts = [
            ChequingAccount("111", "John Doe", 0.02, 5000.0, 1000.0),
            ChequingAccount("222", "Jane Doe", 0.03, 3000.0, 2000.0),
            ChequingAccount("333", "Bob Smith", 0.01, 7000.0, 1500.0),
            SavingsAccount("444", "Alice Johnson", 0.05, 8000.0, 5000.0),
            SavingsAccount("555", "Charlie Brown", 0.04, 6000.0, 3000.0),
            SavingsAccount("666", "Eva Green", 0.02, 9000.0, 4500.0)]

    
    def searchAccount(self, accountNumber):
        for account in self.accounts:  #Iterates through each account in the list of accounts
            if accountNumber == account.__accountNumber__: #Checks if the provided accountNumber matches the account's accountNumber
                print("Found") #Prints a message indicating that the account is found
                print(accountNumber) #Print the account number for debugging or informational purposes.
                return account # Return the account object if a match is found.
        return None #If no matching account is found, returns None.
    ''' - Code I tried out, but didn't get running.
    def showInfo(self, accountNumber):
        accountInfo = [account.getAccountNumber, account.getAccountHolder, account.getcurrentBalance]
        return accountInfo
    
    def addAccount(self, account):
        return self.accounts.append(account)

    def createAccountNumber(self):
        return ''.join(str(random.randint(0, 10)) for _ in range(random.randint(11, 20)))

    def createAccount(self):
        self.addAccount(ChequingAccount(self.createAccountNumber(), 500, 1000))
        self.addAccount(ChequingAccount(self.createAccountNumber(), 5000, 1500))
        self.addAccount(ChequingAccount(self.createAccountNumber(), 1500, 5000))
        self.addAccount(SavingsAccount((self.createAccountNumber(), 10000, 5000)))
        self.addAccount(SavingsAccount(self.createAccountNumber(), 15000, 6000))
        self.addAccount(SavingsAccount(self.createAccountNumber(), 20000, 4000))'''

    def openAccount(self, accountType, accountNumber = None, accountHolderName = None, rateOfInterest = None, currentBalance = None, minimumBalance = None, overdraftLimit = None):
        accountNumber = random.randint(111111, 999999) #Creates an object that randomizes an account number.
        
        if accountType == "savings": #Creates an instance of Savings Account
            new_account = SavingsAccount(accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance)
        
        elif accountType == "chequing": #Creates an instance of Chequing Account
            new_account = ChequingAccount(accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftLimit)
        
        else: 
            print("Invalid account type. Only 'Savings' and 'Chequing' accounts are supported.")
            return 

        self.accounts.append(new_account) #Adds the account made through the account list/constructor in the intializer.
        print(f"Account opened successfully. Account number: {accountNumber}") #Prints the updated Account Number.



#b.searchAccount("111") - Testing an object of the class.