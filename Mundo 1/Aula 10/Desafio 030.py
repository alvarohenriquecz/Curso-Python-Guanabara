"""
DESAFIO 030: par ou impar?

Crie um programa que leia um numero inteiro e mostre na tela se ele e PAR ou IMPAR.
"""
num = int(input('Digite um numero inteiro (ex: 55) '))
if num % 2 == 0:
    print('{} e um numero par!'.format(num))
else:
    print('{} e um numero impar!'.format(num))
    