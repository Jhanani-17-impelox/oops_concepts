class Account:
    def __init__(self, balance):   # Constructor
        self.balance = balance     # Initialize the balance

    def deposit(self, amount):     # Method to add money
        self.balance += amount     # Add amount to balance

    def show_balance(self):        # Method to return balance
        return f"Balance after bonus deposit: {self.balance}"


class SavingsAccount(Account):     # Inheriting from Account
    def __init__(self, balance):   # Constructor of SavingsAccount
        super().__init__(balance)  # Call parent constructor to set balance

    def deposit(self, amount):     # Overriding deposit method
        super().deposit(amount)    # Call the parent class deposit
        if amount > 1000:
            bonus = amount * 0.02  # 2% bonus
            self.balance += bonus  # Add bonus


# Sample usage
acc = SavingsAccount(5000)     # Create object with balance 5000
acc.deposit(1500)              # Deposit 1500, triggers bonus
print(acc.show_balance())      # Output balance after bonus
