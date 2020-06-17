""" Desafio 013: Reajuste Salarial 

Faca um algoritmo que leia o salario de um
funcionario e mostre seu novo salario,com 15% de acrescimo
"""

s = float(input('Qual e o salario do funcionario? '))
a  = s * 0.15
r = s + a
print('\n O salario atual e {:.2f}, e com o aumento de 15% ($ {:.2f} ficara $ {:.2f}'.format(s, a, r))

