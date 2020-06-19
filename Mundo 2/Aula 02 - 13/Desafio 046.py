"""
Desafio 046: COntagem Regressiva

Faca um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 ate 0, com pausa de 1 segundo entre eles.
"""
from time import sleep
print('Contagem regressiva para estourar os fogos de artificio:')
for c in range(10, 0, -1, -1)
    sleep(1)
    if c != 0:
        print('{}...'.format(c))
    else:
        print('BOOMMM')
    