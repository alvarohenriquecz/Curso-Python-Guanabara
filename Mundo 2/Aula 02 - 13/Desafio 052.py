"""
Desafio 052: Numeros Primos

Faca um programa que leia um numero inteiro e diga se ele e ou nao um numero primo.
"""

n = int(input('Digite um numero: '))
v = True

if n < 2:
    v = False
else:
    for c in range(2, n -1):
        if n % c == 0:
            v = False

if v:
    print('{} e um numero primo.'.format(n))
else:
    print('{} nao e um numero primo.'.format(n))
    