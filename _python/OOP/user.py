class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
    def make_withdrawl(self,amount):
        self.account_balance-=amount
    def make_transfer(self,another_user,amount):
        self.account_balance -= amount
        another_user.account_balance += amount
user1 = User("User1", "user1@gmail.com")
user2 = User("User2", "user2@gmail.com")
user3 = User("User3", "user3@gmail.com")

user1.make_deposit(1)
user1.make_deposit(4)
user1.make_withdrawl(3)

print(user1.account_balance)

user2.make_deposit(10)
user2.make_deposit(5)
user2.make_withdrawl(4)
user2.make_withdrawl(4)

print(user2.account_balance)

user3.make_deposit(100)
user3.make_withdrawl(50)
user3.make_withdrawl(30)
user3.make_withdrawl(10)

print(user3.account_balance)

user3.make_transfer(user1,3)

print(user1.account_balance,user3.account_balance)