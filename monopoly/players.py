import random


class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.money = 300
        self.is_bankrupt = False

    def __str__(self):
        return f"Name: {self.name}, Money: {self.money}"

    def get_money(self):
        return self.money

    def get_name(self):
        return self.name

    def add_money(self, amount):
        self.money += amount

    def take_money(self, amount, board):
        amount_taken = min(self.money, amount)
        self.money -= amount
        final_account_balance = self.money
        self.check_bankrupcy(board)
        if self.is_bankrupt:
            amount_taken += self.money - final_account_balance
        return amount_taken

    def make_a_move(self, board):
        if self.is_bankrupt:
            return

        # roll dice
        dice = random.randint(1, 6)

        # move the piece
        self.position += dice

        if self.position >= 20:
            self.position = self.position - 20
            self.add_money(100)

        board.action(self, self.position)

    def check_bankrupcy(self, board):
        if self.money < 0:
            self.is_bankrupt = True

            board.sell_all(self)

    def purchase_strategy(self, base_cost, rent):
        if self.name == "exigente" and rent <= 50:
            return False

        elif self.name == "cauteloso" and self.money - base_cost <= 80:
            return False

        elif self.name == "aleatorio":
            luck = random.randint(1, 2)
            if luck == 1:
                return False

        return True
