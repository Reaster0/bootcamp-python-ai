class Account(object):
	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(kwargs)
		Account.ID_COUNT += 1

	def transfer(self, amount):
		self.value += amount

class Bank(object):
	
	def __init__(self):
		self.account = []
	
	def add(self, account):
		assert isinstance(account, Account), "the account is corrupted"
		self.account.append(account)
		print(dir(account))

	def transfer(self, origin, dest, amount):
		if not origin in self.account or not dest in self.account:
			return False
	

	def fix_account(self, account):
		pass

	def find_account(self, account):
		for user in self.account:
			if user.name == account:
				return user

bank = Bank()
bank.add(Account(
    'Smith Jane',
    zip='911-745',
    value=1000.0,
    bref='1044618427ff2782f0bbece0abd05f31'))

#print (bank.account[0])
