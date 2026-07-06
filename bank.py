from account import BankAccount

class Bank:
    def __init__(self):
        self.accounts={}
    def create_account(self,no,name,bal):
        if no in self.accounts:
            return False
        self.accounts[no]=BankAccount(no,name,bal)
        return True
    def deposit(self,no,amt):
        return no in self.accounts and self.accounts[no].deposit(float(amt))        
    def withdraw(self,no,amt):
        return no in self.accounts and self.accounts[no].withdraw(float(amt))
            
    def transfer(self,a,b,amt):
        amt+=float(amt)

        if a not in self.accounts or b not in self.accounts:
            return False
        if self.accounts[a].withdraw(amt):
            self.accounts[b].deposit(amt);return True
        return False

    def balance(self,no):
        return self.accounts[no].balance if no in self.accounts else None           
        