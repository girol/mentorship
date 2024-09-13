"""Current Account Class: Create a class to implement a current account.
The class must have the following attributes: account number,
account holder name and balance.
The methods are as follows:
 - changeName
 - deposit
 - withdrawal

In the constructor, balance is optional, with a default value of zero
and the other attributes are mandatory.
 """


class CurrentAccount:
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def changeName(self, new_name):
        self.account_holder_name = new_name

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + int(amount)
            print(f"Deposit: ${amount}, New Balance: {self.balance}")
        else:
            print("ERROR: Deposit amount must be positive")

    def withdrawal(self, amount):
        if amount > 0:
            if amount > self.balance:
                print("ERROR: Insuffecient funds!")
            else:
                self.balance = self.balance - amount
                print(f"Withdraw: {amount}, New Balance: {self.balance}")
        else:
            print("ERROR: Withdrawal amount must be positive")
