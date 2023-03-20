import pickle
from small_town_teller import Person, Account, Bank


class PersistenceUtils:
    @staticmethod
    def write_pickle(data):
        pickle.dump(data, open("save.p", "wb"))

    @staticmethod
    def load_pickle():
        return pickle.load(open("save.p", "rb"))


class Bank(Bank):
    def save_data(self):
        PersistenceUtils.write_pickle(self.accounts)

    def load_data(self):
        self.accounts = PersistenceUtils.load_pickle()
        for value in self.accounts:
            self.add_customer(self.accounts.get(value).owner)


if __name__ == '__main__':
    pass