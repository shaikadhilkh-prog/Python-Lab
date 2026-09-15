class BankAccount:
    def __init__(self, account_number, holder_name, account_type, initial_balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.account_type = account_type
        self.balance = float(initial_balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"[+] Deposited: ${amount:.2f} | New balance: ${self.balance:.2f}")
        else:
            print("[!] Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("[!] Error: Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(f"[!] Transaction Declined: Insufficient funds. Current balance is ${self.balance:.2f}.")
        else:
            self.balance -= amount
            print(f"[-] Withdrew: ${amount:.2f} | Remaining balance: ${self.balance:.2f}.")

    def display_account_details(self):
        print("\n" + "="*35)
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.holder_name}")
        print(f"Account Type: {self.account_type}")
        print(f"Current Balance: ${self.balance:.2f}")
        print("="*35)

print("---Instantiating Account 1---")
acc1 = BankAccount("10012024", "Adhil", "Savings", 500.00)
acc1.display_account_details()

acc1.deposit(150.75)
acc1.withdraw(200.00)
acc1.withdraw(600.00)  

print("\n---Instantiating Account 2---")
acc2 = BankAccount("10012025", "Hashim", "Current", 50.00)
acc2.display_account_details()
acc2.deposit(1000.00)