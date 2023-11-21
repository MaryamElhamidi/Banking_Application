#Bank
from Account import *
import random

class Bank():
    def __init__(self, bankName):
        self.__bankName__ = bankName
        self.accounts = []
    
    def searchAccount(self, accountNumber):
        for account in self.accounts:  
            if accountNumber == account.__accountNumber__:
                print("Found")
                print(accountNumber)
                return account
        return None
    
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
        self.addAccount(SavingsAccount(self.createAccountNumber(), 20000, 4000))

    def openAccount(self, accountType, accountNumber = None, accountHolderName = None, rateOfInterest = None, currentBalance = None, minimumBalance = None, overdraftLimit = None):
        accountNumber = random.randint(111111, 999999)
        
        if accountType.lower() == "Savings":
            new_account = SavingsAccount(accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance)
        
        elif accountType.lower() == "Chequing":
            new_account = ChequingAccount(accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftLimit)
        
        else:
            print("Invalid account type. Only 'Savings' and 'Chequing' accounts are supported.")
            return

        self.accounts.append(new_account)
        print(f"Account opened successfully. Account number: {accountNumber}")



#b.searchAccount("111")