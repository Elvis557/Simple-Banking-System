class BankAccount:
    def __init__(self, account_name):
        self.account_name = account_name
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def view_balance(self):
        print(f"Account: {self.account_name}, Balance: ${self.balance:.2f}")


def main():
    print("=== Welcome to Simple Bank ===")
    account_name = input("Enter your account name: ")
    account = BankAccount(account_name)

    while True:
        print("\n=== Main Menu ===")
        print("1. View Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            account.view_balance()
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Please enter a valid amount.")
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Please enter a valid amount.")
        elif choice == "4":
            print("Thank you for using Simple Bank. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
