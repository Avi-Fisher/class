class Bank_account():

    def __init__(self,account_holder:str,initial_balance:int):

        self.holder = account_holder
        self.balance = initial_balance


    def transfer_funds(self,other_account,amount):

        if amount <= self.balance:

            self.balance = self.balance - amount
            other_account.balance += amount

            print("The transfer was successful")

        else:
            print("You dont have money")


    def __str__(self):
        return f"{self.holder} welcome to your account \n \n you have {self.balance} in your account \n     goodbye"

