"""
Desafio 078: Maior e Menor valores na Lista

Faca um programa que leia 5 valores numericos e guarde-os em uma lista. No final, mostre
qual foi o maior e o menor valor digitado e as suas respectivas posicoes na lista.
"""

lista = list()
for n in range(0, 5):
    list.append(int(input(f'Digite um valor para a Posicao {n}:')))
maximo = max(lista)
minimo = min(lista)
print('-=' * 25)
print(f'Voce digitou os valores {lista}')

print(f'O maior valor digitado foi {maximo} nas posicoes ', end='')
for i, v in enumerate(lista):
    if v == maximo:
        print(f'{i}...', end='')

print(f'\nO menor valor digitado foi {minimo} nas posicoes ', end='')
for i, v in enumerate(lista):
    if v == minimo:
        print(f'{i}....', end='')

print('')
