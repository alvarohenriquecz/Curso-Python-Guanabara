""" 
Desafio 036: Aprovando Emprestimo

Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
Pergunte o valor da casa, o salario do comprador e quantos anos ele vai pagar.
A prestacao mensal nao pode exceder 30% do salario, ou entao o emprestimo sera negado.
"""

casa = float(input('Qual e o valor da casa que voce deseja comprar? R$ '))
salario = float(input('Quanto voce ganha por mes? R$ '))
anos = int(input('Em quantos anos voce pretende paga? '))
meses = anos * 12
prestacoes = casa / meses
minimo = salario * 30 / 100
print('Entao voce deseja comprar uma casa no valor R$ {:.2f}'.format(casa), end=' ')
print('em {}x ({} anos) de R$ {:.2f}, correto?'.format(meses, anos, prestacoes))
print('Seu salario corresponde a R$ {:.2f}, portanto,'.format(salario), end=' ')
print('cada prestacao nao devera exceder o valor de R$ {:.2f} (30%).'.format(minimo))
if prestacoes > minimo:
    print('Lamentamos, mas NAO poderemos lhe conceder o emprestimo!')
else:
    print('Sendo assim, Poderemos lhe conceder o emprestimo!')
