import random

from .players import Player
from .properties import Property


class Board:
    def __init__(self):
        self.players = []

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

    def make_players(self) -> list:
        players = []
        names = ["impulsivo", "exigente", "cauteloso", "aleatorio"]
        random.shuffle(names)
        players = [Player(name) for name in names]
        return players

    def sell_all(self, player):
        for plot in self.b:
            if plot.owner == player:
                plot.owner = ""

    def action(self, player, position):
        self.b[position].action(player, self)
