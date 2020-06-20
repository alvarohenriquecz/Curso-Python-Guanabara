"""
Desafio 058: Jogo da adivinhacao v2.0

Melhore o jogo do desafio 028 onde o computador vai "pensar" em um numero entre 0 e 10.
So que agora o jogador vai tentar adivinhar ate acertar, mostrando no final quantos 
palpites foram necessarios para vencer.
"""

from random import randint
from time import sleep
print('Vou pensar em um numero de 0 a 10...')
sleep(1)
numero_pensado = randint(0, 10)
quantos_chutes = 1
chute = int(input('Em qual numero eu pensei? '))

while chute != numero_pensado:
    if 0 <= chute <= 10:
        if numero_pensado < chute:
            print('{} chute errado! O numero que eu pensei e menor. Chute novamente!'.format(quantos_chutes))
        else:
            print('{} chute errado! O numero que eu pensei e maior. Chute novamente!'.format(quantos_chutes))
        quantos_chutes += 1
        chute = int(input('Em qual numero eu pensei? '))
    else:
        print('Chute invalido! o numero que eu pensei e de 0 a 10')
        chute = int(input('Em qual numero eu pensei? '))

print('Eu pensei no numero {}.'.format(numero_pensado), end=' ')
if quantos_chutes == 1:
    print('Parabens, voce acertou no 1 chute!')
else:
    print('Parabens, voce acertou no {} chute'.format(quantos_chutes))
