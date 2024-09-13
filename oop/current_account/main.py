from account import CurrentAccount
qambar = CurrentAccount("454545454", "Abdul:")

print(
    f"Account Number: {qambar.account_number:} Holder:{qambar.account_holder_name}, Balance{qambar.balance}"
)
qambar.changeName("qambar")
qambar.deposit(400)
qambar.withdrawal(300)
