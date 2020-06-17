"""
Desafio 018: Seno, Cosseno e Tangente

Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente
"""

from math import radians, sin, cos, tan
a = float(input('Digite o angulo para calcular: '))
ac = radians(a)
s = sin(ac)
c = cos(ac)
t = tan(ac)
print('\nO seno de {:.2f}º e {:.2f}, o cosseno e {:.2f}, e a tangente e {:.2f}!'.format(a, s, c, t))
