class BankAccount:
    def __init__(self, full_name, account_numbers):
        self.full_name = full_name
        self.account_number = self.generate_account_number(account_numbers)
        self.balance = 0

    def generate_account_number(self, account_numbers):
        """Generates and assigns a random 8-digit account number to the account.
        Takes in a list of existing account numbers, and generates new account numbers until
        a unique account number (one not already in this list) is found"""
        random_account_number = 0
        return random_account_number

    def deposit(self, amount):
        """adds amount to the balance of the account"""
        self.balance += amount

    def withdraw(self, amount):
        """subtracts amount from the balance of the account. does not allow overdraft."""
        
    def get_balance(self):
        """prints and returns the current balance of the account"""

    def print_statement(self):
        """prints a statement message with account name, number, and balance"""
