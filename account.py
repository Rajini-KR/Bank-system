class BankAccount:
    def __init__(self, account_no, account_name, balance):
        self.account_no = account_no
        self.account_name = account_name
        self.balance = float(balance)

    def deposit(self, amount):
        amount = float(amount)
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True

    def get_details(self):
        return (self.account_no, self.account_name, self.balance)