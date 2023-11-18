#Bank
from Account import SavingsAccount
from Account import ChequingAccount
from Account import Account


class Bank:
    def __init__(self, bankName):
        self.__bankName__ = bankName
        self.accounts = []
    
    def searchAccount():
        for account in accounts:  
            if accountNumber == getAcountNumber:
                return account
        return None  # Account not found

    def openAccount(self, accountType, accountNumber, currentBalance, minimumBalance = None, overdraftLimit = None):
        if accountType == "Savings":
            new_account = SavingsAccount(accountNumber, currentBalance, minimumBalance)
        elif accountType == "Chequing":
            new_account = ChequingAccount(accountNumber, currentBalance, overdraftLimit)
        else:
            print("Invalid account type. Only 'Savings' and 'Chequing' accounts are supported.")
            return

        self.accounts.append(new_account)
        print(f"Account opened successfully. Account number: {accountNumber}")