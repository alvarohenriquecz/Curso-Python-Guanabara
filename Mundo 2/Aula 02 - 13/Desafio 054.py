"""
Desafio 054: Grupo de Maioridade

Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas aidna nao atingiram a maioridade e quantas ja sao maiores.
"""

from datetime import date
ano = date.today().year
pessoas = 0

for c in range(1, 7 +1):
    msg = 'Digite o ano de nascimento da pessoa Nº {}: '.format(c)
    date = int(input(msg))
    if ano - date >= 21:
        pessoas += 1

if pessoas == 0:
    print('Todas as 7 pessoas ainda sao menores de idade.')
elif pessoas == 1:
    print('6 pessoas ainda sao menores de idade. Somente 1 ja atingiu a maioridade.')
else:
    print('Das 7 pessoas, {} sao menores de idade e {} ja atingiram a maioridade.'.format(7 - pessoas, pessoas))
