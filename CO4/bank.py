class Bank:
    def __init__(self, accNo, name, accType, balance=0):
        # Constructor to initialize account details
        self.accNo = accNo
        self.name = name
        self.accType = accType
        self.balance = balance

    def deposit(self, amount):
        # Method to deposit money into the account
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful! New balance: {self.balance}")
        else:
            print("Invalid deposit amount. Enter a positive value.")

    def withdraw(self, amount):
        # Method to withdraw money from the account
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount. Enter a positive value.")

    def display(self):
        # Method to display account details
        print("\nAccount Number:", self.accNo)
        print("Account Holder Name:", self.name)
        print("Account Type:", self.accType)
        print("Balance:", self.balance)


b1 = Bank(1002, "Alfiya P K", "Savings", 0)
b1.display()

while True:
    # Repeat the menu until the user chooses Exit
    print("\n*** MENU ***")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display")
    print("4. Exit")

    choice = int(input("\nEnter your choice (1-4): "))

    if choice == 1:
        d = float(input("Enter amount to be deposited: "))
        b1.deposit(d)

    elif choice == 2:
        w = float(input("Enter amount to withdraw: "))
        b1.withdraw(w)

    elif choice == 3:
        b1.display()

    elif choice == 4:
        print("Exit")
        break

    else:
        print("Enter a valid choice.")
