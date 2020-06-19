"""
Desafio 034: Aumentos Multiplos

Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
Para salarios superiores a R$ 1.250,00, calcule um aumento de 10%
Para inferiores ou iguais, aumento de 15%
"""

salario = float(input('Digite o salario do funcionario: '))
if salario > 1250:
    novo_salario = (salario * 0.10) + salario
    print('O salario atual de R$ {:.2f} aumentou em 10% (R$ {:.2f},'.format(salario, salario * 0.10), end=' ')
    print('Totalizando R$ {:.2f}!'.format(novo_salario))
else:
    novo_salario = (salario * 0.15) + salario
    print('O salario atual de R$ {:.2f} aumentou em 15% ( R$ {:.2f},'.format(salario, salario * 0.15), end=' ')
    print('Totalizando R$ {:.2f}!'.format(novo_salario))
