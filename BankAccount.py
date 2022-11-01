from re import L


class BankAccount:
    def __init__ (self, full_name, account_number, balance, account_type):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
    
    def deposit (self, amount):
        self.balance += amount
        print(f'Amount Deposited: ${"{:.2f}".format(amount)}. New balance: ${"{:.2f}".format(self.balance)}')

    def withdraw (self, amount):
        self.balance -= amount
        if (self.balance < 0):
            print("Insufficient funds. This transaction incurs a $10 overdraft fee.")
            self.balance -= 10
        print(f'Amount Withdrawn: ${"{:.2f}".format(amount)}. New balance: ${"{:.2f}".format(self.balance)}')
            
    def get_balance(self):
        print(f'Current account balance is ${"{:.2f}".format(self.balance)}')
        return self.balance

    def add_interest(self):
        if self.account_type == 'chequing':
            self.balance *= 1.00083
        elif self.account_type == 'savings':
            self.balance *= 1.01

    def print_statement(self):
        print('----------- STATEMENT -----------')
        print(f'{self.full_name}')
        print(f'Account No.: ****{str(self.account_number)[4:]}')
        print(f'Balance: ${"{:.2f}".format(self.balance)}')
        print(f'Account type: {self.account_type}')
        print('---------------------------------')

account_1 = BankAccount('Mitchell Hudson', 13141592, 0, 'chequing') 
account_2 = BankAccount('Joi Anderson', 76543218, 100.00, 'chequing') 
account_3 = BankAccount('Rick Martin', 65432187, 10000.99, 'chequing') 

# Examples
account_1.deposit(400000.00)
account_1.get_balance()
account_1.add_interest()
account_1.get_balance()
account_1.withdraw(500000)
account_1.print_statement()

# Stretch Challenges
mitch_savings = BankAccount('Mitchell Hudson', 13141592, 400000.00, 'savings')
mitch_chequing = BankAccount('Mitchell Hudson', 24567893, 23000.56, 'chequing')

bank = []
bank.append(mitch_savings)
bank.append(mitch_chequing)

for account in bank:
    account.get_balance()
    account.add_interest()
    account.get_balance()