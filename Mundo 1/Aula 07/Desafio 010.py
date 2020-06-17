"""
DESAFIO 010: Conversor de Moedas

Crie um programa que leia quanto dinheiro ma pessoa tem 
na carteira e mostre quantos Dolares ela pode comprar

Considere U$ 1,00 = R$ 3,27
"""

r = float(input('Quanto dinheiro em Reais voce tem?'))
d = 3.27
print('/nA cotacao do Dolar esta a R$ {:.2f} hoje. com R$ {:.2f}, voce pode comprar  U$ {:.2f}!'.format(d, r, r / d))
