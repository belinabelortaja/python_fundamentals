class BankAccount:
    def __init__(self, account_nr, iban, interes_rate):
        self.nr = account_nr
        self.iban = iban
        self.account_balance = 0
        self.interes_rate = interes_rate

    def make_deposit(self, amount):
        self.account_balance+=amount
        return self

    def make_withdrawl(self,amount):
        self.account_balance-=amount
        return self

    def yeld_interest(self,amount):
        interest= self.interes_rate* amount
        self.account_balance += interest
        return self

    def display_account_info(self):
        return self

Account1 = BankAccount("123553333", "NF19293930330303", 0.01)
Account2 = BankAccount("757383839339", "MH2828238493939393",0.01)


Account1.make_deposit(500).make_deposit(100).make_deposit(40).make_withdrawl(300).yeld_interest(20).display_account_info()

print(Account1.account_balance)

Account2.make_deposit(700).make_deposit(1000).make_withdrawl(300).make_withdrawl(200).make_withdrawl(100).yeld_interest(15).display_account_info()

print(Account2.account_balance)
