class BankAccount:
    def __init__(self, account_name, balance=0):
        """Initialize a bank account with a name and optional starting balance."""
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account. Amount must be positive."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account. Cannot withdraw more than balance."""
        if amount > self.balance:
            print(f"Insufficient funds. Current balance: ${self.balance}.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}.")

    def display_balance(self):
        """Display the current balance of the account."""
        print(f"{self.account_name}'s balance: ${self.balance}")

