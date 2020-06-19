"""
Desafio 051: Progressao Aritmetica

Desenvolva um programa que leia o primeiro termo e a razao de uma pa.
no final, mostre os 10 primeiros termos dessa progressao.
"""

pt = int(input('Digite o primeiro termo da progressao aritmetica: '))
r = int(input('Digite a razao: '))
print('\n10 Primeiros Termos da PA com razao {} (Iniciado em {}):'.format(r, pt))
print(pt, end=' ')

for c in range(1, 10):
    pt += r
    print(pt, end=' ')
    