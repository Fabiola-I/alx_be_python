import unittest
from bank_account import BankAccount
from io import StringIO
import sys

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # This runs before each test
        self.account = BankAccount(100)  # Start with $100

    def test_display_balance(self):
        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output
        self.account.display_balance()
        sys.stdout = sys.__stdout__
        self.assertIn("Current account balance: $100", captured_output.getvalue())

    def test_deposit(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.account.deposit(50)
        sys.stdout = sys.__stdout__
        self.assertEqual(self.account.account_balance, 150)
        self.assertIn("Deposited $50. New balance: $150", captured_output.getvalue())

    def test_withdraw(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        result = self.account.withdraw(40)
        sys.stdout = sys.__stdout__
        self.assertTrue(result)
        self.assertEqual(self.account.account_balance, 60)
        self.assertIn("Withdrew $40. New balance: $60", captured_output.getvalue())

    def test_withdraw_more_than_balance(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        result = self.account.withdraw(200)
        sys.stdout = sys.__stdout__
        self.assertFalse(result)
        self.assertEqual(self.account.account_balance, 100)
        self.assertIn("Insufficient funds!", captured_output.getvalue())

    def test_display_balance_after_transactions(self):
        # Perform deposit and withdrawal
        self.account.deposit(50)
        self.account.withdraw(30)
        captured_output = StringIO()
        sys.stdout = captured_output
        self.account.display_balance()
        sys.stdout = sys.__stdout__
        self.assertIn("Current account balance: $120", captured_output.getvalue())

if __name__ == "__main__":
    unittest.main()
