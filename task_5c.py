class BankAccount:
    def __init__(self, name, balance=0.0):
        """Initialize account with owner's name and optional starting balance."""
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        """Withdraw money from the account if funds are available."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")
    def check_balance(self):
        """Return the current balance."""
        print(f"Account balance for {self.name}: {self.balance}")
if __name__ == "__main__":
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))  
    account = BankAccount(name, balance)
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            amt = float(input("Enter deposit amount: "))
            account.deposit(amt)
        elif choice == "2":
            amt = float(input("Enter withdrawal amount: "))
            account.withdraw(amt)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("Exiting")
            break
        else:
            print("Invalid choice. Please try again.")
