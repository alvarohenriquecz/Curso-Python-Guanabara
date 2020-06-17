""" DESAFIO 012: Calculando Descontos

faca um algoritmo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto
"""

p = float(input('Qual e o preco do produto? '))
d = p * 0.05
r = p - d
print('\n O produto que custa $ {:.2f} fica por $ {:.2f} com 5% de dedsconto ($ {:.2f}.'.format(p, r, d)))
