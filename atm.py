class ATM:
    def _init_(self):
        self.balance = 0

    def set_balance(self, initial_balance):
        self.balance = initial_balance

    def check_balance(self):
        return f"Your balance is ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit of ${amount} successful. Your new balance is ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds. Withdrawal failed."
        else:
            self.balance -= amount
            return f"Withdrawal of ${amount} successful. Your new balance is ${self.balance}"

# Example usage:
atm = ATM()
initial_balance = float(input("Enter initial balance: $"))
atm.set_balance(initial_balance)

while True:
    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        print(atm.check_balance())
    elif choice == '2':
        amount = float(input("Enter deposit amount: $"))
        print(atm.deposit(amount))
    elif choice == '3':
        amount = float(input("Enter withdrawal amount: $"))
        print(atm.withdraw(amount))
    elif choice == '4':
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")