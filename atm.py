original_pin=1729
balance=10000
pin=int(input("enter pin"))
amount=int(input("enter amount of money"))
if original_pin!=pin:
    print("access denied")
elif amount>balance:
    print("insufficient balance")
elif amount < 0:
    print("invalid amount")
else:
    balance=balance-amount
    print("balance:", balance)
