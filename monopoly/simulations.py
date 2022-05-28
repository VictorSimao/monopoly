from functools import reduce

from .boards import Board


def game_over(players) -> bool:
    alive = 0
    for player in players:
        if not player.is_bankrupt:
            alive += 1
    if alive > 1:
        return False
    return True


def oneGame() -> tuple:
    # create board
    game_board = Board()
    players = game_board.make_players()

    # game
    for round in range(1000):
        if game_over(players):
            break

        for player in players:
            if not game_over(players):
                while player.make_a_move(game_board):
                    pass

    # return final scores
    results = [players[i] for i in range(4)]
    scores = [players[i].money for i in range(4)]
    champions = list(filter(lambda player: player.money == max(scores), results))

    return champions[0].name, round
