"""
Em, Python, existem 3 tipos de Variaveis Compostas:
- Tuplas
- Listas
- Dicionarios

Exemplo de variavel simples:
lanche = 'Hamburguer'

Exemplo de Tupla (variavel Composta):
lanche = ('Hamburguer'), 'Suco', 'Pizza', 'Pudim')
Indices:    [0]      [1]    [2]     [3]

Nota 1: As Tuplas sao imutaveis!

Nota 2: Tuplas sao identificadas por "()" (parenteses). Nas versoes atuais do Python
nem e necessario colocar entre "()", mas facilita para melhor entendimento do codigo.
"""

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') # Tupla "lanche"

print(lanche) # Exibe ('Hamburguer', 'Suco', 'Pizza', 'Pudeim')

# lanche[1] = 'Refrigerante' -> Comando impossivel, pos tuplas sao imutaveis

print(lanche[0]) # Exibe Hamburguer
print(lanche[1]) # Exibe suco
print(lanche[2]) # exibe pizza
print(lanche[3]) # exibe pudim

print(lanche[0:2])  # Exibe ('Hambúrguer', 'Suco')
print(lanche[1:3])  # Exibe ('Suco', 'Pizza')
print(lanche[1:])  # Exibe ('Suco', 'Pizza', 'Pudim')
print(lanche[:2])  # Exibe ('Hambúrguer', 'Suco')
print(lanche[-1])  # Exibe Pudim
print(lanche[-2])  # Exibe Pizza
print(lanche[-3:])  # Exibe ('Suco', 'Pizza', 'Pudim')

print(len(lanche))  # Exibe 4 (número de elementos de "lanche")

print(sorted(lanche))  # Exibe os elementos da tupla "lanche" em ordem alfabética, na forma de lista

# For 1 - Somente o elemento
for comida in lanche:   # para cada "comida" em "lanche"...
    print(f'{comida}') # Exibe a "comida" atual

# For 2.1 - Elemento e posicao com o comando "range"
for cont in ranger(0, len(lanche)): # Para cada numero "cont" de 0 ao numero de elemento em "lanche".
    print(f'{lanche[cont]} na posicao {cont}') # Exibe o elemento na posicao "cont" de "lanche" e o valorde "cont"

# For 2.2 - Elemento e posicao com o comando "enumerate"
for pos, quecomida in enumerate(lanche): # Para cada posicao "pos" e elemento "quecomida" em "lanche"...
    print(f'{quecomida} na posicao {pos}') # Exibe o elemento "quecomida" e a posicao "pos" atuais
