"""
Desafio 071: Simulador de Caixa Eletronico

Crie um programa que simule o funcionamento de caixa eletronico. No inicio, pergunte ao
usuario qual sera o valor a ser sacado (numero inteiro) e o programa vai informar quantas
cedulas de cada valor serao entregues.

OBS: Considere que o caixa possui cedulos de R$ 50, 20, 10 e 1
"""
sep = '=' * 40
c50 = 0
c20 = 0
c10 = 0
c1 = 0
titulo = 'BANCO CEV'
print(f'{sep}\n{titulo:^40}\n{sep}')
valor = int(input('Qual valor voce deseja sacar? R$ '))
print('')

while valor >= 50:
    valor -= 50
    c50 += 1

while valor >= 20:
    valor -= 20
    c20 += 1

while valor >= 10:
    valor -= 10
    c10 += 1

while valor >= 1:
    valor -= 1
    c1 += 1

print(f'Total de {c50} cédulas de R$ 50')
print(f'Total de {c20} cédulas de R$ 20')
print(f'Total de {c10} cédulas de R$ 10')
print(f'Total de {c1} cédulas de R$ 1')
print(sep)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
