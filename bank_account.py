"""bank_account.py defines classes for BankAccount and Bank objects, incluidng common
banking operations"""
from random import randint

class BankAccount:
    """Defines a BankAccount class, which represents a generic bank account. Includes
    attributes for full name of account holder, account number, and balance. Includes
    methods to generate a random account number, assign a manual account number,
    deposit, withdraw, and view a statement of account."""
    def __init__(self, full_name, account_numbers, is_savings_account=False, overdraft_fee=10):
        self.full_name = full_name
        self.account_number = self.generate_account_number(account_numbers)
        self.balance = 0
        self.overdraft_fee = overdraft_fee
        self.is_savings_account = is_savings_account
        self.interest_rate = self.set_interest_rate()

    def generate_account_number(self, account_numbers):
        """Generates and assigns a random 8-digit account number to the account.
        Takes in a list of existing account numbers, and generates new account numbers until
        a unique account number (one not already in this list) is found"""
        unique_account_number = False
        while not unique_account_number:
            new_account_number = randint(0, 99999999)
            new_account_number = str(new_account_number).rjust(8, '0')
            if new_account_number in account_numbers:
                unique_account_number = False
                print('Duplicate found!')
            else:
                unique_account_number = True
                return new_account_number

    def set_interest_rate(self):
        """Sets the interest rate of the account based on the account type. Called in the
        constructor."""
        if self.is_savings_account is True:
            return 1.2
        else:
            return 1.0

    def assign_account_number(self, account_number):
        """allows manual overide of the randomly generated account number to account_number"""
        self.account_number = account_number

    def deposit(self, amount):
        """adds amount to the balance of the account, and prints a confirmation message"""
        if isinstance(amount, (float, int)):
            self.balance += round(amount, 2)
            print(f'Amount deposited: ${amount} New Balance: ${self.balance}')
        else:
            print('Please enter a valid numeric entry for the amount to deposit.')

    def withdraw(self, amount):
        """subtracts amount from the balance of the account. Does not allow withdrawal to negatives,
        and charges a $10 overdraft fee if an attempt is made to do so."""
        if isinstance(amount, (float, int)):
            balance = self.balance - round(amount, 2)
            if balance > 0:
                self.balance = balance
                print(f'Amount withdrawn: ${amount} New balance: ${balance}')
            else:
                self.balance -= self.overdraft_fee
                print(f'Insufficient funds. ${self.overdraft_fee} overdraft fee charged.')

    def get_balance(self):
        """prints and returns the current balance of the account"""
        print(f'The current balance of the account belong to {self.full_name} is ${self.balance}')
        return self.balance

    def add_interest(self):
        """adds interest at a rate of 1% annually, compounded monthly (0.083% per month).
        This function adds one month worth of interest"""
        interest = self.balance * (self.interest_rate / 100 / 12)
        interest = round(interest, 2)
        self.balance += interest
        print(f'Added interest. New account balance is ${self.balance}')

    def print_statement(self):
        """prints a statement message with account name, number, and balance"""
        statement_string = (f'{self.full_name}\nAccount No.:'
                            f'{self.get_redacted_account_number()}'
                            f'\nBalance: ${self.balance}')
        print(statement_string)

    def get_account_number(self):
        """returns the full account number"""
        return self.account_number

    def get_redacted_account_number(self):
        """returns the account number with the first four digits redacted and replaced with ****,
        e.g. 12345678 -> ****5678"""
        account_number = self.account_number
        account_number = '****' + account_number[4:8]
        return account_number


class Bank:
    """Bank class, which manages a list of BankAccount objects"""
    def __init__(self):
        self.account_list = []

    def create_account(self, full_name, is_savings_account=False, overdraft_fee=10):
        """creates a new BankAccount instance and adds it to account_list"""
        self.account_list.append(BankAccount(
            full_name,
            self.account_list,
            is_savings_account,
            overdraft_fee
            ))

    def get_account(self, account_num):
        """returns the account object from account_list with account
        number account_num if it exists, otherwise returns None"""
        for account in self.account_list:
            if account.account_number == account_num:
                return account
        return None

    def deposit(self, amount, account_num):
        """deposits amount to account with account number account_num"""
        account = self.get_account(account_num)
        if isinstance(account, BankAccount):
            account.deposit(amount)
        else:
            print('Deposit could not be made.')

    def withdraw(self, amount, account_num):
        """withdraws amount from the account with account number account_num"""
        account = self.get_account(account_num)
        if isinstance(account, BankAccount):
            account.withdraw(amount)
        else:
            print('Withdrawal could not be made.')

    def transfer(self, amount, from_account_num, to_account_num):
        """transfers amount from from_account to to_account"""
        from_account = self.get_account(from_account_num)
        to_account = self.get_account(to_account_num)
        # ensure both accounts exist in the list before altering balance of either
        if isinstance(from_account, BankAccount) and isinstance(to_account, BankAccount):
            from_account.withdraw(amount)
            to_account.deposit(amount)
        else:
            print('Transfer could not be made.')

    def add_monthly_interest(self):
        """adds monthly interest to all accounts in the Bank"""
        for account in self.account_list:
            account.add_interest()

    def statement(self, account_num):
        """prints a statement for the account with the given account_num
        or prints an error message if account does not exist"""
        account = self.get_account(account_num)
        if isinstance(account, BankAccount):
            account.print_statement()
        else:
            print('Statement could not be printed')


# list to store account numbers to prevent duplicates
accounts = []
josh_account = BankAccount('Josh Broughton', accounts, True)
accounts.append(josh_account.get_account_number())
mitchell_account = BankAccount('Mitchell', accounts)
mitchell_account.assign_account_number('03141592')
accounts.append(mitchell_account.get_account_number())
broke_account = BankAccount('Some Person', accounts)
accounts.append(broke_account.get_account_number())

# part 6 of assignment, using methods on Mitchell's account
mitchell_account.deposit(400000)
mitchell_account.print_statement()
mitchell_account.add_interest()
mitchell_account.print_statement()
mitchell_account.withdraw(150)
mitchell_account.print_statement()

# examples of other methods working
broke_account.deposit(100)
broke_account.get_balance()
broke_account.print_statement()
broke_account.add_interest()
josh_account.deposit(1000000)
josh_account.print_statement()
josh_account.add_interest()
josh_account.get_balance()
