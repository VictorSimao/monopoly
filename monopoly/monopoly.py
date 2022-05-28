import random


class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.money = 300
        self.is_bankrupt = False
        self.properties = []

    def __str__(self):
        return (
            "Player: "
            + self.name
            + ". Position: "
            + str(self.position)
            + ". Money: $"
            + str(self.money)
        )

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
        else:
            amount_taken = amount
        return amount_taken

    def move_to(self, position):
        self.position = position

    def make_a_move(self):
        if self.is_bankrupt:
            return

        # roll dice
        dice = random.randint(1, 6)

        # move the piece
        self.position += dice

        if self.position >= 20:
            self.position = self.position - 20
            self.add_money(100)

    def check_bankrupcy(self, board):
        if self.money < 0:
            board.sell_all(self)
            self.is_bankrupt = True

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


class Property:
    def __init__(self, name, cost, rent):
        self.name = name
        self.cost = cost
        self.rent = rent
        self.owner = ""

    def action(self, player):

        if self.owner == player:
            return

        # sale
        elif self.owner == "":
            if player.purcharse_strategy(self.cost, self.rent):
                player.take_money(self.cost)
                self.owner = player
            return

        # rent
        else:
            amount_taken = player.take_money(self.rent)
            self.owner.add_money(amount_taken)


class Board:
    def __init__(self, players):
        """
        name: does not really matter, just convenience
        cost: used when buying plot
        rent: used for rent
        """

        self.players = players

        self.b = []
        # 1-5
        self.b.append(Property("Mediterraneal Avenue", 60, 5))
        self.b.append(Property("Baltic Avenue", 60, 5))
        self.b.append(Property("Park Place", 200, 30))
        self.b.append(Property("Oriental Avenue", 100, 10))
        self.b.append(Property("Vermont Avenue", 100, 10))
        # 6 - 10
        self.b.append(Property("Connecticut Avenue", 120, 15))
        self.b.append(Property("St.Charle's Place", 140, 20))
        self.b.append(Property("Martin Gardens", 150, 25))
        self.b.append(Property("States Avenue", 140, 20))
        self.b.append(Property("Virginia Avenue", 160, 25))
        # 11-15
        self.b.append(Property("Atlantic Avenue", 200, 30))
        self.b.append(Property("St.James Place", 180, 35))
        self.b.append(Property("Tennessee Avenue", 180, 35))
        self.b.append(Property("New York Avenue", 200, 40))
        self.b.append(Property("Kentucky Avenue", 220, 50))
        # 15-20
        self.b.append(Property("Indiana Avenue", 220, 45))
        self.b.append(Property("Illinois Avenue", 240, 50))
        self.b.append(Property("Park Place", 260, 55))
        self.b.append(Property("Pacific Avenue", 300, 60))
        self.b.append(Property("North Carolina Avenue", 300, 60))
        self.b.append(Property("Pennsylvania Avenue", 320, 70))

    def sell_all(self, player):
        for plot in self.b:
            if plot.owner == player:
                plot.owner = ""


def isGameOver(players):
    alive = 0
    for player in players:
        if not player.is_bankrupt:
            alive += 1
    if alive > 1:
        return False
    return True


def oneGame():
    players = []
    names = ["impulsivo", "exigente", "cauteloso", "aleatorio"]
    random.shuffle(names)
    players.append(Player(names[i] for i in range(4)))

    # create board
    gameBoard = Board(players)

    # game
    for i in range(1000):
        if isGameOver(players):
            break

        for player in players:
            if not isGameOver(players):
                while player.make_a_move(gameBoard):
                    pass

    # return final scores
    results = []
    results.append((players[i].get_money() for i in range(4)))

    print(results)


if __name__ == "__main__":
    oneGame()
