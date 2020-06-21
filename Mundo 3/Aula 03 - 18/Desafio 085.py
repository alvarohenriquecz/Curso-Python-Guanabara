"""
Desafio 085: Listas com Pares e Impares

Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha
separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente.
"""
numeros = [[], []]

for c in range(1, 7 + 1):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)

numeros[0].sort()
numeros[1].sort()

print('-=' * 30)
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')
