class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


class Account:

    def __init__(self, number, type, owner):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = 0




class Bank:
    customers = []
    accounts = {}

    def add_customer(self, Person):
        self.customers.append(Person)

    def add_account(self, Account):
        self.accounts.update({Account.number: Account}) if self.customers.__contains__(Account.owner) else print('Account is not from one of our Customers')

    def remove_account(self, Account):
        self.accounts.pop(Account.number)

    def deposit(self, Account, amount):
        self.accounts[Account].balance = self.accounts.get(Account).balance + amount

    def withdrawal(self, Account, amount):
        self.accounts[Account].balance = self.accounts.get(Account).balance - amount

    def balance_inquiry(self, Account):
        print(self.accounts.get(Account).balance)


if __name__ == '__main__':
    pass
