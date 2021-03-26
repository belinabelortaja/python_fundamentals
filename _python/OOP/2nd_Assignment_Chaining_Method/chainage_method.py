class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance+=amount
        return self

    def make_withdrawl(self,amount):
        self.account_balance-=amount
        return self

    def make_transfer(self,another_user,amount):
        self.account_balance -= amount
        another_user.account_balance += amount
        return self
    def account_balance1(self):
        print(self.account_balance)
        return self


user1 = User("User1", "user1@gmail.com")
user2 = User("User2", "user2@gmail.com")
user3 = User("User3", "user3@gmail.com")

user1.make_deposit(1).make_deposit(4).make_withdrawl(3).account_balance1()

print(user1.account_balance)

user2.make_deposit(10).make_deposit(5).make_withdrawl(4).make_withdrawl(4).account_balance1()

print(user2.account_balance)

user3.make_deposit(100).make_withdrawl(50).make_withdrawl(30).make_withdrawl(10).account_balance1()

print(user3.account_balance)

user3.make_transfer(user1,3)

print(user1.account_balance,user3.account_balance)
