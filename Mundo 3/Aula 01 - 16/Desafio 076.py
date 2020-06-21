"""
Desafio 076: Listas de precos com tupla

Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos precos,
na sequencia. No final, mostre uma linguagem de precos, organizando os dadosem forma tabular.

"""

div = '-' * 40
produtos = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

i, f = 0, 1
tam = len(produtos)

print(div)
print(f'{"LISTAGEM DE PRECOS":^40}')
print(div)
while f < tam:
    print(f'{produtos[i]:.<31}R$ {produtos[f]:>6.2f}', end='\n')
    i += 2
    f += 2
print(div)
