"""
Desafio 017: Catetos e Hipotenusa

Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um retangulo, calcule e mostre o comprimeto da hipotenusa
"""
from math import hypot
c1 = float(input('Digite o comprimento do cateto oposto: '))
c2 = float(input('Digite o comprimento do cateto adjacente: '))
r = hypot(c1, c2)
print('\nO comprimento da hipotenusa e {}!'.format(r))
