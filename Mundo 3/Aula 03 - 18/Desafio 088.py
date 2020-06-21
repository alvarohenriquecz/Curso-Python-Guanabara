"""
DESAFIO 088: Palpites Para a Mega Sena

Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep

sorteio, megasena = list(), list()
print('-' * 30)
print(f'{"JOGADA NA MEGA SENA":^30}')
print('-' * 30)
jogos = int(input('Quantos jogos voce quer que eu sorteie? '))
print('-=' * 4, end=' ')
print(f'SORTEANDO {jogos} JOGOS', end=' ')
print('-=' * 4)

for j in range(jogos):
    b1, b2, b3 = randint(1, 60), randint(1, 60), randint(1, 60)
    b4, b5, b6 = randint(1, 60), randint(1, 60), randint(1, 60)
