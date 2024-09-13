"""Current Account Class: Create a class to implement a current account. 
The class must have the following attributes: account number, account holder name and balance.
 The methods are as follows: changeName, deposit and withdrawal; 
 In the constructor, balance is optional, with a default value of zero and the other attributes are mandatory."""


class CurrentAccount:
    def __init__(self, account_number, account_holder_name, balance=2000):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def changeName(self, new_name):
        self.account_holder_name = new_name

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + int(amount)
            print(f"Deposit{amount}, new balance {self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdrawal(self, amount):
        if amount > 0:
            if amount - self.balance:
                print(f"withdraw{amount}, New balance is {self.balance}")
            else:
                print("insuffeciente fund")
        else:
            print("withdrawal amount must be positive")


"""my_account = CurrentAccount("454545454", "Abdul")

print(
    f"Account Number:{my_account.account_number:} Holder:{my_account.account_holder_name}, Balance{my_account.balance}"
)
my_account.changeName("qambar")
my_account.deposit(400)
my_account.withdrawal(300)"""
