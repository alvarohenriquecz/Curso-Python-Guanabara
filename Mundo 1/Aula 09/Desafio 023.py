"""
DESAFIO 023: Separando Digitos de um Numero

Faca um programa que leia um Numero de 0 a 9999 e mostre na tela cada um dos digitos separados .

Ex:
Digite um numero: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
"""

n = int(input('Digite um umero de 0 a 9999'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('nUnidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar:' {}.format(m))
