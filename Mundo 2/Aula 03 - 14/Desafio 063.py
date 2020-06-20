"""
Desafio 063: Sequencia de Fibonacci v1.0

Escreva um programa que leia um numero n inteiro qualquer e mostre
na tela os n primeiros elementos de uma sequencia de fibonacci.

ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
"""

"""
# Feito com for
x = 1
y = 0

n = int(input('Digite quantos primeiros elementos da sequencia de fibonacci voce quer exibir'))

if n > 0:
    if n == 1:
        print('0')
    else:
        print('0', end=' - ')
    
    for i in range(1, n):
        z = x + y
        if i == n - 1:
            print(z, end='')
        else:
            print(z, end=' - ')
        x = y
        y = z
"""

# Feito com while
contador = 1
x = 1
y = 0

n = int(input('Digite quantos primeiros elementos da sequencia de fibonacci voce quer exibir: '))

if n > 0:
    if n == 1:
        print('0')
    else:
        print('0', end=' - ')
    
    while contador < n:
        z = x + y
        if contador == n - 1:
            print(z, end='')
        else:
            print(z, end=' - ')
        x = y
        y = z
        contador += 1