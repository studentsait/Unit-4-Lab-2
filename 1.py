class BankAccount:
    def __init__(self, accountNumber, customerName, balance):
        self.accountNumber = accountNumber
        self.customerName = customerName
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance is ${self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")

    def display(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Customer Name: {self.customerName}")
        print(f"Current Balance: ${self.balance}")
# Create a new bank account
account1 = BankAccount(123456, "kartikey", 50000)

# Deposit money into the account
account1.deposit(1000)

# Withdraw money from the account
account1.withdraw(500)

# Display the account details
account1.display()