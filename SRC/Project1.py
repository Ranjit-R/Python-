#!/usr/bin/env python3
class BankAccount:

    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return

        self.balance += amount
        print(f"Rs.{amount} deposited successfully")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return

        if amount > self.balance:
            print("Insufficient balance")
            return

        self.balance -= amount
        print(f"Rs.{amount} withdrawn successfully")

    def transfer(self, amount, target_account):
        if amount <= 0:
            print("Transfer amount must be positive")
            return

        if amount > self.balance:
            print("Insufficient balance")
            return

        self.balance -= amount
        target_account.balance += amount

        print(f"Rs.{amount} transferred to {target_account.holder_name}")

    def show_balance(self):
        print(f"Current Balance: Rs.{self.balance}")

    def __str__(self):
        return (f"\nAccount Details\n"
                f"-------------------\n"
                f"Account Number : {self.account_number}\n"
                f"Holder Name    : {self.holder_name}\n"
                f"Balance        : Rs.{self.balance}")
                

acc1 = BankAccount("ACC001", "Ranjith", 5000)
acc2 = BankAccount("ACC002", "Shashank", 2000)

acc1.deposit(1000)
acc1.withdraw(1500)
acc1.transfer(2000, acc2)

print(acc1)
print(acc2)
"""
Rs.1000 deposited successfully
Rs.1500 withdrawn successfully
Rs.2000 transferred to Shashank

Account Details
-------------------
Account Number : ACC001
Holder Name    : Ranjith
Balance        : Rs.2500

Account Details
-------------------
Account Number : ACC002
Holder Name    : Shashank
Balance        : Rs.4000
"""
