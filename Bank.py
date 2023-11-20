#Bank
from Account import *
import random

class Bank():
    def __init__(self, bankName):
        self.__bankName__ = bankName
        self.accounts = [ChequingAccount("111", "John Doe", 0.02, 5000.0, 1000.0),
                         ChequingAccount("222", "Jane Doe", 0.03, 3000.0, 2000.0),
                         ChequingAccount("333", "Bob Smith", 0.01, 7000.0, 1500.0),
                         SavingsAccount("444", "Alice Johnson", 0.05, 8000.0, 5000.0),
                         SavingsAccount("555", "Charlie Brown", 0.04, 6000.0, 3000.0),
                         SavingsAccount("666", "Eva Green", 0.02, 9000.0, 4500.0)]
    
    def searchAccount(self, accountNumber):
        for account in self.accounts:  
            if accountNumber == account.__accountNumber__:
                print("Found")
                print(accountNumber)
                return account
        return None  # Account not found

    
    def openAccount(self, accountType, accountNumber = None, accountHolderName = None, rateOfInterest = None, currentBalance = None, minimumBalance = None, overdraftLimit = None):
        accountNumber = random.randint(111111, 999999)
        
        if accountType == "Savings":
            new_account = SavingsAccount(accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance)
        
        elif accountType == "Chequing":
            new_account = ChequingAccount(accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftLimit)
        else:
            print("Invalid account type. Only 'Savings' and 'Chequing' accounts are supported.")
            return

        self.accounts.append(new_account)
        print(f"Account opened successfully. Account number: {accountNumber}")



#b.searchAccount("111")