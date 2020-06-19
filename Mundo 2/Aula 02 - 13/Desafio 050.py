"""
Desafio 050: Soma dos pares

Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas 
daqueles que forem pares. se o valor digitado for impar, desconsidere-o.
"""

t = 0
np = 0

for c in range(1, 7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        t += n
        np += 1

if np == 0:
    print('Voce nao digitou nenhum par, portanto, o seu total e 0.')
elif np == 1:
    print('Voce digitou {} numero par. O seu total e {}.'.format(np, t))
else:
    print('Voce digitou {} numeros pares. A soma total deles e {}.'.format(np, t))
