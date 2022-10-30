class BankAccount:
    def __init__ (self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance
    
    def deposit (self, amount):
        self.balance += amount
        print(f'Amount Deposited: ${amount}')

    def withdraw (self, amount):
        self.balance -= amount
        print(f'Amount Withdrawn: ${amount}')
        if (self.balance < 0):
            print("Insufficient funds. This transaction incurs a $10 overdraft fee.")
            self.balance -= 10
            print(f'Current balance is ${self.balance}')

