"""
Desafio 079: Valores Unicos em uma lista

Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista.
Caso o numero ja exista la dentro, ele nao sera adicionado. No final, serao exibidos todos os
valores unicos digitados, em ordem crescente.
"""

lista = list()
cont = 0
msg1 = 'Digite um valor: '
msg2 = 'Valor adicionado com sucesso...'

while True:
    if cont == 0:
        lista.append(int(input(msg1)))
    else:
        num = int(input(msg1))
        if num not in lista:
            lista.append(num)
            print(msg2)
        else:
            print('Valor duplicado! Nao vou adicionar...')
    cont += 1

    while True:
        continuar = str(input('Quer continuar [S/N]? ')).upper()[0]
        if continuar in 'SN':
            break
        else:
            print('Resposta invalida! Digite S para sim e N para nao.')
    if continuar == 'N':
        break

lista.sort()
print('-='*30)
print(f'Voce digitou os valores {lista}')