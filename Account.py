#Account
class Account():
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance):
        self.__accountNumber__ = accountNumber
        self.__accountHolderName__ = accountHolderName
        self.__rateOfInterest__ = rateOfInterest 
        self.__currentBalance__ = currentBalance

    
    def getAccountNumber(self): #Gets the Account Number
        return self.__accountNumber__ #Returns the account number
    def getAccountHolderName (self): #Gets the Account Holder Name
        return self.__accountHolderName__ #Returns the Name
    def getRateOfinterest(self): #Gets the Rate of Interest
        return self.__rateOfInterest__ #Returns the ROI
    def getCurrentBalance(self): #Gets the Current Balance
        return self.__currentBalance__ #Returns the balance
    def setAccountHolderName(self, accountName):#Sets the user's name, by using and passing the accountName as a parameter
        self.__accountHolderName__ = accountName #Updates the field variable for accountName
    def setRateOfinterest(self, rateOfInterest): #Sets the user's name, by using and passing the rateOfInterest as a parameter
        self.__rateOfInterest__ = rateOfInterest #Updates the field variable for rateOfInterest
    
    def deposit(self, amount): 
        if amount > 0:
            self.__currentBalance__ += amount
            print(f"Deposit successful. New balance: {self.__currentBalance__}")
            return True
        else:
            print("Invalid deposit amount. Please enter a positive value.")
            return False

    def withdraw(self, amount): #Uses 'amount', prompted by the user, to withdraw and perform the withdrawal function. 
        if amount > 0 and amount <= self.__currentBalance__:
            self.__currentBalance__ -= amount
            print(f"Withdrawal successful. New balance: {self.__currentBalance__}")
            return True
        else:
            print("Invalid withdrawal amount or insufficient funds. Withdrawal failed.")
            return False

    
#SavingsAccount
class SavingsAccount(Account): #requires the account holder(s) to maintain a minimum balance in the account
    def __init__(self,accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance): #Created SavingsAccount class that takes the attributes from the 'Account' Class, and empty base variables for the Application class to use in future methods. This is a IS-A relationship between classes.

        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self.___minimumBalance__ = minimumBalance #Minimum Balance field Variable

    def withdraw(self, amount):
        max_withdrawl =  self.__currentBalance__ - self.___minimumBalance__ #Calculates and stores the maximum withdrawl amount.
        if amount <= max_withdrawl: 
            print(f"Withdrawal successful. Balance: {self.__currentBalance__}") #Prints the current balance.
            print(f"Your Maximum withdrawl amount is now {max_withdrawl}") #Prints the updated maximum withdrawl amount.
            return True
        else:
            raise ValueError(f"Withdrawal failed. The maximum allowed withdrawal is {max_withdrawl} CAD.") #Raises Value error and prints what is expected.


#ChequingAccount
class ChequingAccount(Account): #Created ChequingAccount class that takes the attributes from the 'Account' Class, and empty base variables for the Application class to use in future methods. This is a IS-A relationship between classes.
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftLimit):
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance) #Uses the attributes and hard copies them from class 'Account'
        self.__overdraftLimit__ = overdraftLimit #Overdraft field Variable

    def withdraw(self, amount):
        max_withdrawal = self.__currentBalance__ + self.__overdraftLimit__ #Calculates and stores the maximum withdrawl amount
        

        if amount > 0 and amount <= max_withdrawal: #If the amount is greater than 0, and is greater than or equal to 0, the loop calculates and updates the current balance.
            self.__currentBalance__ -= amount #Updates the current balance to the new amount.
            print(f"Withdrawal successful. Your allowed overdraft withdrawl is: {max_withdrawal} CAD.") #Prints the results
            return True #Returns True, for future refrences.

        else:
            raise ValueError(f"Withdrawal failed. The maximum allowed withdrawal is {max_withdrawal} CAD.") #Raises Value error and prints what is expected.



