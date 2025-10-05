# bank_account.py
class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance  # return new balance for testing

    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return True  # return True to indicate success

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
