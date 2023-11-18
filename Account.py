#Account

class Account():
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance):
        self.__accountNumber__ = accountNumber
        self.__accountHolderName__ = accountHolderName
        self.__rateOfInterest__ = rateOfInterest
        self.__currentBalance__ = currentBalance

    
    def getAccountNumber(self):
        return self.__accountNumber__
    def getAccountHolderName (self):
        return self.__accountHolderName__
    def getRateOfinterest(self):
        return self.__rateOfInterest__
    def getCurrentBalance(self):
        return self.__currentBalance__
    def setAccountHolderName(self, accountName):
        return self.__accountHolderName__ == accountName
    def setRateOfinterest(self, ROI):
        return self.__rateOfInterest__ == ROI
    
    def deposit(self, amount):
        if amount > 0:
            self.__currentBalance__ += amount
            print(f"Deposit successful. New balance: {self.__currentBalance__}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__currentBalance__:
            self.__currentBalance__ -= amount
            print(f"Withdrawal successful. New balance: {self.__currentBalance__}")
        else:
            print("Invalid withdrawal amount or insufficient funds. Withdrawal failed.")

    
#SavingsAccount
class SavingsAccount(Account): #requires the account holder(s) to maintain a minimum balance in the account
    def __init__(self,accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance):
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self.___minimumBalance__ = minimumBalance

    def withdraw(self, amount):
        max_withdrawl =  self.__currentBalance__ - self.___minimumBalance__
        if amount <= max_withdrawl:
            print(f"Withdrawal successful. Balance: {self.__currentBalance__}")
            print(f"Your Maximum withdrawl amount is now {max_withdrawl}")
            return True
        else:
            raise ValueError(f"Withdrawal failed. The maximum allowed withdrawal is {max_withdrawl} CAD.")
            return False


#ChequingAccount
class ChequingAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftLimit):
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self.__overdraftLimit__ = overdraftLimit

    def withdraw(self, amount):
        max_withdrawal = self.__currentBalance__ + self.__overdraftLimit__
        
        if amount <= max_withdrawal:
            print(f"Withdrawal successful. Your allowed overdraft withdrawl is: {max_withdrawal} CAD.")
            return True

        else:
            raise ValueError(f"Withdrawal failed. The maximum allowed withdrawal is {max_withdrawal} CAD.")
            return False
