"""
DESAFIO 028: Jogo da Adivinhacao v1.0

Escreva um programa que faca o computado "pensar" em um numero inteiro entre 0 e 5
e peca para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
O programa devera escrever na tela se o usuario venceu ou perdeu.
"""

from random import randint
nr = randint(0, 5)
ad = int(input('Adivinhe qual numero eu estou pensando (digite um numero de 0 a 5) : '))
if add == nr:
    print('Parabens, voce acertou! Eu estava pensando no numero {}.'.format(nr))
else:
    print('Voce errou! Eu estava pensando no numero {}.'.format(nr))