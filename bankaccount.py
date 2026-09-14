class BankAccount:
    def __init__(self, account_number, holder_name, account_type, initial_balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.account_type = account_type
        self.balance = float(initial_balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}"