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
    def withdraw():
        return
    
#SavingsAccount

class SavingsAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance):
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self.___minimumBalance__ = minimumBalance

    def withdraw():
        return
    
#ChequingAccount

class ChequingAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftLimit):
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self.__overdraftLimit__ = overdraftLimit

    def withdraw():
        return