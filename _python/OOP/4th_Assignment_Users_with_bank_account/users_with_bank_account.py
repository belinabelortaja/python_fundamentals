class BankAccount:
    def __init__(self, account_nr, iban, interes_rate,balance):
        self.nr = account_nr
        self.iban = iban
        self.account_balance = balance
        self.interes_rate = interes_rate

    def deposit(self, amount):
        self.account_balance+=amount
        return self

    def withdrawl(self,amount):
        self.account_balance-=amount
        return self

    def yeld_interest(self,amount):
        interest= self.interes_rate* amount
        self.account_balance += interest
        return self

    def display_info(self):
        return self
class User:
    def __init__(self, name, email,bankAccount):
        self.name = name
        self.email = email
        self.account = bankAccount

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawl(self,amount):
        self.account.withdrawl(amount)
        return self

    def account_balance1(self):
        print(self.account)
        return self.account

account1 = BankAccount("123553333", "NF19293930330303", 0.01,0)
user1 = User("User1", "user1@gmail.com", account1)

account1.deposit(500).deposit(100).deposit(40).withdrawl(300).yeld_interest(20).display_info()
print(account1.account_balance)


