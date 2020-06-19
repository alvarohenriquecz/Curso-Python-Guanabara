"""
Desafio 038: Comparando Numeros

Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor e maior.
- O segundo valor e maior.
- Nao existe um valor maior, os dois sao iguais.
"""

n1 = int(input('Digite o primeiro valor inteiro: '))
n2 = int(input('Digite o segundo valor inteiro: '))
if n1 == n2:
    print('{} e {} sao numeros exatamente iguais!'.format(n1, n2))
elif n1 > n2:
    print('{} e maior que {}'.format(n1, n2))
elif n2 > n1:
    print('{} e maior do que {}'.format(n2, n1))
