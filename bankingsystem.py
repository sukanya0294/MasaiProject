
"""BankingSystem




import sys

class Bank:
    def __init__(self, account_number, account_holder, balance=0.0):
        """
        Initializes a new BankAccount object.

        Args:
            account_number (str): The unique account number.
            account_holder (str): The name of the account holder.
            balance (float, optional): The initial balance of the account. Defaults to 0.0.
        """
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.

        Args:
            amount (float): The amount to deposit.

        Returns:
            float: The updated account balance.
        """
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        self.balance += amount
        return self.balance

    def withdrawal(self, amount):
        """
        Withdraws the specified amount from the account.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            float: The updated account balance.

        Raises:
            ValueError: If the withdrawal amount is negative or exceeds the account balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

# Get account details from the user
account_number = int(input("Enter Account Number: "))
account_holder = input("Enter Account Holder Name: ")

# Create a bank account object
B = Bank(account_number, account_holder)

while True:
    print('''\nEnter D-for Deposit:
              Enter W-for Withdrawal:
              Enter E-for Exit:''')
    choice = input("Enter your Choice: ").strip().lower()

    if choice == "e":
        sys.exit()

    if choice in ("d", "w"):
        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue

    if choice == "d":
        try:
            updated_balance = B.deposit(amount)
            print("Balance after Deposit:", updated_balance)
        except ValueError as e:
            print(e)

    elif choice == "w":
        try:
            updated_balance = B.withdrawal(amount)
            print("Balance after Withdrawal:", updated_balance)
        except ValueError as e:
            print(e)

    else:
        print("Invalid choice. Please try again.")

