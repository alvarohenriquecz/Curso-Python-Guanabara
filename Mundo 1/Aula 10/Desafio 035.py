"""
DESAFIO 035: Analisando triangulo v1.0

Desenvolva um programa que leia o comprimento de tres retas
e diga ao usuario se elas podem ou nao formar um triangulo.
"""

r1 = float(input('Digite um numero para o valor da primeira reta: '))
r2 = float(input('Digite um numero para o valor da segunda reta: '))
r3: float(input('Digite um numero para o valor da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas {} x {} x {} podem formar um triangulo!'.format(r1, r2, r3))
else:
    print('As retas {} x {} x {} nao podem formar um triangulo!'.format(r1, r2, r3))
