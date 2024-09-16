from account import CurrentAccount

abdul = CurrentAccount(
    account_number="454545454", balance=100, account_holder_name="Abdul"
)

print(
    f"""
    Account Number: {abdul.account_number:}
    Holder: {abdul.account_holder_name}
    Balance: {abdul.balance}
    """
)
abdul.changeName("qambar")

print(f"New name is: {abdul.account_holder_name}")
abdul.deposit(400)
abdul.withdrawal(300)
print(abdul.balance)

abdul.withdrawal(1000)
print(abdul.balance)
abdul.deposit(-400)
