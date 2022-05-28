import statistics

from decimal import Decimal
from monopoly.simulations import oneGame


def analyzeResults():
    list_champions = []
    list_finished_round = []
    for i in range(300):
        champion, finished_round = oneGame()
        list_champions.append(champion)
        list_finished_round.append(finished_round)

    time_out = list_finished_round.count(999)
    finished_round_avg = statistics.mean(list_finished_round)
    names = ["impulsivo", "exigente", "cauteloso", "aleatorio"]
    strategies = {}
    names_count = [list_champions.count(name) for name in names]
    for name in names:
        strategies[name] = round(list_champions.count(name) / 300 * 100)
    winning_strategy = list(
        filter(
            lambda strategy: list_champions.count(strategy) == max(names_count), names
        )
    )
    print(f"Quantas partidas terminam por time out (1000 rodadas): {time_out} partidas")
    print(
        f"Quantos turnos em média demora uma partida: {finished_round_avg*4:.2f} turnos"
    )
    print(
        f"Qual a porcentagem de vitórias por comportamento dos jogadores: {strategies}"
    )
    print(f"Qual o comportamento que mais vence: {winning_strategy[0]}")
