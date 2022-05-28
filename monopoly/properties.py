class Property:
    def __init__(self, name, cost, rent):
        self.name = name
        self.cost = cost
        self.rent = rent
        self.owner = ""

    def action(self, player, board):

        if self.owner == player:
            return

        # sale
        elif self.owner == "":
            if player.purchase_strategy(self.cost, self.rent):
                player.take_money(self.cost, board)
                self.owner = player
            return

        # rent
        else:
            amount_taken = player.take_money(self.rent, board)
            self.owner.add_money(amount_taken)
