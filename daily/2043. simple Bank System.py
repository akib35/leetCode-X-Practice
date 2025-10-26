class Bank:
    def __init__(self, balance: list[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 <= len(self.balance) and account2 <= len(self.balance):
            if self.balance[account1 - 1] >= money:
                self.balance[account1 - 1] -= money
                self.balance[account2 - 1] += money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account <= len(self.balance):
            self.balance[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if account <= len(self.balance):
            if self.balance[account - 1] >= money:
                self.balance[account - 1] -= money
                return True
        return False


s = Bank([10, 100, 20, 50, 30])
print(s.withdraw(3, 10))  # return True, account 3 has enough balance
print(s.transfer(5, 1, 20))  # return False, account 5 has only 30 in balance
print(s.deposit(5, 20))  # return True, account 5's balance becomes 50 after the deposit
print(s.transfer(3, 4, 15))  # return False, account 3 only has 10 left
print(s.withdraw(10, 50))  # return False, account 10 is invalid
