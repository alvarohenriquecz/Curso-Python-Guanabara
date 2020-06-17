"""
DESAFIO 015: Aluguel de Carros

Escreva um rograma que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. calcule o preco a pagar,
sabendo que o carro custa R$ 60 por dia e R$ 0,015 por km rodado.
"""

km = float(input('Qual foi a quantidade de quilometros percorridos pelo caroo alugado? '))
d = int(input('Por quantos dias ele foi alugado? '))
t = (d * 60) + (km * 0.15)
print('O carro alugado por {} dias percorreu {:.2f} quilometros, e com isso sera preciso pagar R$ {:.2f}!'.format(d, km, t))
