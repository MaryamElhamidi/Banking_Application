#Account

class Account:
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance):
        self.__accountNumber__ = accountNumber
        self.__accountHolderName__ = accountHolderName
        self.__rateOfInterest__ = rateOfInterest
        self.__currentBalance__ = currentBalance

    
    def getAcountNumber():
        return
    def getAccountHolderName ():
        return
    def getRateOfinterest():
        return
    def getCurrentBalance():
        return
    def setAccountHolderName():
        return
    def setRateOfinterest():
        return
    def deposit():
        return
    def withdraw(self):
        return
    
#SavingsAccount
class SavingsAccount(Account): #requires the account holder(s) to maintain a minimum balance in the account
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance):
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self.___minimumBalance__ = minimumBalance

    def withdraw(self, amount):
        max_withdrawl =  self.__currentBalance__ - self.___minimumBalance__
        if amount <= max_withdrawl:
            print(f"Withdrawal successful. Balance: {self.__currentBalance__}")
            print(f"Your Maximum withdrawl amount is now {max_withdrawl}")
        else:
            print(f"Withdrawal failed. The maximum allowed withdrawal is {max_withdrawl} CAD.")
    


#ChequingAccount
class ChequingAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftLimit):
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self.__overdraftLimit__ = overdraftLimit

    def withdraw(self, amount):
        max_withdrawal = self.__currentBalance__ + self.__overdraftLimit__
        
        if amount <= max_withdrawal:
            print(f"Withdrawal successful. Your allowed overdraft withdrawl is: {max_withdrawal} CAD.")

        else:
            raise ValueError(f"Withdrawal failed. The maximum allowed withdrawal is {max_withdrawal} CAD.")
