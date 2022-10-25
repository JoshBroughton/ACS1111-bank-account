from random import randint

class BankAccount:
    def __init__(self, full_name, account_numbers, overdraft_fee=10):
        self.full_name = full_name
        self.account_number = self.generate_account_number(account_numbers)
        self.balance = 0
        self.overdraft_fee = overdraft_fee

    def generate_account_number(self, account_numbers):
        """Generates and assigns a random 8-digit account number to the account.
        Takes in a list of existing account numbers, and generates new account numbers until
        a unique account number (one not already in this list) is found"""
        unique_account_number = False
        while not unique_account_number:
            new_account_number = randint(10000000, 99999999)
            if new_account_number in account_numbers:
                unique_account_number = False
            else:
                unique_account_number = True
                return new_account_number

    def deposit(self, amount):
        """adds amount to the balance of the account, and prints a confirmation message"""
        if type(amount) is int or type(amount) is float:
            self.balance += amount
            print(f'Amount deposited: ${amount} New Balance: ${self.balance}')
        else:
            print('Please enter a valid numeric entry for the amount to deposit.')

    def withdraw(self, amount):
        """subtracts amount from the balance of the account. Does not allow withdrawal to negatives,
        and charges a $10 overdraft fee if an attempt is made to do so."""
        if type(amount) is int or type(amount) is float:
            balance = self.balance - amount
            if balance > 0:
                self.balance = balance
                print(f'Amount withdrawn: ${amount} New balance: ${balance}')
            else:
                self.balance -= self.overdraft_fee
                print(f'Insufficient funds. ${self.overdraft_fee} overdraft fee charged.')

        
    def get_balance(self):
        """prints and returns the current balance of the account"""

    def print_statement(self):
        """prints a statement message with account name, number, and balance"""
