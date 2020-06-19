"""
Desafio 025: Procurando uma string dentro de outra

crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

nome = input('Digite seu nome completo: ')
nl = nome.upper().strip()
res = 'SILVA' in nl
print('\n Voce possui "Silva" no nome? True significa que sim e false que nao. \n Resposta: {}'.format(res))
