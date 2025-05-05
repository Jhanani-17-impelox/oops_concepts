# Design an abstract class BankAccount with an abstract method withdraw(). 
# Implement subclasses SavingsAccount and CheckingAccount with their own withdrawal logic. 
# The base class should only define common methods like deposit() but leave withdraw() as an abstract method.

from abc import ABC, abstractmethod

# Abstract Base Class
class BankAccount(ABC):
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"[{self.account_number}] Deposited: ₹{amount}. New Balance: ₹{self.balance}")
        else:
            print(f"[{self.account_number}] Invalid deposit amount: ₹{amount}")

    @abstractmethod
    def withdraw(self, amount):
        pass

# Subclass: SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, withdrawal_limit=10000):
        super().__init__(account_number, balance)
        self.withdrawal_limit = withdrawal_limit

    def withdraw(self, amount):
        if amount <= 0:
            print(f"[{self.account_number}] Invalid withdrawal amount: ₹{amount}")
        elif amount > self.withdrawal_limit:
            print(f"[{self.account_number}] Withdrawal failed. Amount exceeds savings limit: ₹{self.withdrawal_limit}")
        elif amount > self.balance:
            print(f"[{self.account_number}] Withdrawal failed. Insufficient balance.")
        else:
            self.balance -= amount
            print(f"[{self.account_number}] Withdrawn: ₹{amount}. Remaining Balance: ₹{self.balance}")

# Subclass: CheckingAccount
class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance=0, overdraft_limit=5000):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print(f"[{self.account_number}] Invalid withdrawal amount: ₹{amount}")
        elif amount > self.balance + self.overdraft_limit:
            print(f"[{self.account_number}] Withdrawal failed. Exceeds overdraft limit of ₹{self.overdraft_limit}")
        else:
            self.balance -= amount
            print(f"[{self.account_number}] Withdrawn: ₹{amount}. New Balance: ₹{self.balance}")

# Create accounts
savings = SavingsAccount("SAV123", 15000)
checking = CheckingAccount("CHK456", 5000)

# Deposits
savings.deposit(2000)
checking.deposit(1000)

# Withdrawals
savings.withdraw(11000)   # exceeds limit
savings.withdraw(5000)    # valid

checking.withdraw(7000)   # allowed (5000 balance + 5000 overdraft)
checking.withdraw(12000)  # exceeds overdraft


