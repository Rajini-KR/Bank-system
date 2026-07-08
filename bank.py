from account import BankAccount


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, no, name, bal):
        if no in self.accounts:
            return False
        self.accounts[no] = BankAccount(no, name, bal)
        return True

    def deposit(self, no, amt):
        return no in self.accounts and self.accounts[no].deposit(amt)

    def withdraw(self, no, amt):
        return no in self.accounts and self.accounts[no].withdraw(amt)

    def transfer(self, f, t, amt):
        amt = float(amt)
        if f not in self.accounts or t not in self.accounts:
            return False

        if self.accounts[f].withdraw(amt):
            self.accounts[t].deposit(amt)
            return True
        return False

    def balance(self, no):
        return self.accounts[no].balance if no in self.accounts else None

    def get_all_accounts(self):
        return self.accounts.values()