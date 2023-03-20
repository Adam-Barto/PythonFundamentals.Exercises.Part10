# from small_town_teller import Person, Account, Bank
#
# zc_bank = Bank()
# bob = Person(1, "Bob", "Smith")
# zc_bank.add_customer(bob)
# bob_savings = Account(1001, "SAVINGS", bob)
# zc_bank.add_account(bob_savings)
# zc_bank.balance_inquiry(1001)
# # 0
# zc_bank.deposit(1001, 256.02)
# zc_bank.balance_inquiry(1001)
# # 256.02
# zc_bank.withdrawal(1001, 128)
# zc_bank.balance_inquiry(1001)
# # 128.02
# mochi = Person(2, "Mochi", "Potato")
# zc_bank.add_customer(mochi)
# mochi_checking = Account(1002, "CHECKING", mochi)
# zc_bank.add_account(mochi_checking)

from persistent_small_town_teller import Person, Account, Bank


zc_bank = Bank()
# zc_bank.save_data()
zc_bank.customers
# {}
zc_bank.accounts
# {}
zc_bank.load_data()
print(zc_bank.accounts)
# {1: <persistent_small_town_teller.Person object at 0x1098e6a90>}
print(zc_bank.customers)
# {1001: <persistent_small_town_teller.Account object at 0x1099e04d0>}