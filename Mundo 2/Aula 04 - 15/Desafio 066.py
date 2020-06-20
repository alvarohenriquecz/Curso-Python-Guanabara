"""
Desafio 066: Varios Numeros com flag

Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando 
o usuario digitar o valor 999, que e a condicao de parada. No final, mostre quantos numeros
foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""

s = t = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    s += n
    t += 1

if t == 0:
    print('Voce nao digitou nenhum valor!')
elif t == 1: 
    print(f'Voce digitou somente 1 valor, portanto seu total e {s}')
else:
    print(f'A soma dos {t} valores foi {s}')
