class ATM:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.logged_in = False

    def login(self):
        print("Please enter your secret PIN to login.")
        entered_pin = input("PIN: ")
        if entered_pin == self.pin:
            self.logged_in = True
            print("Login successful!")
        else:
            print("Incorrect PIN. Please try again.")

    def logout(self):
        self.logged_in = False
        print("You have been logged out.")

    def check_balance(self):
        if self.logged_in:
            print(f"Your current balance is: ${self.balance:.2f}")
        else:
            print("Please login first.")

    def deposit(self):
        if self.logged_in:
            try:
                amount = float(input("Enter amount to deposit: $"))
                if amount > 0:
                    self.balance += amount
                    print(f"${amount:.2f} deposited successfully!")
                else:
                    print("Deposit amount must be positive.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Please login first.")

    def withdraw(self):
        if self.logged_in:
            try:
                amount = float(input("Enter amount to withdraw: $"))
                if amount > 0:
                    if amount <= self.balance:
                        self.balance -= amount
                        print(f"${amount:.2f} withdrawn successfully!")
                    else:
                        print("Insufficient balance.")
                else:
                    print("Withdrawal amount must be positive.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Please login first.")

    def show_menu(self):
        if not self.logged_in:
            print("You need to login first.")
            return

        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")

        option = input("Please select an option: ")

        if option == "1":
            self.check_balance()
        elif option == "2":
            self.deposit()
        elif option == "3":
            self.withdraw()
        elif option == "4":
            self.logout()
        else:
            print("Invalid option. Please try again.")

def main():
    # Create an instance of ATM with a dummy account
    atm = ATM(account_number="123456", pin="7975", balance=1000)

    # Simulate ATM interface
    while True:
        print("\nWelcome to the ATM!")
        if atm.logged_in:
            atm.show_menu()
        else:
            atm.login()

        continue_option = input("Would you like to perform another action? (y/n): ")
        if continue_option.lower() != 'y':
            print("Thank you for using the ATM!")
            break

if __name__ == "__main__":
    main()
