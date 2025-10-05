# bank_account.py
class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited ${amount}. New balance: ${self.account_balance}")

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds!")
            return False
        else:
            self.account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.account_balance}")
            return True

    def display_balance(self):
        print(f"Current account balance: ${self.account_balance}")
