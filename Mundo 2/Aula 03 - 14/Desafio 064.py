"""
Desafio 064: Tratando Varios Valores v1.0

Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar
o valor 999, que e a condicao de parada. No final, mostre quantos numeros foram digitado e qual foi a soma 
entre eles (desconsiderando o flag).
"""

n = int(input('Digitando um numero qualquer (ou digite 999 paraa encerrar o programa): '))
if n != 999:
    numeros = 1
    soma = n
else:
    numeros = 0
    soma = 0

while n != 999:
    n = int(input('Digite um numero qualquer (ou digite 999 para encerrar o programa): '))
    if n != 999:
        soma += n
        numeros += 1

if numeros == 0:
    print('Voce nao digitou nenhum numero.')
elif numeros == 1:
    print('Voce digitou somente o numero {}.'.format(soma))
else:
    print('Voce digitou {} numeros. A soma total deles e {}.'.format(numeros, soma))
