# Account balancecheck
class BankAccount:
    def __init__(self,initial_balance=0):
       self.account_balance=initial_balance
    def deposit(self,amount):          
            self.account_balance=self.account_balance+amount
            print(f"You deposited ${amount}.New balance: ${self.account_balance}")
    def withdraw(self,amount):
            self.amount=amount
            if amount>self.account_balance:
                return False
            else:
                self.account_balance= self.account_balance-amount
                print(f" The action of withdraw ${amount}. is successfull! your New balance is ${self.account_balance}")
                return True
    def display_balance(self):
            print(f"The current account balance: ${self.account_balance}")
account= BankAccount(100)
account.deposit(50)
account.withdraw(30)
account.display_balance()

                
            
    
        