"""
Desfio 091: Jogo de Dados em Python

Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. Guarde esses resultados em um
dicionario. No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior numero no dado.
"""

from random import randint
from time import sleep
jogadores = dict()
jogadores['Jogador 1'] = randint(1, 6)
jogadores['Jogador 2'] = randint(1, 6)
jogadores['Jogador 3'] = randint(1, 6)
jogadores['Jogador 4'] = randint(1, 6)

print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'    O {k} tirou {v}')
    sleep(1)

print('Ranking dos jogadores:')
contador = 1
for item in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'    {contador}º lugar: {item} com {jogadores[item]}')
    contador += 1
    sleep(1)
