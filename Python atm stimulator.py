class ATM:
    def __init__(self):
        self.balance = int(input("Enter the amount : "))

    def login(self,pin):
        if pin == 456123:
            return True
        return False
    
    def credit(self,amount):
        self.balance += amount
        print("Amount Credited successfully")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdraw was succesful")
        else:
            print("Insuffient balance")

    def display(slef):
        print("Remaining Balance : ",slef.balance)

obj = ATM()

# Login attempts
for i in range(3):
    pin = int(input("enter the pin : "))
    if obj.login(pin):
        print("Login succeful")
        break
    else:
        print("Wrong pin")
else:
    print(" 3 attempts completed")
    exit()

while True :
    print("\n 1.credit amount")
    print("2.Withdraw the amount")
    print("3.Check the reamining balance")
    print("4.Exit")

    choice = int(input("Enter choice : "))

    if choice == 1:

        amount = int(input("Enter amount to credit : "))
        obj.credit(amount)

    elif choice == 2:

        amount = int(input("Enter amount to debit : "))
        obj.withdraw(amount)

    elif choice == 3:

        obj.display()

    elif choice == 4:

        print("Thank You")
        break

    else:
        print("Invalid Choice")






