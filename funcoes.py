import random


def computador_ganha(mesa, deck_jogador_1, deck_jogador_2):
    mesa.append(deck_jogador_2.pop(0))
    mesa.append(deck_jogador_1.pop(0))
    while len(mesa) > 0:
        deck_jogador_2.append(mesa.pop(0))


def usuario_ganha(mesa, deck_jogador_1, deck_jogador_2):
    mesa.append(deck_jogador_1.pop(0))
    mesa.append(deck_jogador_2.pop(0))
    while len(mesa) > 0:
        deck_jogador_1.append(mesa.pop(0))


def empate(mesa, deck_jogador_1, deck_jogador_2):
    cartas_empate = [deck_jogador_1.pop(0), deck_jogador_2.pop(0)]
    random.shuffle(cartas_empate)
    mesa.append(cartas_empate.pop(0))
    mesa.append(cartas_empate.pop(0))
