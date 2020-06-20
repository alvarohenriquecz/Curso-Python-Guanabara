"""
Desafio 065: Maior e Menor valores

Crie um programa que leia varios numeros inteiros pelo teclado. no final da execucao, mostre a media entre
todos os valores e qual foi o maior e menor valores lidos. O programa deve perguntar ao usuario se ele
quer ou nao continuar a digitar valores.
"""

numeros = soma = menor = maior = 0
continuar = 'S'

while continuar == 'S':
    n = int(input('Digite um numero: '))
    if numeros == 0:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    numeros += 1
    soma += n

    continuar = str(input('Quer digitar outro numero [S/N]? ')).upper()
    while continuar != 'S' and continuar != 'N':
        print('Resposta invalida!')
        continuar = str(input('Quer digitar outro numero [S/N] ')).upper()
    
media = soma / numeros
if numeros == 1:
    print('Voce digitou apenas o numero {}.'.format(soma))
else:
    print('Voce digitou {} numeros. A media entre eles e {}.'.format(numeros, media))
    print('O menor numero digitado foi {}. O maior numero digitado foi {}.'.format(menor, maior))
