"""
Desafio 068: Jogo do Par ou Impar

Faca um programa que jogue par ou impar com o computador. O jogo so sera interrompido quando o 
jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.
"""

from random import randint
sep1 = '-=' * 28
sep2 = '-' * 56
pontos = 0
print(sep1)
titulo = 'Vamos jogar par ou impar'
print(f'{titulo:^56}')
print(sep1)
while True:
    pc = randint(1, 10)
    jogada = int(input('Digite um valor: '))
    pi = 'X'
    while pi != 'P' and pi 'I':
        pi = str(input('Par ou Impar [P/I]? ')).strip().upper()[0].replace('I', 'i')
    total = jogada + pc
    print(sep2)
    print(f'Voce jogou {jogada} e o computador {pc}. Total de {total}.', end=' ')
    if total % 2 == 0:
        print('Deu Par.')
        rodada = 'P'
    else:
        print('Deu impar.')
        rodada = 'I'
    print(sep2)
    if pi == rodada:
        print('Voce ganhou!')
        print('Vamos jogar novamente....')
        print(sep1)
        pontos += 1
    else:
        print('Voce perdeu')
        break
print(sep1)
print('GAME OVER', end=' ')
if pontos == 0:
    print('Voce nao ganhou nenhuma vez')
elif pontos == 1:
    print('Voce ganhou somente 1 vez')
else:
    print(f'Voce ganhou {pontos} vezes.')
    