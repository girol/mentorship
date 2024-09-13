from random import randint
from account import CurrentAccount
from time import sleep

name = input("Tell your name for the new Account: ")
balance = input("How much money will you startt your account? ")

account_number = randint(1000, 9999)

account = CurrentAccount(account_number, name, int(balance))

print(
    f"""
    Details of your new account:
    ================================
    Number: {account.account_number}
    Holder: {account.account_holder_name}
    Balance: {account.balance}
    ================================
    """
)

action = ""
while action != "exit":
    sleep(0.5)
    print("What action you want do do?")
    print("Choose your action:")
    print("1. Deposit")
    print("2. Withdrawal")
    print("Type: exit, to exit the program")
    action = input(">> ")

    if action not in ["1", "2"]:
        print("ERROR: Invalid Option")
        continue

    if action == "1":
        amount = input("How much to deposit? >> ")
        account.deposit(int(amount))
    elif action == "2":
        amount = input("How much to withdraw? >> ")
        account.withdrawal(int(amount))

    print("================================")
