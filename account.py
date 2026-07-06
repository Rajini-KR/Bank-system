class BankAccount:
    def __init__(self,account_number,account_name,balance):
        self.account_number=account_number
        self.account_name=account_name
        self.balance=balance

    def deposit(self,amt):
        if amt<0:
            return False
        self.balance+=amt
        return True

    def withdraw(self,amt):
        if amt<0 or amt>self.balance:
            return False
        self.balance-=amt
        return True

    def get_details():
        return(self.account_number,self.account_name,self.balance)