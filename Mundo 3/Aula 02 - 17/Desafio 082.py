"""
Desafio 082: Dividindo valores em varias listas

crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso, cria duas listas extras que vao
conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteudo das
tres listas geradas.
"""

lista, pares, impares = list(), list(), list()
while True:
    lisa.append(int(input('Digite um valor: ')))

    while True:
        continuar = str(input('Quer continuar [S/N]? ')).upper()[0]
        if continuar in 'SN':
            break
        else:
            print('Respostas invalida! Digite S para Sim ou N para nao.')
        
    if continuar == 'N':
        break

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print('-=' * 30)
print(f'A lista completa e {lista}.')
print(f'A lista de pares e {pares}.')
print(f'A lista de impares e {impares}.')
